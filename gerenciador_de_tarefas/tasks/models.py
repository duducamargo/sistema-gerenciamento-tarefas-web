from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
    
