from django.db import models

class Estacionamiento(models.Model):
    PrecioHora=models.FloatField(max_length=40)
    hora_ingreso=models.DateTimeField()
    hora_egreso=models.DateTimeField()

class Entrada(models.Model):
    vehiculo=models.CharField(max_length=40)
    patente=models.CharField(max_length=40)
    nombre=models.CharField(max_length=40)

class Salida(models.Model):
    vehiculo=models.CharField(max_length=40)
    patente=models.CharField(max_length=40)
    nombre=models.CharField(max_length=40)
