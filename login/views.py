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

@csrf_exempt
def login_proses(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    pass_hash = hashlib.md5(password.encode("utf-8")).hexdigest()
    total_user = User.objects.filter(username__contains=username).count()
    if total_user > 0 :
        data_user = User.objects.filter(username__contains=username).first()
        password_db = data_user.password
        if pass_hash == password_db:
            status = 'success'
        else:
            status = 'wrong_password'
    else:
        status = 'no_user'

    context = {
        'username' : username,
        'status' : status
    }
    return JsonResponse(context, safe=False)