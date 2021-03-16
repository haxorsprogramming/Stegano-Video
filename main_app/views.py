from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string
from stegano import lsb
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

import binascii
import cv2
import math
import hashlib
import datetime

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
    kdPengujian = get_random_string(5)
    kunci = get_random_string(20)
    save_kunci = Kunci_RSA.objects.create(kd_kunci=kdPengujian, kunci=kunci, active='1')
    save_kunci.save()
    context = {
        'status' : 'sukses'
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
    videoPath = "ladun/data_video_upload/"+video_name
    kd_pengujian = video_name.split(".")
    kd_fix = kd_pengujian[0]
    data_encode = Encode_Pesan.objects.filter(kd_uji__contains=kd_fix).first()
    pesan_video = data_encode.message_encode
    pesan = hidden_message(videoPath)
    context = {
        'kdKunci' : '8922',
        'status' : 'sukses',
        'nama_video' : video_name,
        'hash_data' : pesan,
        'kdPengujian' : kd_pengujian[0],
        'pesan' : pesan_video,
        'kunci_input' : kunciRsa
    }
    return JsonResponse(context, safe=False)

@csrf_exempt
def upload_video(request):
    count = 0
    kdPengujian = get_random_string(10)
    video = request.FILES['txtVideo']
    fs = FileSystemStorage()
    fs.save("ladun/data_video_upload/"+kdPengujian+".mp4", video)
    # alamat video yang sudah di upload
    videoPath = "ladun/data_video_upload/"+kdPengujian+".mp4"
    captureData = cv2.VideoCapture(videoPath)
    frameRate = captureData.get(5)
    x = 1
    while(captureData.isOpened()):
        idFrame = captureData.get(1)
        ret, frame = captureData.read()
        if(ret != True):
            break
        if(idFrame % math.floor(frameRate) == 0):
            filename = "ladun/keras_proses/"+kdPengujian+"_frame_%d_.jpg" % count; count+=1
            cv2.imwrite(filename, frame)
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
    }
    return JsonResponse(context, safe=False)

@csrf_exempt
def tes_enkripsi_rsa(request):
    # keyPair = RSA.generate(1024)
    # pubKey = keyPair.publickey()
    # pubSplit = str(pubKey).split(" ")
    # privSplit = str(keyPair).split(" ")
    # pubRsaKey = pubSplit[4]
    # privRsaKey = privSplit[4]
    # generator_key = get_random_string(80)
    # pesan = b'Diana vita'
    # pubKeyStr = 'MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKRSDa5YWtAdsKZYPef0h2UZItIL7FqTxh/N4cXQtr0BBT2C60AVlVeIC5Qzn21P5hHIlEAoUNowOau2msGaNVUCAwEAAQ=='
    # print(pubKey)
    # enkriptor = PKCS1_OAEP.new(pubSplit[4])
    # pesan_enkripsi = enkriptor.encrypt(pesan)
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
    kunci = request.POST['kunci']
    hash_key = request.POST['hashKey']
    now = datetime.datetime.now()
    total_kunci = Kunci_RSA.objects.filter(kunci__contains=kunci).count()
    if total_kunci > 0 :
        status_kunci = 'sukses' 
        save_encode = Encode_Pesan.objects.create(kd_uji=kdUji, nama_video="Pengujian Enskripsi", nama_pengujian="-", rsa=kunci, rsa_crt=hash_key, a_value=0, c_value=0, m_value=0, x_0="-", crt_value=0, waktu_pengujian=now, message_encode=pesan)
        save_encode.save()
    else:
        status_kunci = 'error'
    # Encode_Pesan
    context = {
        'status' : 'sukses',
        'kdUji' : kdUji,
        'status_kunci' : status_kunci
    }
    return JsonResponse(context, safe=False)

def generateRsa(generator):
    keyPair = RSA.generate(1024)
    pubKey = keyPair.publickey()
    pubSplit = str(pubKey).split(" ")
    privSplit = str(keyPair).split(" ")
    pubRsaKey = pubSplit[4]+get_random_string(20)
    privRsaKey = privSplit[4]+get_random_string(100)
    keyData = {
        'private' : privRsaKey,
        'public' : pubRsaKey
    }
    return keyData;

def hidden_message(filename):
    h = hashlib.sha1()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    
    return h.hexdigest()