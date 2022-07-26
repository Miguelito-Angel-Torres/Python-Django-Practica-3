from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo= models.CharField(primary_key=True, max_length=6)
    nombre= models.CharField(max_length=100)
    #models.PositiveSmallIntegerFiel : es un entero 
    creditos= models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural ="Cursos"

    def __str__(self):
        return self.codigo + self.nombre 
        # texto = "{0} ({1})"
        # return texto.format(self.codigo,self.creditos)  





#Migraciones:
# python manage.py makemigrations
#python manage.py migrate 
#Super Usuario:
#python manage.py createsuperuser
# nory 123456