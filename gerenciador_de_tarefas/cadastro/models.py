from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True) 
    primeiro_nome = models.CharField(max_length=50)
    ultimo_nome = models.CharField(max_length=50)
    foto_perfil = models.CharField(max_length=100, default="foto_perfil_1.png")
    senha = models.CharField(max_length=255) 
