from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.




class CancionResources(resources.ModelResource):
    fields = "__all__"
    class Meta:
        model = Cancion
@admin.register(Cancion)
class CancionAdmin(ImportExportModelAdmin):
    resource_class = CancionResources
    list_display = (
        "cancion", "version"
    )
    search_fields = ("cancion"), 
    ordering = ["cancion"]

class ProgramaAdmin(admin.ModelAdmin):
    ordering = ["nombre"]
    autocomplete_fields = ["cancion"]

admin.site.register(Nombre)

admin.site.register(Tonalidad)
admin.site.register(Programa, ProgramaAdmin)