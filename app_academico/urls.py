
from django.urls import path
from app_academico import views
app_name = 'academico'


urlpatterns = [
    ########
    path('', views.index, name='index'),
    path('alumnos_admin/', views.alumnos, name="alumnos"),
    path('alumnos_admin/<int:id>/editar/', views.editar_alumnos, name='editar_alumnos'),
    path('alumnos_admin/<int:id>/eliminar/', views.eliminar_alumnos, name='eliminar_alumnos'),
    path('clases_admin/', views.clasesAdmin, name='clasesAdmin'),
    path('clases_admin/<int:id>/eliminar/', views.eliminar_clase, name='eliminar_clase'),
    path('clases_admin/<int:id>/editar/', views.editar_clase, name='editar_clase'),
    path('periodos_admin/', views.periodos_admin, name='periodosAdmin'),
    path('periodos_admin/<int:id>/eliminar/', views.eliminar_periodo, name='eliminar_periodo'),
    path('periodos_admin/<int:id>/editar/', views.editar_periodo, name='editar_periodo'),
    path('periodo_agregar/', views.agregar_periodo, name='agregar_periodo'),
    path('asignaturas/', views.asignaturas, name="asignaturas"),
    path('asignaturas/<int:id>/eliminar/', views.eliminar_asignatura, name="eliminar_asignatura"),
    path('asignaturas/<int:id>/editar/', views.editar_asignatura, name="editar_asignatura"),
    path('docentes_admin/', views.docente_admin, name='docenteAdmin'),
    path('docentes_admin/<int:id>/eliminar/', views.eliminar_docente, name='eliminar_docente'),
    path('docentes_admin/<int:id>/editar/', views.editar_docente, name='editar_docente'),
    path('notas/', views.notas, name="notas"),
    path('notas/<int:id>/editar', views.editar_nota, name="editar_nota"),
    path('oferta/', views.ofertaAlumno, name='ofertaAlumno'),
    path('boleta_alumno/', views.boletaAlumno, name='boletaAlumno'),
    path('perfilAlumno/', views.editar_perfil_alumnos, name='editar_perfil_alumnos'),
    path('clasesdocente/', views.clasesdocente, name='clasesdocente'),
    path('clases_matriculadas/', views.clasesMatricula, name='clasesMatricula'),

] 