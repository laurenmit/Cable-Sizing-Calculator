from django.db import models

# Create your models here.
class Cable(models.Model):
    cross_section = models.FloatField() # unit is [mm^2]
    insulation = models.CharField(max_length=5)
    conductor = models.CharField(max_length=15)
    voltage_rating = models.CharField(max_length=20) #rating of insulation [V]
    short_circuit_1s = models.FloatField() # unit is [kA]
    nom_current_rating = models.IntegerField() #unit is [A]
    impedance = models.FloatField()
