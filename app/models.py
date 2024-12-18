from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

class Curso(models.Model):
   nombre = models.CharField(max_length=100)
   codigo = models.CharField(max_length=10, unique=True)
   fecha_inicio = models.DateField()
   fecha_fin = models.DateField()

   def clean(self):
      if self.fecha_inicio >= self.fecha_fin:
         raise ValidationError("La fecha de inicio debe ser anterior a la fecha de finalización")

   def __str__(self):
      return f"Nombre: {self.nombre} ({self.codigo})"

class Estudiante(models.Model):
   nombre = models.CharField(max_length=100)
   email = models.EmailField(unique=True)
   fecha_nacimiento = models.DateField()

   def clean(self):
      if self.fecha_nacimiento > timezone.now().date():
         raise ValidationError("La fecha de nacimiento no puede ser posterior al día actual")
      
      edad_minima = 18
      if self.fecha_nacimiento > timezone.now().date() - timedelta(days=edad_minima * 365):
            raise ValidationError("El estudiante debe tener al menos 18 años")
        
   def __str__(self):
        return f"Nombre: {self.nombre} ({self.email})"

class Inscripcion(models.Model):
   estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE, related_name='inscripciones')
   curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='inscripciones')
   fecha_inscripcion = models.DateField()

   class Meta:
        unique_together = ('estudiante', 'curso')

   def clean(self):
      if self.curso.fecha_fin < timezone.now().date():
         raise ValidationError("No se puede inscribir a un curso que ya ha finalizado")
        
      if self.fecha_inscripcion > timezone.now().date():
         raise ValidationError("La fecha de inscripción no puede ser posterior al día actual")

   def __str__(self):
      return f"{self.estudiante} - {self.curso}"
   