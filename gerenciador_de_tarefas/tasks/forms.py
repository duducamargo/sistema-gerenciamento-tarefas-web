from django import forms
from .models import Board

class TaskForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['nome', 'descricao']
