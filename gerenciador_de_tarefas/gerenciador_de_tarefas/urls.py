from django.contrib import admin
from django.urls import path, include
from tasks import views as TaskViews
from cadastro import views as CadastroViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CadastroViews.login, name='login'),
    path('cadastro/', CadastroViews.cadastro, name='cadastro'),
    path('tasks/', include('tasks.urls'))
]
