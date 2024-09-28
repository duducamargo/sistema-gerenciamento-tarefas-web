from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Usuario
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
import random

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'usuario_id' not in request.session:
            return redirect('login') 
        return view_func(request, *args, **kwargs)
    return wrapper

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
            request.session['usuario_id'] = usuario.id_usuario 
            messages.success(request, "Login realizado com sucesso!")
            return redirect("tasks") 
        else:
            messages.error(request, "Senha incorreta.")
            return render(request, "cadastro/login.html")

    return render(request, "cadastro/login.html")

@csrf_protect
def cadastro(request):
    if request.method == "POST":
        email = request.POST.get("email")
        
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "Este e-mail já está cadastrado.")
            return render(request, "cadastro/cadastro.html")

        novo_usuario = Usuario()
        novo_usuario.primeiro_nome = request.POST.get("primeiro_nome")
        novo_usuario.ultimo_nome = request.POST.get("ultimo_nome")
        novo_usuario.email = email
        novo_usuario.senha = make_password(request.POST.get("senha"))

        fotos_disponiveis = ["foto_perfil_1.png", "polar-bear.png", "reindeer.png"]
        numero_aleatorio = random.randint(0, len(fotos_disponiveis) - 1)
        novo_usuario.foto_perfil = fotos_disponiveis[numero_aleatorio]

        novo_usuario.save()

        return redirect("login")

    return render(request, "cadastro/cadastro.html")
