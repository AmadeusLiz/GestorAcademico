from typing import AsyncIterable
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.urls import reverse
from .models import Clase, Asignatura, OfertaAcademica, Alumnos
from django.http import HttpResponse


def alumnos(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        edad = request.POST.get('edad')

        Alumnos.objects.filter(pk=id).update(usuario=usuario, nombre=nombre, apellido=apellido, correo=correo, telefono=telefono, edad=edad)

        messages.add_message(request, messages.INFO, f'El alumno {alumno.nombre} se ha actualizado éxitosamente')

    alumnos = Alumnos.objects.all().order_by('nombre')
    
    ctx = {
        'activo': 'alumnos',
        'alumnos': alumnos
    }

    return render(request, 'academico/alumnos.html', ctx)


def editar_alumnos(request, id):
    if request.method=='POST':
        usuario = request.POST.get('usuario')
        nombre  = request.POST.get('nombre')
        apellido  = request.POST.get('apellido')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        edad = request.POST.get('edad')

        Alumnos.objects.filter(pk=id).update(usuario=usuario, nombre=nombre, apellido=apellido, correo=correo, telefono=telefono, edad=edad)

        messages.add_message(request, messages.INFO, f'El alumno {alumno.nombre} se ha actualizado éxitosamente')

        alumno = get_object_or_404(Alumnos, pk=id)
   
    
    ctx = {
        'activo': 'alumnos',
        'alumno': alumno
    }

    return render(request, 'academico/alumnos.html', ctx)


def clasesAdmin(request):
    asignaturas = Asignatura.objects.all().order_by('nombre')

    if request.method == 'POST':
        asignatura  = get_object_or_404(Asignatura, pk= request.POST.get('asignatura'))
        seccion  = request.POST.get('seccion')
        hora  = request.POST.get('hora')
        dias = request.POST.get('dias')
        aula = request.POST.get('aula')
        cupos = request.POST.get('cupos')

        Clase.objects.create(asignatura=asignatura, seccion=seccion, hora=hora, dias=dias, aula=aula, cupos=cupos)
        
        messages.add_message(request, messages.INFO, f'La clase {asignatura.nombre} ha sido agregada con éxito')

    q = request.GET.get('q')

    if q:
        clases = Clase.objects.filter(asignatura__nombre__contains=q).order_by('asignatura') #asignatura es unicamente un id, para acceder al nombre de la asignatura se usa doble guion bajo
    else: 
        clases = Clase.objects.all().order_by('asignatura')

    ctx = {
        'activo': 'clases',
        'clases': clases,
        'asignaturas': asignaturas,
        'q': q
    }

    return render(request, 'academico/clasesAdmin.html', ctx)

def editar_clase(request, id):
    if request.method=='POST':
        asignatura = get_object_or_404(Asignatura, pk=request.POST.get('asignatura'))
        seccion  = request.POST.get('seccion')
        hora  = request.POST.get('hora')
        dias = request.POST.get('dias')
        aula = request.POST.get('aula')
        cupos = request.POST.get('cupos')

        Clase.objects.filter(pk=id).update(asignatura=asignatura, seccion=seccion, hora=hora, dias=dias, aula=aula, cupos=cupos)

        messages.add_message(request, messages.INFO, f'La clase {asignatura.nombre} se ha actualizado éxitosamente')

    clase = get_object_or_404(Clase, pk=id)
    asignaturas = Asignatura.objects.all().order_by('nombre')
    clases = Clase.objects.all().order_by('asignatura')
    
    ctx = {
        'activo': 'clases',
        'clases': clases,
        'asignaturas': asignaturas,
        'c': clase
    }

    return render(request, 'academico/clasesAdmin.html', ctx)

def eliminar_clase(request, id):
    messages.add_message(request, messages.INFO, f'La clase se ha eliminado éxitosamente')
    Clase.objects.get(pk=id).delete()
    return redirect(reverse('clasesAdmin'))

def periodosAdmin(request):
    periodos = OfertaAcademica.objects.all().order_by('-anio','-periodo')

    ctx = {
        'activo': 'periodos',
        'periodos': periodos,
    }

    return render(request, 'academico/periodosAdmin.html', ctx)

def eliminar_periodo(request, id):
    messages.add_message(request, messages.INFO, f'El periodo se ha eliminado éxitosamente')
    OfertaAcademica.objects.get(pk=id).delete()
    return redirect(reverse('periodosAdmin'))

def editar_periodo(request, id):
    periodo = get_object_or_404(OfertaAcademica, pk=id)
    clases = Clase.objects.all().order_by('asignatura')
   
    if request.method == 'POST':
        anio = request.POST.get('anio')
        numperiodo = request.POST.get('numperiodo')
        estado = request.POST.get('estado')
        print(anio)
        periodo.anio = anio
        periodo.periodo = numperiodo

        if estado:
            periodo.estado = True
        else:
            periodo.estado = False
        
        for c in clases:
            chk = request.POST.get(f'chk-{c.id}') #almacenar id de clase
            if str(c.id) == chk: 
                #https://stackoverflow.com/questions/50015204/direct-assignment-to-the-forward-side-of-a-many-to-many-set-is-prohibited-use-e
                periodo.clases.add(c.id)
            else:
                #https://docs.djangoproject.com/en/2.2/topics/db/examples/many_to_many/
                periodo.clases.remove(c.id)
        
        periodo.save()
        messages.add_message(request, messages.INFO, f'La oferta académica ha sido actualizada con éxito')

    ctx = {
        'activo':'oferta',
        'clases': clases,
        'periodo': periodo,
        'ofertadas': periodo.clases.all()
    }

    return render(request, 'academico/ofertaAdmin.html', ctx)

def agregar_periodo(request):
    if request.method == 'POST':
        anio = request.POST.get('anio')
        periodo = request.POST.get('periodo')
        estado = request.POST.get('estado')

        if estado:
            estado = True
        else:
            estado = False

        OfertaAcademica.objects.create(anio=anio, periodo=periodo, estado=estado)
        
        messages.add_message(request, messages.INFO, f'El periodo académico ha sido añadido con éxito')

    return redirect(reverse('periodosAdmin'))
    