from django.views import generic
from .models import Servico, Ordem_de_Servico, Empresa, Tecnico
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

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

class UpdateOrdem(UpdateView):
    model = Ordem_de_Servico
    fields = '__all__'

class DeleteOrdem(DeleteView):
    model = Ordem_de_Servico
    success_url = reverse_lazy('service:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'ServiceOrdering/registration_form.html'

    #display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form  = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            