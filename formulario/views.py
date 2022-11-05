from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import CreateView
from dal import autocomplete

from .models import Cancion


# Create your views here.

class formPrincipal(CreateView):

    model = Programa
    template_name = "formulario/formulario_incial.html"
    form_class = ProgramaForm
    success_url = '.'



