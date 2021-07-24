from django.db import models
from datetime import datetime

class Alumnos(models.Model):
    usuario = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    correo = models.EmailField()
    telefono = models.IntegerField(null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'




class Asignatura(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre}'

class Clase(models.Model):
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    seccion = models.CharField(max_length=4)
    hora = models.TimeField()
    dias = models.CharField(max_length=25)
    aula  = models.CharField(max_length=20)
    cupos = models.SmallIntegerField(default=10)

    def __str__(self):
        return f'{self.asignatura} | {self.seccion} '

class OfertaAcademica(models.Model):
    PERIODOS = (
        ('1', 'I PERIODO'), 
        ('2', 'II PERIODO'), 
        ('3', 'III PERIODO'), 
    )

    YEAR_CHOICES = [] #https://es.stackoverflow.com/questions/93320/usar-solo-el-a%C3%B1o-en-django-model-datefield
    for r in range(2017, (datetime.now().year+20)):
        YEAR_CHOICES.append((r,r))

    anio = models.IntegerField(choices=YEAR_CHOICES, default=datetime.now().year)
    periodo = models.CharField(max_length=1, choices=PERIODOS, default='1')
    clases = models.ManyToManyField(Clase, blank=True) #MtM no llevan on delete y el nulo no aplica
    estado = models.BooleanField(default=True)
