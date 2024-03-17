from django.db import models

from django.contrib.auth.forms import User


class VehicleFares(models.Model):
    VEHICLE_TYPES={
        1:"Auto",
        2:"Car",
        3:"Bike"
    }
    Id=models.AutoField(primary_key=True)
    vehicleType=models.IntegerField(choices=VEHICLE_TYPES)
    # modelName=models.TextField(max_length=50)
    distance=models.IntegerField()
    fare=models.FloatField()
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now_add=True)


class Normaluser(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)    
    email = models.EmailField(max_length=255, unique=True)
    phonenumber = models.CharField(max_length=20)
    address = models.TextField()
    displayname = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Driver(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)    
    email = models.EmailField(max_length=255, unique=True)
    phonenumber = models.CharField(max_length=20)
    address = models.TextField()
    displayname = models.CharField(max_length=255)
    vehicletype = models.CharField(max_length=255)
    licensenum = models.CharField(max_length=255)
    vehicleregnum = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username    
    
        
class Feedback(models.Model):
    Feedbackcomments =  models.CharField(max_length=255)
    starRating =  models.IntegerField()

class Booking(models.Model):
    user = models.ForeignKey(Normaluser, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=255)
    drop_location = models.CharField(max_length=255)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    driver_id = models.CharField(max_length=255)
    vehicletype = models.CharField(max_length=255)
    vehicleregnum = models.CharField(max_length=255)
    base_fare = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    total_fare = models.DecimalField(max_digits=10, decimal_places=2)
    booking_status = models.IntegerField() # 0- Ride Booked and waiting for rider to accept, 2- rider accepted ( Order summary page), 3- Ride completed, 4- Ride cancelled 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

