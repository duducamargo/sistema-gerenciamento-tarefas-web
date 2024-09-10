from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm
from .models import Board

# Create your views here.

def tasks(request):
    return render(request, 'tasks/tasks.html')

def nova_task(request):
    if request.method == "POST":
        nova_task = Board()
        nova_task.nome = request.POST.get('nome')
        nova_task.descricao = request.POST.get('descricao')
        nova_task.data = request.POST.get('data')
        nova_task.save()
        tasks = {
            'tasks': Board.objects.all()
        }
        return render(request, "tasks/tasks.html", tasks)
    return render(request, 'tasks/nova_task.html')

def editar_task(request):
    if request.method == "POST":
            return render(request, "tasks/tasks.html")
    
    return render(request, 'tasks/editar_task.html')
