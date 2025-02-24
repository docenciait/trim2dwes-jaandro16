from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORIAS = [
    ('Alumbrado', 'Alumbrado'),
    ('BASURA', 'Basura'),
    ('Otros', 'Otros'),
]

class Denuncia(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to='denuncias/', blank=True, null=True)
    categoria = models.CharField(max_length=100, choices=CATEGORIAS)
    estado = models.CharField(max_length=50, default='Pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.titulo) + ' - ' + str(self.usuario)