from django.shortcuts import render, redirect
from .models import Denuncia
from django.contrib.auth.decorators import login_required
# Create your views here.

def listar_denuncias(request):
    denuncias = Denuncia.objects.all()
    return render(request, 'denuncias/listar_denuncias.html', {'denuncias': denuncias})

@login_required
def crear_denuncia(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        imagen = request.FILES.get('imagen')
        categoria = request.POST.get('categoria')
        usuario = request.user
        denuncia = Denuncia(titulo=titulo, descripcion=descripcion, imagen=imagen, categoria=categoria, usuario=usuario)
        denuncia.save()
        return redirect('usuarios.index')
    else:
        return render(request, 'denuncias/crear_denuncia.html')
