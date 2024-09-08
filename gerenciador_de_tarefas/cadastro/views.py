from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'cadastro/login.html')

def cadastro(request):
    return render(request, 'cadastro/cadastro.html')
