from django.contrib import admin
from django.urls import path

from home import views as home_app
from login import views as login_app

urlpatterns = [
    path('', home_app.home_page),
    path('login/', login_app.login_page),
]
