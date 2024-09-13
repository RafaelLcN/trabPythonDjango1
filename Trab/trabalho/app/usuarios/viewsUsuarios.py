from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from ..tarefas.models import Tarefas
from django.contrib.auth.decorators import login_required

def home(request):
    tarefas={
        'tarefas': Tarefas.objects.all()
    }
    return render(request, 'usuarios/home.html', tarefas)

def cadastro (request):
    if request.method == 'GET':
        return render(request, 'usuarios/cadastro.html')
    else:
        username= request. POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = User.objects.filter(username=username).first()

        if user:
            erro = "ERRO: Já existe um usuário com esse username."
            erro = {
                'erro' : erro
            }

            return render(request, 'usuarios/cadastro.html', erro)

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        login_django(request, user)
        return redirect('home')


def login (request):
    if request.method == 'GET':
        return render(request, 'usuarios/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        if user:
            login_django(request, user)
            return redirect('home')
        else:
            erro = "ERRO: Nome de usuário ou senha inválidos."
            erro = {
                'erro' : erro
            }

            return render(request, 'usuarios/login.html', erro)

def logout(request):
    auth_logout(request)
    return redirect('login')