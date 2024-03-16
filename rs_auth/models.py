from django.db import models

from django.contrib.auth.forms import User

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


