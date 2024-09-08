from django.shortcuts import render
from django.http import HttpResponse

def tasks(request):
    return render(request, 'tasks/tasks.html')

