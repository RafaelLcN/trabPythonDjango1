from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .models import Tarefas


@login_required
def tarefas (request):
    if (Tarefas.objects.filter(responsavel=request.user) is not None):
        if request.method == 'POST':
            tarefas = {
                'tarefas': Tarefas.objects.filter(responsavel=request.user, status=request.POST.get('status'))
            }

        else:
            tarefas = {
                'tarefas': Tarefas.objects.filter(responsavel=request.user)
            }

    return render(request, 'tarefas/tarefas.html', tarefas)

@login_required
def novaTarefa (request):
    if request.method == 'POST':
        tarefa = Tarefas()

        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.status = request.POST.get('status')
        tarefa.responsavel = request.user

        tarefa.save()

        return redirect('tarefas')
    else:
        return render(request, 'tarefas/novaTarefa.html')


@login_required
def editarTarefa(request, id_tarefa):
    tarefa = Tarefas.objects.get(id_tarefa=id_tarefa, responsavel=request.user)

    if request.method == 'POST':

        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.status = request.POST.get('status')
        tarefa.responsavel = request.user

        tarefa.save()

        return redirect('tarefas')
    else:
        tarefa = {
            'tarefa' : tarefa
        }
        return render(request, 'tarefas/editarTarefa.html', tarefa)


@login_required
def removerTarefa(request, id_tarefa):
    tarefa = Tarefas.objects.get(id_tarefa=id_tarefa, responsavel=request.user)
    tarefa.delete()
    return redirect('tarefas')





