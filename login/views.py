from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import User

import json
import hashlib

developer = "Diana Vita"
judul = "PENERAPAN STEGANOGRAFI PADA CITRA DIGITAL MENGGUNAKAN METODE CHINESE REMAINDER THEOREM"

# Create your views here.
def login_page(request):
    context = {
        'judul' : judul,
        'developer' : developer
    }
    return render(request, 'login/login.html', context)