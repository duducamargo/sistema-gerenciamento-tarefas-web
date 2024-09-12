from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Task
from cadastro.models import Usuario
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .forms import TaskForm
from .models import Board

def tasks(request):
    return render(request, 'tasks/tasks.html')

from cadastro.models import Usuario

@csrf_protect
def nova_task(request):
    if request.method == "POST":
        nova_task = Task()
        nova_task.nome = request.POST.get("nome")

        user_id = request.POST.get("atribuicoes")
        if user_id:
            try:
                usuario_atribuido = Usuario.objects.get(id_usuario=user_id)
                nova_task.atribuido_para = usuario_atribuido
            except Usuario.DoesNotExist:
                messages.error(request, "Usuário atribuído não encontrado.")
                return render(request, "tasks/nova_task.html")

        nova_task.data_vencimento = request.POST.get("data")
        nova_task.descricao = request.POST.get("task")

        usuario_logado_id = request.session.get('usuario_id')
        if usuario_logado_id:
            try:
                usuario_logado = Usuario.objects.get(id_usuario=usuario_logado_id)
                nova_task.criado_por = usuario_logado
            except Usuario.DoesNotExist:
                messages.error(request, "Usuário logado não encontrado.")
                return render(request, "tasks/nova_task.html")
        else:
            messages.error(request, "Nenhum usuário está logado.")
            return redirect("login")

        nova_task.save()

        return render(request, "tasks/tasks.html")

    usuarios = Usuario.objects.all()
    return render(request, 'tasks/nova_task.html', {'usuarios': usuarios})


def editar_task(request):
    if request.method == "POST":
            return render(request, "tasks/tasks.html")
    
    return render(request, 'tasks/editar_task.html')
