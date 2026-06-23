from django.db import models

class Parroquia(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=10,
        choices=[('norte','Norte'), ('sur','Sur'), ('este','Este'), ('oeste','Oeste')])
    tipo = models.CharField(max_length=10,
        choices=[('urbana','Urbana'), ('rural','Rural')])

    def __str__(self):
        return self.nombre

class Barrio(models.Model):
    nombre = models.CharField(max_length=100)
    numero_viviendas = models.IntegerField(default=0)
    numero_parques = models.IntegerField(
        choices=[(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)], default=1)
    numero_edificios_residenciales = models.IntegerField(default=0)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class PresidenteBarrio(models.Model):
    cedula = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=50)
    edad = models.IntegerField(default=0)
    profesion = models.CharField(max_length=100)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.nickname, self.cedula)
