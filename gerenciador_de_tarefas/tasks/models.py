from django.db import models
from cadastro.models import Usuario

class Task(models.Model):
    nome = models.CharField(max_length=255)
    atribuido_para = models.ForeignKey(Usuario, related_name='tasks_atribuidas', on_delete=models.CASCADE) 
    descricao = models.TextField(blank=True) 
    data_vencimento = models.DateField()
    status = models.CharField(max_length=50)
    criado_por = models.ForeignKey(Usuario, related_name='tasks_criadas', on_delete=models.CASCADE)  
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

