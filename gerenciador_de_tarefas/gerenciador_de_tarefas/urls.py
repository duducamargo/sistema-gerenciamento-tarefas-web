from django.contrib import admin
from django.urls import path
from tasks import views as TaskViews
from cadastro import views as CadastroViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CadastroViews.login, name='login'),
    path('cadastro/', CadastroViews.cadastro, name='cadastro'),
    path('tasks/', TaskViews.tasks, name='tasks'),
    path('nova_task/', TaskViews.nova_task, name='nova_task'),
    path('editar_task/', TaskViews.editar_task, name='editar_task'),
]
