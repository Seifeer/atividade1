from django.db import models

# Create your models here.

class Despesa(models.Model):
    data_criacao= models.DateField()
    tipo_despesa= models.CharField(max_lenght=50)
    descricao= models.TextField()
    forma_pagamento= models.CharField(max_lenght=50)
    vencimento= models.DateField()
g