from django.urls import path
from . import views

urlpatterns = [
    path("", views.tasks, name="tasks"),
    path("add-task/", views.nova_task, name="nova_task"),
    path("editar_task/<int:id>/", views.editar_task, name="editar_task"),
    path("deletar_task/<int:id>/", views.deletar_task, name="deletar_task"),
    path("logout/", views.logout, name="logout"),
]
