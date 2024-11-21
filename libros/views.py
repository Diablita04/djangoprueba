from django.shortcuts import render
from libros.models import Libro
#from .models import Libro
#Para busqueda
from django.db.models import Q
#Para ListView
from django.views.generic.list import ListView

#Para crear, modificar y borrar
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from libros.models import Libro
from libros.forms import LibroForm

def buscarlib(request):
    busqueda = request.POST.get('buscar')
    buscarLib = Libro.objects.all()
    if busqueda:
        buscarLib = Libro.objects.filter(Q(titulo__icontains = busqueda)|Q(autor__icontains = busqueda)).distinct()
    return render(request, "libros/buscar.html",{'buscar':buscarLib})

def modifBusc(request):
    busqueda = request.POST.get('buscar')
    modifBusc = Libro.objects.all()
    if busqueda:
        modifBusc = Libro.objects.filter(Q(titulo__icontains = busqueda)|Q(autor__icontains = busqueda)).distinct()
    return render(request, "libros/modificarLibros.html",{'buscar':modifBusc})

class LibroListView(ListView):
    model = Libro

class LibroCreate(CreateView):
    model = Libro
    #fields = ["name"]
    form_class = LibroForm
    success_url = reverse_lazy('buscarM')

class LibroUpdate(UpdateView):
    model = Libro
    #fields = ["name"]
    form_class = LibroForm
    template_name_suffix = "_update_form"
    def get_success_url(self):
        return reverse_lazy('buscarM')+'?Actualizado'
    
class LibroDelete(DeleteView):
    model = Libro
    def get_success_url(self):
        return reverse_lazy("buscarM")+'?Eliminado'
   
    
