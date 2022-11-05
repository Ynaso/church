from django.urls import path

from . import views

from django.urls import re_path as url

app_name = "formulario_app"
urlpatterns = [
    
   path(
        '',
        views.formPrincipal.as_view(),
        name='formulario'
    ),

]
