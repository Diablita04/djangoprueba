from django.shortcuts import render,redirect
#Para login
from django.contrib.auth.decorators import login_required

from clientes.models import Clientes
# Create your views here.
#Para búsqueda
from django.db.models import Q
#Para ListView
from django.views.generic.list import ListView

#Para crear, modificar y borrar
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from clientes.models import Clientes
from clientes.forms import ClientesForm



#def clientes(request):
#    clientes = Clientes.objects.all()
#    return render(request, "clientes/clientes_list.html", {'misClientes':clientes})

#Para búsqueda
@login_required
def buscarPrest(request):
    busqueda = request.POST.get('buscarPrestamo')
    buscarPrest = Clientes.objects.all()
    if busqueda:
        buscarPrest = Clientes.objects.filter(Q(nombre__icontains = busqueda)|(Q(dni__icontains = busqueda))|Q(nombrelibro__icontains = busqueda)).distinct()
    return render(request, "clientes/buscarPrestamo.html",{'buscarPrestamo':buscarPrest})

class ClientesListView(ListView):
    model = Clientes

class ClientesCreate(CreateView):
    model = Clientes
    #fields = ["name"]
    form_class = ClientesForm
    success_url = reverse_lazy('buscarL')

class ClientesUpdate(UpdateView):
    model = Clientes
    #fields = ["name"]
    form_class = ClientesForm
    template_name_suffix = "_update_form"
    def get_success_url(self):
        return reverse_lazy('buscarL')+'?Actualizado'
    
class ClientesDelete(DeleteView):
    model = Clientes
    def get_success_url(self):
        return reverse_lazy("buscarL")+'?Eliminado'