from django.db import models


class Base(models.Model):
    nombre_base = models.CharField(max_length=20)
    ciudad_base = models.CharField(max_length=20)
    latitud_base = models.FloatField()
    longitud_base = models.FloatField()


class Piloto(models.Model):
    base = models.ForeignKey(Base, on_delete=models.PROTECT)
    codigo_piloto = models.CharField(max_length=20, unique=True)
    nombre_piloto = models.CharField(max_length=20)
    horas_vuelo_piloto = models.IntegerField()


class Avion(models.Model):
    base = models.ForeignKey(Base, on_delete=models.PROTECT)
    tipo_avion = models.CharField(max_length=20)
    codigo_avion = models.CharField(max_length=20)


class Miembro(models.Model):
    base = models.ForeignKey(Base, on_delete=models.PROTECT)
    codigo_miembro = models.CharField(max_length=20)
    nombre_miembro = models.CharField(max_length=20)


class Tripulacion(models.Model):
    miembro = models.ForeignKey(Miembro, on_delete=models.PROTECT)
    codigo_tripulacion = models.CharField(max_length=20)


class Vuelo(models.Model):
    piloto = models.ForeignKey(Piloto, on_delete=models.PROTECT)
    avion = models.ForeignKey(Avion, on_delete=models.PROTECT)
    tripulacion = models.ForeignKey(Tripulacion, on_delete=models.PROTECT)
    numero_vuelo = models.CharField(max_length=10)
    origen = models.CharField(max_length=20)
    destino = models.CharField(max_length=20)
    hora_vuelo = models.DateTimeField()
