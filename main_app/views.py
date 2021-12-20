from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string
from stegano import lsb
#from Crypto.PublicKey import RSA
#from Crypto.Cipher import PKCS1_OAEP
from PIL import Image

import binascii
import cv2
import math
import hashlib
import datetime
import random
from numpy import mod
import sympy
import time
import matplotlib.pyplot as plt

from .models import Encode_Pesan
from .models import Kunci_RSA

# Create your views here.
def main_dash(request):
    ip_address = request.META['REMOTE_ADDR']

    context = {
        'aplikasi' : '-',
        'developer' : 'Diana Vita',
        'ip_address' : ip_address
    }
    return render(request, 'dashboard/main.html', context)

def beranda(request):
    context = {
        'status' : 'sukses'
    }
    return render(request, 'dashboard/beranda.html', context)

def pengujian(request):
    context = {
        'status' : 'sukses'
    }
    return render(request, 'dashboard/pengujian.html', context)

def pengujian_decode(request):
    context = {
        'status' : 'sukses'
    }
    return render(request, 'dashboard/pengujian-decode.html', context)

def buat_kunci_rsa(request):
    dataKunciRsa = Kunci_RSA.objects.all().values()
    context = {
        'status' : 'sukses',
        'kunciRsa' : dataKunciRsa
    }
    return render(request, 'dashboard/buat-kunci-rsa.html', context)

@csrf_exempt
def buat_kunci_baru(request):
    # {'teks':teks, 'kunci':kunci}
    teks = request.POST['teks']
    kunci = request.POST['kunci']
    kunci2 = request.POST['kunci2']
    

    # chiper = encrypt(teks, [e, n])

    #cek bilangan prima 
    cek_prima = checkBilanganPrima(int(kunci))
    cek_prima2 = checkBilanganPrima(int(kunci2))
    if(cek_prima == True or cek_prima2 == True):
        prima = False
        status = 'not_prime_number'
        hasil = ''
    else:
        prima = True
        # cek apakah nama kunci sudah ada 
        cek_kunci = Kunci_RSA.objects.filter(nama__contains=teks).count()
        if(cek_kunci < 1):
            p = int(kunci)
            q = int(kunci2)
            n = p * q
            phi = (p - 1) * (q - 1)
            # nilai e di tentukan sendiri
            e = 529
            d = modular_inverse(e, phi)
            dp = d % (p - 1)
            dq = d % (q - 1)
            qInv = modular_inverse(q, p)
            public_key = [e, n]
            p_key_s = listToString(str(public_key))
            private_key = [dp, dq, qInv, p, q]
            priv_key_s = listToString(str(private_key))
            save_kunci = Kunci_RSA.objects.create(nama=teks, p=p, q=q, dp=dp, dq=dq, q_inv=qInv, public_key=p_key_s, private_key=priv_key_s)
            save_kunci.save()
            status = 'success'
        else:
            status = 'double_kunci'
            
    context = {
        'status' : status
    }
    return JsonResponse(context, safe=False)

@csrf_exempt
def proses_hapus_kunci(request):
    kdKunci = request.POST['kdKunci']
    Kunci_RSA.objects.filter(kd_kunci__contains=kdKunci).delete()
    context = {
        'kdKunci' : kdKunci,
        'status' : 'sukses'
    }
    return JsonResponse(context, safe=False)

@csrf_exempt
def proses_decode(request):
    video = request.FILES['txtVideo']
    kunciRsa = request.POST['kunciRsa']
    video_name = video.name
    kd_pengujian = video_name.replace(".mp4", "")
    # cek apakah video terdaftar 
    total_v_data = Encode_Pesan.objects.filter(kd_uji__contains=kd_pengujian).count()
    if(total_v_data < 1):
        status = 'no_video'
        pesan = ''
    else:
        # cek apakah kunci rsa cocok 
        total_rsa_data = Encode_Pesan.objects.filter(kd_uji__contains=kd_pengujian).filter(chiper_text__contains=kunciRsa).count()
        if(total_rsa_data < 1):
            status = 'no_rsa_key'
            pesan = ''
        else:
            status = 'sukses'
            data_decode = Encode_Pesan.objects.filter(kd_uji__contains=kd_pengujian).filter(chiper_text__contains=kunciRsa).first()
            pesan = data_decode.message_encode

    context = {
        'kd_pengujian' : kd_pengujian,
        'kunci_rsa' : kunciRsa,
        'status' : status,
        'pesan' : pesan
    }
    return JsonResponse(context, safe=False)

