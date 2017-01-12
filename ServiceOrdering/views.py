from django.views import generic
from .models import Servico, Ordem_de_Servico, Empresa, Tecnico
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse

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
    #template_name = 'ServiceOrdering/ordem_de_servico_form.html'
    #context_object_name = 'ordem_de_servico'
    fields = '__all__'

    def get_success_url(self):
        return reverse('service:detail', kwargs={'pk': self.object.pk})


    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CreateOrdem, self).get_form_kwargs(
            *args, **kwargs)
        return kwargs