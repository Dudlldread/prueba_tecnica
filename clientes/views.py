import json
import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import Http404

from .models import Cliente

class LandView(ListView):
    template_name = "land_page.html"
    model = Cliente
    context_object_name = 'clientes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clientes = self.get_queryset()
        clientes = Cliente.objects.all()
        context['clientes'] = clientes

        return context

class AddView(CreateView):
    template_name = "formulario.html"
    model = Cliente
    fields = ('nombre','apellido','nacimiento','email','telefono',)
    success_url = reverse_lazy('home')

class DView(DetailView):
    template_name = "consulta.html"
    model = Cliente
    context_object_name = 'cliente'
    slug_field = 'email'
    slug_url_kwarg = 'email'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        clientes = self.get_queryset()
        clientes = Cliente.objects.filter(email=kwargs['object'].email)
        context['clientes'] = clientes
        return context

class Update_View(UpdateView):

    model = Cliente
    template_name = 'actualizacion.html'
    context_object_name = 'client'
    fields = ('nombre','apellido','nacimiento','email','telefono',)

    def get_success_url(self):
        return reverse_lazy('home')

class Delete_View(DeleteView):
    model = Cliente
    template_name = 'eliminar.html'
    success_url = reverse_lazy('home')

def consult_view(request, email):    
    context = []
    url ="http://localhost:8000/api/" + email
    resp = requests.get(url)
    context = resp.json()

    return render(request, 'consult.html', context)

def consult(request,email):
    try:
        clientes = Cliente.objects.filter(email=email)
        context = {
            'id': clientes[0].id,
            'nombre' : clientes[0].nombre,
            'apellido' : clientes[0].apellido,
            'fecha_de_nacimiento' : str(clientes[0].nacimiento),    
            'email' : clientes[0].email,
            'telefono' : clientes[0].telefono,
        }
    except : 
        context = {
            'error': "Cliente no encontrado"
        }
    
    json_object = json.dumps(context,indent=4) 
    return HttpResponse(json_object)
