from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Usuario
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            messages.error(request, "Usuário não encontrado.")
            return render(request, "cadastro/login.html")

        if check_password(senha, usuario.senha):
            messages.success(request, "Login realizado com sucesso!")
            return redirect("home")
        else:
            messages.error(request, "Senha incorreta.")
            return render(request, "cadastro/login.html")

    return render(request, "cadastro/login.html")


@csrf_protect
def cadastro(request):
    if request.method == "POST":
        novo_usuario = Usuario()
        novo_usuario.primeiro_nome = request.POST.get("primeiro_nome")
        novo_usuario.ultimo_nome = request.POST.get("ultimo_nome")
        novo_usuario.email = request.POST.get("email")
        novo_usuario.senha = make_password(request.POST.get("senha"))
        novo_usuario.save()

        return redirect("login")

    return render(request, "cadastro/cadastro.html")
