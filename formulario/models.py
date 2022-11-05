from django.db import models

# Create your models here.


class Nombre(models.Model):
    name = models.CharField(max_length = 200, null = True)
    apellido = models.CharField(max_length = 200, null = True)
    Numero_whatsapp = models.CharField(max_length = 200, null = True)
    date_created = models.DateTimeField(auto_now_add= True)

    class Meta:
        verbose_name = 'Nombre'
        verbose_name_plural = 'Nombres'

    def __str__(self):
        return f"{self.name}"

class Cancion(models.Model):
    cancion = models.CharField(max_length = 1000, null = True)
    version = models.CharField(max_length = 1000, null = True)
    date_created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.cancion} version: {self.version}"


class Tonalidad(models.Model):
        tonalidad = models.CharField(max_length = 1000, null = True)
        def __str__(self):
            return f"{self.tonalidad}"

class Programa(models.Model):
    nombre = models.ForeignKey(Nombre, null=True, on_delete = models.SET_NULL)
    cancion = models.ForeignKey(Cancion, null=True, on_delete = models.SET_NULL)
    tonalidad = models.ForeignKey(Tonalidad, null=True, on_delete = models.SET_NULL)
    dia = models.DateTimeField()
    notas_adicionales = models.TextField(blank = True)
    date_created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"Programa del dia {self.dia} "
