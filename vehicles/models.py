from django.db import models

# Create your models here.
from django.db import models
class Vehicle(models.Model):

    vehicle_name = models.CharField(max_length=100)

    vehicle_type = models.CharField(max_length=20)

    rent_per_day = models.IntegerField()

    available = models.BooleanField(default=True)

    def __str__(self):
        return self.vehicle_name