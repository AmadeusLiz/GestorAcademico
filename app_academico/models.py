from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.core.files.base import ContentFile


class Alumno(models.Model):
    FACULTAD = (
        ('1', 'Ingeniería en Ciencias de la Computación'),
        ('2', 'Ingeniería Industrial'),
        ('3', 'Ingeniería Civil'),
        ('4', 'Medicina y Cirugía'),
        ('5', 'Odontología'),
        ('6', 'Enfermería'),
        ('7', 'Psicología'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='alumno', null=True, blank=True)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    correo = models.EmailField()
    telefono = PhoneField(blank=True, help_text='Numero de teléfono')
    direccion = models.TextField(default="Dirección pendiente")
    fecha_nacimiento = models.DateField()
    facultad = models.CharField(max_length=1, choices=FACULTAD, default='1')



    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Asignatura(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(default="Descripción pendiente")
    creditos = models.IntegerField(default=3)

    def __str__(self):
        return f'{self.nombre}'


class Docente(models.Model):
    GENEROS = (
        ('1', 'Mujer'),
        ('2', 'Hombre'),
        ('3', 'Otro')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='docente', null=True, blank=True)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    telefono = PhoneField(blank=True, help_text='Numero de teléfono')
    correo = models.EmailField()
    direccion = models.TextField(default="Dirección pendiente")
    genero = models.CharField(max_length=1, choices=GENEROS, default='1')
    fecha_nacimiento = models.DateField()
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Clase(models.Model):
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    seccion = models.CharField(max_length=4)
    hora = models.TimeField()
    duracion = models.IntegerField(default=1)
    dias = models.CharField(max_length=25)
    aula = models.CharField(max_length=20)
    cupos = models.SmallIntegerField(default=10)
    room = models.URLField(null=True, blank=True)
    fecha_inicio = models.DateField(null=True)
    fecha_finalizacion = models.DateField(null=True)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, null=True, blank=True)
    alumnos = models.ManyToManyField(Alumno, blank=True, through='NotasClase')
    finalizada = models.BooleanField(default=False)

    @property
    def cupos_disponibles(self):
        matriculados = self.alumnos.count()
        return self.cupos - matriculados

    @property
    def hora_finalizacion(self):
        start = timedelta(hours=self.hora.hour, minutes=self.hora.minute)
        return start + timedelta(
            hours=self.duracion)  # https://www.lawebdelprogramador.com/foros/Python/1578062-Consulta-con-Suma-y-Resta-de-Horas.html

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

    class Meta:
        verbose_name_plural = 'Ofertas Academicas'


class NotasClase(models.Model):
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    parcial1 = models.IntegerField(null=True, default=0, blank=True)
    parcial2 = models.IntegerField(null=True, default=0, blank=True)
    parcial3 = models.IntegerField(null=True, default=0, blank=True)

    def __str__(self):
        return f'{self.alumno.nombre}'

    class Meta:
        verbose_name_plural = 'Notas Clases'
