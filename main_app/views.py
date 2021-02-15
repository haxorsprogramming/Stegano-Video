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
    context = {
        'kdUji' : kdPengujian,
        'status' : 'sukses',
        'kunci' : pesan,
        'total_citra' : count
    }
    return JsonResponse(context, safe=False)

@csrf_exempt
def tes_enkripsi_rsa(request):
    keyPair = RSA.generate(1024)
    pubKey = keyPair.publickey()
    pubSplit = str(pubKey).split(" ")
    privSplit = str(keyPair).split(" ")
    pubRsaKey = pubSplit[4]
    privRsaKey = privSplit[4]
    generator_key = get_random_string(80)
    # pesan = b'Diana vita'
    # pubKeyStr = 'MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKRSDa5YWtAdsKZYPef0h2UZItIL7FqTxh/N4cXQtr0BBT2C60AVlVeIC5Qzn21P5hHIlEAoUNowOau2msGaNVUCAwEAAQ=='
    # print(pubKey)
    # enkriptor = PKCS1_OAEP.new(pubSplit[4])
    # pesan_enkripsi = enkriptor.encrypt(pesan)

    context = {
        'status' : 'sukses',
        'pubKey' : pubRsaKey,
        'privKey' : privRsaKey,
        'generator' : generator_key
    }
    return JsonResponse(context, safe=False)


def hidden_message(filename):
    h = hashlib.sha1()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    
    return h.hexdigest()