from django.contrib import admin
from django.urls import path

from home import views as home_app

urlpatterns = [
    path('', home_app.home_page),
    path('admin/', admin.site.urls),
]
