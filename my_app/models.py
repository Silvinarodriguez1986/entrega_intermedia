from django.db import models

class Destino(models.Model):
   pais = models.CharField(max_length=20)
   poblacion = models.IntegerField() 

   def __str__(self):
       return f"{self.pais} | {self.poblacion}"

class Visa(models.Model):
       tipo = models.CharField(max_length=30)
       cantidad = models.IntegerField() 

       def __str__(self):
           return f"{self.tipo} | {self.cantidad}"

class Requisito(models.Model):
       estudio = models.CharField(max_length=30)
       edad = models.IntegerField() 

       def __str__(self):
           return f"{self.estudio} | {self.edad}"           

