from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Apto, Registro, Item, Tipo
from django.urls import reverse_lazy

# Update your views here.

# Create

class AptoCreate(CreateView):
    model = Apto
    fields = ['apto', 'resp', 'email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-apto')

class ItemCreate(CreateView):
    model = Item
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-item')

class TipoCreate(CreateView):
    model = Tipo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tipo')
    
class RegistroCreate(CreateView):
    model = Registro
    fields = ['data', 'valor', 'id_tipo', 'id_item', 'qtd', 'id_apto']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-registro')

# Update

class AptoUpdate(UpdateView):
    model = Apto
    fields = ['apto', 'resp', 'email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-apto')

class ItemUpdate(UpdateView):
    model = Item
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-item')

class TipoUpdate(UpdateView):
    model = Tipo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tipo')
    
class RegistroUpdate(UpdateView):
    model = Registro
    fields = ['data', 'valor', 'id_tipo', 'id_item', 'qtd', 'id_apto']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-registro')


# Delete

class AptoDelete(DeleteView):
    model = Apto
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-apto')

class ItemDelete(DeleteView):
    model = Item
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-item')

class TipoDelete(DeleteView):
    model = Tipo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-tipo')
    
class RegistroDelete(DeleteView):
    model = Registro
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-registro')

# List

class AptoList(ListView):
    model = Apto
    template_name = 'cadastros/listas/apto.html'
    success_url = reverse_lazy('listar-apto')

class ItemList(ListView):
    model = Item
    template_name = 'cadastros/listas/item.html'
    success_url = reverse_lazy('listar-item')

class TipoList(ListView):
    model = Tipo
    template_name = 'cadastros/listas/tipo.html'
    success_url = reverse_lazy('listar-tipo')
    
class RegistroList(ListView):
    model = Registro
    template_name = 'cadastros/listas/registro.html'
    success_url = reverse_lazy('listar-registro')
