#Nos permite definir una ruta :
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = "Home"),

    # Crear el urls del formulario
    path('registrarCurso/', views.registrarCurso),

    # Crear el path eliminar Una ruta particular
    path('eliminarCurso/<codigo>',views.eliminarCurso),
    path('edicionCurso/<codigo>',views.edicionCurso),
    
    #Crear el path de editar 

    path('editarCurso/',views.editarCurso),

]