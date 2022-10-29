from django.db import models 

class Destino(models.Model):
   pais = models.CharField(max_length=20)
   poblacion = models.IntegerField() 

   def __str__(self):
       return f"{self.pais} | {self.poblacion}"

class Visa(models.Model):
       tipo = models.CharField(max_length=30)
       costo = models.IntegerField()

       def __str__(self):
           return f"{self.tipo} | {self.costo}"

        

class Requisito(models.Model):
       visa =  models.CharField(max_length=30)
       estudio = models.CharField(max_length=30)
       edad = models.IntegerField()

       def __str__(self): 
           return f"{self.visa} | {self.estudio} | {self.edad}"   
