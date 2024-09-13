from django.db import models
from django.contrib.auth.models import User

class Tarefas(models.Model):
    id_tarefa = models.AutoField(primary_key=True)
    titulo = models.TextField()
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=[('Pendente', 'Pendente'), ('Em andamento', 'Em andamento'), ('Concluida', 'Concluida')])
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE, null = True)

