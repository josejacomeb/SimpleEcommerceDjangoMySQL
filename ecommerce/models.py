from django.db import models

# Create your models here.

"""
Clase para describir los atributos que tiene una TV en el Ecommerce
"""
class Televisores(models.Model):
    # Descripcion como LG  Smart TV 4K, 32 Pulgadas, 
    descripcion=models.CharField(max_length=400) 
    # Marcas comerciales como LG, Samsung
    marca = models.CharField(max_length=150)
    # Modelo como por Ejemplo 75UR7800PSB 
    modelo = models.CharField(max_length=150)
    # Resolución en pixeles
    resolucion = models.IntegerField()
    
"""
Clase para describir los atributos que tiene una Celular en el Ecommerce
"""
class TelefonoCelular(models.Model):
    descripcion=models.CharField(max_length=400) # Descripcion como LG  Smart TV 4K, 32 Pulgadas, 
    # Marcas comerciales como LG, Samsung
    marca = models.CharField(max_length=150)
    # Modelo como por Ejemplo 75UR7800PSB 
    modelo = models.CharField(max_length=150)
    # Como A16 Bionic en iPhone o Snapdragon 8 Gen 1 
    procesador = models.CharField(max_length=150)

"""
Clase para describir los atributos que tiene una Portatil en el Ecommerce
"""
class Laptop(models.Model):
    descripcion=models.CharField(max_length=400) # Descripcion como LG  Smart TV 4K, 32 Pulgadas, 
    # Marcas comerciales como LG, Samsung
    marca = models.CharField(max_length=150)
    # Modelo como por Ejemplo 75UR7800PSB 
    modelo = models.CharField(max_length=150)
    # Como Core i7 para Intel o Ryzen en AMD 
    procesador = models.CharField(max_length=150)
    # Tamaño pantalla como 17 pulgadas
    tamano_pantalla = models.IntegerField()
    
    
