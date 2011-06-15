# coding: utf-8
from django.db import models

VEHICLE_TYPES = (
        ('Caminhao', u'Caminhão'),
        ('Carro', u'Carro'),
        ('Moto', u'Moto'),
        ('Onibus', u'Onibus'),
        ('SUV', u'SUV / Jipe'),
        ('Van', u'Van'),
    )

class Offence(models.Model):
    license_plate = models.CharField(u"Placa do veículo", max_length=8)
    media_url = models.URLField(u"Endereço da foto ou video")
    vehicle_type = models.CharField(u"Tipo de veículo", max_length=10, choices=VEHICLE_TYPES)
    email = models.EmailField(u"Seu e-mail", null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True) # (lat.itude, lon.gitude)
