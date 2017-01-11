from django.views import generic
from .models import Servico, Ordem_de_Servico, Empresa, Tecnico
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class IndexView(generic.ListView):
    template_name = 'ServiceOrdering/index.html'
    context_object_name = 'all_ordens'

    def get_queryset(self):
        return Ordem_de_Servico.objects.all()

class DetailView(generic.DetailView):
    model = Ordem_de_Servico
    template_name = 'ServiceOrdering/detail.html'

class CreateOrdem(CreateView):
    model = Ordem_de_Servico
    fields = '__all__'