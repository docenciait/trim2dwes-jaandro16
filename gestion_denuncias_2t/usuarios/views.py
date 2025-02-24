from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import CustomUserCreationForm, CustomErrorList
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
 
@login_required
def cerrar_sesion(request):
    auth_logout(request)
    return redirect('usuarios.index')

def index(request):
    return render(request, 'usuarios/index.html')

def iniciar_sesion(request):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'usuarios/login.html', {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            template_data['error'] = 'Invalid username or password'
            return render(request, 'usuarios/login.html', {'template_data': template_data})
        else:
            auth_login(request, user)
            return redirect('usuarios.index')

def registro(request):
    template_data = {}
    template_data['title'] = 'Sign up'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'usuarios/registro.html', {'template_data': template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('usuarios.login')
        else:
            template_data['form'] = form
            return render(request, 'usuarios/registro.html', {'template_data': template_data})