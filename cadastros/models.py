from enum import auto
from pyexpat import model
from django.db import models

# Create your models here.
class Apto(models.Model):
    
    apto = models.IntegerField(verbose_name='Apartamento')
    resp = models.CharField(max_length=50, verbose_name='Responsável')
    email = models.EmailField(max_length=254)

    def __str__(self) -> str:
        return f'{self.apto} - {self.resp}'
    
class Item(models.Model):
    
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=150, verbose_name='Descrição')

    def __str__(self) -> str:
        return f'{self.nome} - {self.descricao}'
    
class Tipo(models.Model):
    
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=150, verbose_name='Descrição')

    def __str__(self) -> str:
        return f'{self.nome} - {self.descricao}'
    
class Registro(models.Model):
    
    data = models.DateField()
    valor = models.DecimalField(max_digits=20, decimal_places=2)
    id_tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, verbose_name='Tipo')
    id_item = models.ForeignKey(Item, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Item')
    qtd = models.IntegerField(verbose_name='Quantidade')
    id_apto = models.ForeignKey(Apto, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Apartamento')

    def __str__(self) -> str:
        return f'[{self.data}] R$ {self.valor}'

