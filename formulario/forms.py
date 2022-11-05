from django import forms
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin
from .models import Programa, Cancion


class ProgramaForm(forms.ModelForm):
    
    class Meta:
        model = Programa
        fields =(
            'nombre',
            'cancion',
            'tonalidad', 
            'notas_adicionales', 
            'dia'
        )

        widgets = {
    
            'cancion' : AutocompleteSelect(
            Programa._meta.get_field('cancion').remote_field,
            admin.site,
            attrs={'placeholder': 'seleccionar...'},)
        }
        

  

