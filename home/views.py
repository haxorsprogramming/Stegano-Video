from django.shortcuts import render
from django.http import HttpResponse
import cv2
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import hashlib

# Create your views here.
def home_page(request):
    # count = 0
    # videoFile = "ladun/data_uji/lulu.mp4"
    # cap = cv2.VideoCapture(videoFile)
    # frameRate = cap.get(5)
    # x = 1
    # while(cap.isOpened()):
    #     idFrame = cap.get(1)
    #     ret, frame = cap.read()
    #     if(ret != True):
    #         break
    #     if(idFrame % math.floor(frameRate) == 0):
    #         filename = "keras_proses/frame_%d_.jpg" % count; count+=1
    #         cv2.imwrite(filename, frame)

    # cap.release()
    # pesan = hidden_message(videoFile)
    # print(pesan)
    context = {
        'status' : 'sukses'
    }
    return render(request, 'home/home.html', context)


def hidden_message(filename):
    h = hashlib.sha1()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    
    return h.hexdigest()

