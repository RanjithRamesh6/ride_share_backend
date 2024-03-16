from django.db import models

from django.contrib.auth.forms import User

class Normaluser(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)    
    email = models.EmailField(max_length=255)
    phonenumber = models.CharField(max_length=20)
    address = models.TextField()
    displayname = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Driver(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)    
    email = models.EmailField(max_length=255)
    phonenumber = models.CharField(max_length=20)
    address = models.TextField()
    displayname = models.CharField(max_length=255)
    licensenum = models.CharField(max_length=255)
    vehicleregnum = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username    


