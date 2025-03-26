from django.db import models
from django.contrib.auth.models import User

class Mesa(models.Model):
    numero = models.IntegerField(unique=True)
    capacidade = models.IntegerField()
    local = models.CharField(max_length=20, choices=[
        ('dentro', 'Dentro'),
        ('fora', 'Fora')
    ])
    
    def __str__(self):
        return f"Mesa {self.numero} ({self.local})"

class Reserva(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    
    pessoas = models.IntegerField()
    criancas = models.IntegerField(default=0)
    local_preferido = models.CharField(max_length=10, choices=[
        ('dentro', 'Dentro'),
        ('fora', 'Fora')
    ])
    
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('mesa', 'data', 'hora')
    
    def __str__(self):
        return f"Reserva de {self.nome} para {self.data} às {self.hora}"