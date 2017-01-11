from django.contrib import admin
from .models import Tecnico, Empresa, Ordem_de_Servico, Servico

admin.site.register(Tecnico)
admin.site.register(Empresa)
admin.site.register(Ordem_de_Servico)
admin.site.register(Servico)
