from tabnanny import verbose
from django.db import models

# Create your models here.

class Project(models.Model):
    ruc = models.CharField(max_length=200)
    representante = models.CharField(max_length=200)
    razonsocial = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    descripcion = models.TextField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "solicitud"
        verbose_name_plural = "Solicitudes"
        ordering = ["-created"]
    
    def __str__(self):
        return self.razonsocial 