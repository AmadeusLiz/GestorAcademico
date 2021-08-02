#from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse




# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('academico:index'))

        
    return render(request, 'seguridad/index.html')

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contrasena')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('academico:index'))
        else:
            messages.add_message(request, messages.ERROR, 'El usuario/contraseña inválidos o la cuenta está desactivada')
            return redirect('/')

        messages.add_message(request, messages.ERROR, 'El usuario no existe o esta desactivado')
        return redirect('/')
    else:
        return redirect('/')


def log_out(request):
    logout(request)
    return redirect('/')
