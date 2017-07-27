from django.db import models

# Create your models here.
class MovieTime(models.model)
    title=models.CharField(max_lengh=30,help_text='Escriba el nombre del cine online:')
    gender=models.CharField(max_lengh=30,help_text='Escriba el genero de la pelicula que desea ver:')
    name=models.CharField(max_lengh=30,help_text='Escriba el nombre del actor:')
    surname=models.CharField(max_lengh=30,help_text='Escriba el apellido del actor:')
    year=models.DateField(help_text='seleccione la fecha en que salio la pelicula:')
    time=models.TimeField(help_text='Escriba la duracion de la pelicula:')
    synopsis=models.CharField(max_lengh=2000,help_text='Sinopsis:')


class genero(models.Modelo):
    categories=(
        ('A','Accion')
        ('CF','Ciencia Ficcion')
        ('C','Comedia')
        ('R','Romance')
        ('T','Terror')
        ('S','Suspenso')
        ('CM','Cine Mexicano')
        ('F','Fantasia')
        ('M','Melodrama')
        ('A1','Animacion')
    )
