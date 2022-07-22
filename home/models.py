from urllib import request
from django.db import models

class Agenda(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    ativo = models.BooleanField()
    data = models.DateField(
        auto_now_add=True,
    )

    email = models.EmailField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return self.nome