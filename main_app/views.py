from django.shortcuts import render

# Create your views here.
def main_dash(request):
    ip_address = ''

    context = {
        'aplikasi' : '-',
        'developer' : 'Diana Vita'
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