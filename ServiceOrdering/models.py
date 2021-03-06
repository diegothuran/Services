from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse_lazy, reverse

# Create your models here.

class Tecnico(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class Empresa(models.Model):
    nome = models.CharField(max_length=200)
    cpf_cnpj = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nome

class Estado(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Ordem_de_Servico(models.Model):
    data = models.DateField()
    hora = models.CharField(max_length=5, default="00:00")
    servico = models.ForeignKey(Servico)
    observacao = models.TextField()
    empresa = models.ForeignKey(Empresa)
    contato = models.CharField(max_length=200, blank= True)
    fone = models.CharField(max_length=20, blank= True)
    tecnico = models.ForeignKey(Tecnico)
    agencia = models.CharField(max_length=200, blank=True)
    estado = models.ForeignKey(Estado, default=1)

    def get_absolute_url(self):
        return reverse('service:detail', kwargs={"pk": self.pk})

    def __str__(self):
        return self.empresa.nome

    class Meta:
        verbose_name = 'Ordem de Servico'
        verbose_name_plural = 'Ordens de Servico'