@csrf_exempt
def upload_video(request):
    count = 0
    kdPengujian = get_random_string(10)
    video = request.FILES['txtVideo']
    fs = FileSystemStorage()
    fs.save("ladun/data_video_upload/"+kdPengujian+".mp4", video)
    fs.save("ladun/data_video_hash/"+kdPengujian+".mp4", video)
    # alamat video yang sudah di upload
    videoPath = "ladun/data_video_upload/"+kdPengujian+".mp4"
    captureData = cv2.VideoCapture(videoPath)
    frameRate = captureData.get(5)
    x = 1
    pic_data = []
    while(captureData.isOpened()):
        idFrame = captureData.get(1)
        ret, frame = captureData.read()
        if(ret != True):
            break
        if(idFrame % math.floor(frameRate) == 0):
            filename = "ladun/keras_proses/"+kdPengujian+"_frame_%d_.jpg" % count; count+=1
            cv2.imwrite(filename, frame)
            img = Image.open(filename)
            colors = img.getpixel((320,240))
            pic_data.append(colors)

    pesan = hidden_message(videoPath)
    #rsa
    newRsaF1 = generateRsa(kdPengujian)
    newRsaF5 = generateRsa(kdPengujian)
    newRsaF10 = generateRsa(kdPengujian)
    newRsaF15 = generateRsa(kdPengujian)
    newRsaF20 = generateRsa(kdPengujian)

    context = {
        'kdUji' : kdPengujian,
        'status' : 'sukses',
        'kunci' : pesan,
        'total_citra' : count,
        'rsaF1' : newRsaF1,
        'rsaF5' : newRsaF5,
        'rsaF10' : newRsaF10,
        'rsaF15' : newRsaF15,
        'rsaF20' : newRsaF20,
        'pic_data' : pic_data
    }
    return JsonResponse(context, safe=False)

@csrf_exempt
def tes_enkripsi_rsa(request):
    newRsa = generateRsa("Diana Vita")
    print(newRsa)
    context = {
        'status' : 'sukses',
        'newRsa' : newRsa
    }
    return JsonResponse(context, safe=False)

@csrf_exempt
def proses_enkripsi(request):
    kdUji = request.POST['kdUji']
    pesan = request.POST['pesan']
    kunciPublik = request.POST['kunci']
    kunciPrivate = request.POST['kunciPrivate']
    hash_key = request.POST['hashKey']
    
    now = datetime.datetime.now()
    total_kunci = Kunci_RSA.objects.filter(public_key__contains=kunciPublik).filter(private_key__contains=kunciPrivate).count()
    if total_kunci > 0 :
        dataKunci = Kunci_RSA.objects.filter(public_key__contains=kunciPublik).filter(private_key__contains=kunciPrivate).first()
        # p = dataKunci.p
        # q = dataKunci.q
        # dp = dataKunci.dp
        # dq = dataKunci.dq
        key_pub_1 = kunciPublik.replace("[", "")
        key_pub_2 = key_pub_1.replace("]", "")
        key_pub_s = key_pub_2.split(", ")
        e = int(key_pub_s[0])
        n = int(key_pub_s[1])
        key_priv_1 = kunciPrivate.replace("[", "")
        key_priv_2 = key_priv_1.replace("]", "")
        key_priv_s = key_priv_2.split(", ")
        enkripsiData = encrypt(pesan,[e,n])
        print(enkripsiData)
        # print(key_pub_s[0])
        status_kunci = 'sukses' 
        save_encode = Encode_Pesan.objects.create(kd_uji=kdUji, nama_video="Pengujian Enkripsi", nama_pengujian="-", rsa=key_pub_s, rsa_crt=key_priv_s, a_value=0, c_value=0, m_value=0, chiper_text=enkripsiData, crt_value=0, waktu_pengujian=now, message_encode=pesan)
        save_encode.save()
        
        cipher = listToString(str(enkripsiData))
    else:
        status_kunci = 'error'
        cipher = ''
    # Encode_Pesan
    context = {
        'status' : 'sukses',
        'kdUji' : kdUji,
        'status_kunci' : status_kunci,
        'chiper' : cipher
    }
    return JsonResponse(context, safe=False)

def generateRsa(generator):
    pubRsaKey = get_random_string(20)
    privRsaKey = get_random_string(100)
    keyData = {
        'private' : pubRsaKey,
        'public' : privRsaKey
    }
    return keyData

def hidden_message(filename):
    h = hashlib.sha1()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    
    return h.hexdigest()
 
def checkBilanganPrima(s):
    num = s
    # To take input from the user
    #num = int(input("Enter a number: "))
    # define a flag variable
    flag = False
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break
    return flag

def to_ascii(text):
    ascii_values = [ord(character) for character in text]
    return ascii_values

def listToString(s): 
    # initialize an empty string
    str1 = "" 
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    # return string  
    return str1 


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def convert_to_int(text):
    converted = []
    for letter in text:
        converted.append(ord(letter) - 96)
    return converted


def convert_to_ascii(text):
    converted = ''
    for number in text:
        converted = converted + chr(number + 96)
    return converted


def choose_e(phi, n):
    print('Choosing e...')
    for e in range(2 ** 31, 2, -1):
        if gcd(e, phi) == 1 and gcd(e, n) == 1:
            return e


def modular_inverse(a, m):  # modular inverse of e modulo phi
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x = x + m0

    return x


def encrypt(text, public_key):
    key, n = public_key
    ctext = [pow(ord(char), key, n) for char in text]
    return ctext


def decrypt(ctext, private_key, d, n):
    m = []
    for x in ctext:
        c = pow(x,  d) % n
        m.append(c)
    return m


# The CRT method of decryption is about four times faster overall
# Even though there are more steps in this procedure,
# the modular exponentiation to be carried out uses much shorter exponents and so it is less expensive in the end
def CRT(p, q, dP, dQ, c):
    qInv = modular_inverse(q, p)
    m1 = pow(c, dP, p)
    m2 = pow(c, dQ, q)
    h = (qInv * (m1 - m2)) % p
    m = m2 + h * q
    return m
