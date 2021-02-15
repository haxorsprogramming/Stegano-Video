from django.contrib import admin
from django.urls import path

from home import views as home_app
from login import views as login_app
from main_app import views as main_app

urlpatterns = [
    path('', home_app.home_page),
    path('login/', login_app.login_page),
    path('login/proses', login_app.login_proses),
    path('dashboard/', main_app.main_dash),
    path('dashboard/beranda', main_app.beranda),
    path('dashboard/pengujian', main_app.pengujian),
    path('dashboard/pengujian/upload-video', main_app.upload_video)
]
