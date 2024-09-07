from django.shortcuts import render
from django.http import HttpResponse

def tasks(request):
    return render(request, 'tasks/index.html')

# Create your views here.
