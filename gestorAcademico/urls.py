"""gestorAcademico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_academico import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('clases_admin/', views.clases_admin, name='clasesAdmin'),
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
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

