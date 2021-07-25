from django.contrib import admin
from .models import Clase, Asignatura, OfertaAcademica, Alumno

# Register your models here.
class ClaseAdmin(admin.ModelAdmin):
    list_display = ('id','asignatura', 'seccion', 'hora', 'dias', 'aula', 'cupos')

class OfertaAdmin(admin.ModelAdmin):
    list_display = ('id','anio', 'periodo', 'estado')

admin.site.register(Clase, ClaseAdmin)
admin.site.register(Asignatura)
admin.site.register(OfertaAcademica, OfertaAdmin)
admin.site.register(Alumno)