from django.urls import path
from . import views

urlpatterns = [
    path('add-task/', views.nova_task, name='nova_task'),
    path('tasks/', views.tasks, name='tasks'),
]