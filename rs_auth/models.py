from django.db import models

from django.contrib.auth.forms import User


class VehicleFare(models.Model):
    VEHICLE_TYPES={
        1:"Auto",
        2:"Car",
        3:"Bike"
    }
    Id=models.AutoField(primary_key=True)
    vehicleType=models.IntegerField( choices=VEHICLE_TYPES)
    modelName=models.TextField(max_length=50)
    distance=models.IntegerField()
    fare=models.FloatField()
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now_add=True)


class Normaluser(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)    
    email = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    displayname = models.CharField(max_length=255)

class Driver(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)    
    email = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    displayname = models.CharField(max_length=255)    
    licensenum = models.CharField(max_length=255)
    vehicleregnum = models.CharField(max_length=255)




