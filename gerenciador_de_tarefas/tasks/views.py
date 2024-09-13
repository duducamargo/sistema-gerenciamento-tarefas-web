from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Task
from cadastro.models import Usuario
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from cadastro.views import login_required


@login_required
def tasks(request):
    tasks = Task.objects.all()
    usuario_logado_id = request.session.get("usuario_id")

    tasks = Task.objects.filter(atribuido_para_id=usuario_logado_id)

    context = {
        "tasks": tasks,
        "usuario_logado_id": usuario_logado_id,
    }

    return render(request, "tasks/tasks.html", context)


from cadastro.models import Usuario


@login_required
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
        nova_task.status = "Pendente"

        usuario_logado_id = request.session.get("usuario_id")
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

        return redirect("tasks")

    usuarios = Usuario.objects.all()
    return render(request, "tasks/nova_task.html", {"usuarios": usuarios})


@login_required
def editar_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.nome = request.POST.get("nome", task.nome)
        atribuicoes_id = request.POST.get("atribuicoes")

        if atribuicoes_id:
            try:
                usuario_atribuido = Usuario.objects.get(id_usuario=atribuicoes_id)
                task.atribuido_para = usuario_atribuido
            except Usuario.DoesNotExist:
                messages.error(request, "Usuário atribuído não encontrado.")
                return render(
                    request,
                    "tasks/editar_task.html",
                    {"task": task, "usuarios": Usuario.objects.all()},
                )

        task.descricao = request.POST.get("task", task.descricao)
        task.status = request.POST.get("status", task.status)
        task.data_vencimento = request.POST.get("data", task.data_vencimento)
        task.save()

        return redirect("tasks")

    usuarios = Usuario.objects.all()
    return render(
        request, "tasks/editar_task.html", {"task": task, "usuarios": usuarios}
    )


@login_required
def deletar_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.delete()
        return redirect(
            "tasks"
        )  
    return redirect("tasks")
