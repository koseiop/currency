from django.shortcuts import render

def index(request):

    context = {
        'base': = base,
        'currencies': currencies
    }
    return render(request, 'home.html', context)
