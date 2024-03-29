from django.db import models

# Create your models here.


class Proveedor(models.Model):
    nit = models.IntegerField(primary_key=True, null=False, blank=False, verbose_name='Nit')
    nombre = models.CharField(null=False, blank=False, max_length=100, verbose_name='Nombre')
    direccion = models.CharField(null=False, blank=False, max_length=100, verbose_name='Dierccion')
    correo = models.CharField(null=False, blank=False, max_length=100, verbose_name='Correo')
    numero = models.IntegerField(null=False, blank=False, verbose_name='Numero de contacto')

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'