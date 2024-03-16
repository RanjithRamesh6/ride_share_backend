from django.db import models

from django.contrib.auth.forms import User



class VehicleFare(models.Model):
    VEHICLE_TYPES={
        1:"Auto",
        2:"Car",
        3:"Bike"
    }
    Id=models.AutoField(primary_key=True)
    vehicleType=models.IntegerField(max_length=1, choices=VEHICLE_TYPES)
    vehicleName=models.TextField(max_length=50)
    distance=models.IntegerField()
    fare=models.FloatField()
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now_add=True)
