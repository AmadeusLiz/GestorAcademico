from typing import AsyncIterable
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.urls import reverse
from .models import Clase, Asignatura, OfertaAcademica
from django.http import HttpResponse

def index(request):
    return render(request, 'academico/index.html')

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

#asignaturas
def asignaturas(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion= request.POST.get('descripcion')
        creditos = request.POST.get('creditos')
        
        c = Asignatura(nombre=nombre, descripcion=descripcion, creditos=creditos)
        c.save()

        messages.add_message(request, messages.INFO, f'La asignatura {nombre}  ha sido registrado con éxito')

    q = request.GET.get('q')

    if q:
        data = Asignatura.objects.filter(nombre__startswith=q).order_by('nombre')

        '''
            select * 
            from asignaturas
            where nombre like 'n%'
        '''
    else:
        data = Asignatura.objects.all().order_by('nombre')

    ctx = {
        'asignaturas': data,
        'q':q
    }

    return render(request, 'academico/asignaturas.html', ctx)



def eliminar_asignatura(request, id):
    Asignatura.objects.get(pk=id).delete()
    return redirect(reverse('asignaturas'))

def editar_asignatura(request, id):
    asig = get_object_or_404(Asignatura, pk=id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion= request.POST.get('descripcion')
        creditos = request.POST.get('creditos')

        #asig.nombre = nombre
        #asig.descripcion = descripcion
        #asig.creditos = creditos
        #asig.save()
        Asignatura.objects.filter(pk=id).update(nombre=nombre, descripcion=descripcion, creditos=creditos)

        messages.add_message(request, messages.INFO, f'La clase {nombre} se ha actualizado éxitosamente')

    data = Asignatura.objects.all().order_by('nombre')

    ctx = {
        'activo': 'asignaturas',
        'asignaturas': data,
        'c' : asig
    }

    return render(request, 'academico/asignaturas.html', ctx)
    