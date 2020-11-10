from django.db import models

class Rublos(models.Model):
   id = models.AutoField(primary_key=True)
   flyer = models.ImageField(upload_to="rublos")

   class Meta:
      verbose_name = 'Flyer'
      verbose_name_plural = 'Flyers'

   def __str__(self):
      return self.flyer