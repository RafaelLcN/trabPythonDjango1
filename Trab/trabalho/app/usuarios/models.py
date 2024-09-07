from django.db import models

# Create your models here.

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    username = models.TextField(max_length=100)
    email = models.EmailField()
    senha = models.TextField(max_length=12)