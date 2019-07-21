from django.shortcuts import render

def index(request):
    context = {
        'title' : 'Forum',
    }
    return render(request, 'forum/index.html', context)