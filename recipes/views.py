from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'nome': 'Jon Souza',
    })

def contato(request):
    return HttpResponse('contato')

def sobre(request):
    return HttpResponse('sobre')

def _home(request):
    return HttpResponse('HOME')