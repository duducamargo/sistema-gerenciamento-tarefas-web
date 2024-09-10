from django.shortcuts import render, redirect
from django.http import HttpResponse
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
