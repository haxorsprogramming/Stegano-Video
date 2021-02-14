from django.shortcuts import render

# Create your views here.
def main_dash(request):
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