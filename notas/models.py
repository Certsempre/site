from django.db import models
from datetime import datetime

# Create your models here.

class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    complemento = models.CharField(max_length=65)
    logradouro = models.CharField(max_length=65, null=False)
    numero = models.CharField(max_length=65, null=False)
    bairro = models.CharField(max_length=65, null=False)

class Cliente(models.Model):
    razao_social = models.CharField(max_length=65, primary_key=True)
    documento = models.CharField(max_length=18, blank=False, null=False)
    contato = models.CharField(max_length=100)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

class Notas(models.Model):
    cnpj = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=65)
    dado_bancario = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    status = models.CharField(max_length=65, default='Não emitida')

