from django.shortcuts import render

def index(request):
    context = {
        'title' : 'Anggota',
    }
    return render(request, 'anggota/index.html', context)