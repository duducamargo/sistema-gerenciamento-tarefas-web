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

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Usuario  # Certifique-se de importar o modelo correto
from django.views.decorators.csrf import csrf_protect
import random

@csrf_protect
def cadastro(request):
    numero_aleatorio = random.randint(1, 3)

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

        match numero_aleatorio:
            case 1:
                novo_usuario.foto_perfil = "foto_perfil_1.png"
            case 2:
                novo_usuario.foto_perfil = "polar-bear.png"
            case 3:
                novo_usuario.foto_perfil = "reindeer.png"
            case _:
                novo_usuario.foto_perfil = "foto_perfil_1.png"

        novo_usuario.save()

        return redirect("login")

    return render(request, "cadastro/cadastro.html")
