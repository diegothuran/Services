from django.views import generic
from .models import Servico, Ordem_de_Servico, Empresa, Tecnico
from django.shortcuts import redirect, render,  get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import logout

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

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                all_ordens = Ordem_de_Servico.objects.all()
                return render(request, 'ServiceOrdering/index.html', {'all_ordens': all_ordens})
            else:
                return render(request, 'ServiceOrdering/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'ServiceOrdering/login.html', {'error_message': 'Invalid login'})
    return render(request, 'ServiceOrdering/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'ServiceOrdering/login.html', context)

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

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('service:index')

        return render(request, self.template_name, {'form': form})

def fechar_ordem_de_servico(request, ordem_de_servico_id):
    song = get_object_or_404(Ordem_de_Servico, pk=ordem_de_servico_id)
    try:
        if song.is_favorite:
            song.is_favorite = False
        else:
            song.is_favorite = True
        song.save()
    except (KeyError, Ordem_de_Servico.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})