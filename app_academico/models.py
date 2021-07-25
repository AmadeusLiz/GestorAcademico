from django.db import models
from datetime import datetime
from phone_field import PhoneField


class Alumno(models.Model):
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
    descripcion = models.TextField(null=True, blank=True)
    creditos = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.nombre}'


class Alumno(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre}'


class Docente(models.Model):
    GENEROS = (
        ('1', 'Mujer'),
        ('2', 'Hombre'),
        ('3', 'Otro')
    )
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    telefono = PhoneField(blank=True, help_text='Numero de teléfono')
    correo = models.EmailField()
    genero = models.CharField(max_length=1, choices=GENEROS, default='1')
    fecha_nacimiento = models.DateField()
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


# class Matricula(models.Model):
#     alumno = 

class Clase(models.Model):
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    seccion = models.CharField(max_length=4)
    hora = models.TimeField()
    duracion = models.IntegerField(null=True, blank=True)
    dias = models.CharField(max_length=25)
    aula = models.CharField(max_length=20)
    cupos = models.SmallIntegerField(default=10)
    room = models.URLField(null=True)
    fecha_inicio = models.DateField(null=True)
    fecha_finalizacion = models.DateField(null=True)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, null=True, blank=True)
    alumnos = models.ManyToManyField(Alumno, blank=True)
    finalizada = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.asignatura} | {self.seccion} '


class OfertaAcademica(models.Model):
    PERIODOS = (
        ('1', 'I PERIODO'),
        ('2', 'II PERIODO'),
        ('3', 'III PERIODO'),
    )

    YEAR_CHOICES = []  # https://es.stackoverflow.com/questions/93320/usar-solo-el-a%C3%B1o-en-django-model-datefield
    for r in range(2017, (datetime.now().year + 20)):
        YEAR_CHOICES.append((r, r))

    anio = models.IntegerField(choices=YEAR_CHOICES, default=datetime.now().year)
    periodo = models.CharField(max_length=1, choices=PERIODOS, default='1')
    clases = models.ManyToManyField(Clase, blank=True)  # MtM no llevan on delete y el nulo no aplica
    estado = models.BooleanField(default=True)


class NotasClase(models.Model):
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    parcial1 = models.IntegerField(null=True, default=0, blank=True)
    parcial2 = models.IntegerField(null=True, default=0, blank=True)
    parcial3 = models.IntegerField(null=True, default=0, blank=True)

    def __str__(self):
        return f'{self.clase.asignatura} {self.alumno.nombre}'
