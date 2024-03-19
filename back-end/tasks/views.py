from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError


# Create your views here.


def home(request):
    return render(request, 'home.html')

def signUp(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Registro de usuario
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario (' + request.POST['username'] + ') ya existe.'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas ingresadas no coinciden.'
        })

def tasks (request):
    return render(request, 'tasks.html')