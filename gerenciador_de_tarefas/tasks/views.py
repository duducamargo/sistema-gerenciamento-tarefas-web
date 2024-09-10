from django.shortcuts import render, redirect
from django.http import HttpResponse
<<<<<<< HEAD
from .forms import TaskForm
from .models import Board

# Create your views here.
def task_list(request):
    tasks = Board.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

        return render(request, 'tasks/add_task.html', {'form': form})
=======

def tasks(request):
    return render(request, 'tasks/tasks.html')

def nova_task(request):
    if request.method == "POST":
            return render(request, "tasks/tasks.html")
        
    return render(request, 'tasks/nova_task.html')

def editar_task(request):
    if request.method == "POST":
            return render(request, "tasks/tasks.html")
    
    return render(request, 'tasks/editar_task.html') 
>>>>>>> c928e0faaab417dc7645416da4b4c0506e9d9f29
