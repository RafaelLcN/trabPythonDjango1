"""
URL configuration for trabalho project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.usuarios import viewsUsuarios
from app.tarefas import viewsTarefas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewsUsuarios.home, name='home'),
    path('login', viewsUsuarios.login, name='login'),
    path('cadastro', viewsUsuarios.cadastro, name='cadastro'),
    path('logout', viewsUsuarios.logout, name='logout'),
    path('tarefas', viewsTarefas.tarefas, name='tarefas'),
    path('novaTarefa', viewsTarefas.novaTarefa, name='novaTarefa'),
    path('removerTarefa/<int:id_tarefa>/', viewsTarefas.removerTarefa, name='removerTarefa'),
    path('editarTarefa/<int:id_tarefa>/', viewsTarefas.editarTarefa, name='editarTarefa')
]
    