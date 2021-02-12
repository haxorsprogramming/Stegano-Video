from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    context = {
        'status' : 'sukses'
    }
    return render(request, 'home/home.html', context)