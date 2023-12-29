from django.db import models

# Create your models here.
class Persona(models.Model):
	nombre = models.CharField(max_length=30)
	edad = models.IntegerField()
	salario = models.DecimalField(decimal_places=2, max_digits=10)
		