from django.db import models

class Afiliados(models.Model):
   id = models.AutoField(primary_key=True)
   nombre = models.CharField(max_length=120, blank=False)
   apellidos = models.CharField(max_length=120, blank=False)
   pais = models.CharField(max_length=120, blank=False)
   ciudad = models.CharField(max_length=120, blank=False)
   documento = models.CharField(max_length=20, blank=False)
   celular = models.CharField(max_length=20, blank=False)

   email = models.CharField(max_length=120, blank=False, verbose_name='Email')
   

   def __str__(self):
      return self.nombre

   class Meta:
      ordering = ['nombre']
      verbose_name = 'nombre'
      verbose_name_plural = 'nombres'

