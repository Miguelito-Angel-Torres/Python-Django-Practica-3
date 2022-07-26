from django.contrib import admin

#Importacion del Modelo
from .models import Curso


class CursoAdmin(admin.ModelAdmin):
    list_display=("codigo","nombre","creditos")
    search_fields=("codigo","nombre")

#Registracion del Modelo
admin.site.register(Curso,CursoAdmin)

