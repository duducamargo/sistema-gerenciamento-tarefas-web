from django.shortcuts import render
from django.http import HttpResponse

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
