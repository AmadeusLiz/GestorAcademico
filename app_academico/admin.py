from django.contrib import admin
from .models import Clase, Asignatura, OfertaAcademica, Docente, NotasClase, Alumno

# Register your models here.

class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')

class ClaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'asignatura', 'seccion', 'hora', 'dias', 'aula', 'cupos')

class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'creditos')

class OfertaAdmin(admin.ModelAdmin):
    list_display = ('id', 'anio', 'periodo', 'estado')

class NotasClaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'clase', 'alumno', 'parcial1', 'parcial2', 'parcial3')

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'correo', 'fecha_nacimiento', 'fecha_contratacion')

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'correo', 'fecha_nacimiento')

admin.site.register(Clase, ClaseAdmin)
admin.site.register(Asignatura, AsignaturaAdmin)
admin.site.register(OfertaAcademica, OfertaAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(NotasClase, NotasClaseAdmin)
admin.site.register(Alumno, AlumnoAdmin)

