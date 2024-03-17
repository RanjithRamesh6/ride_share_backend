from rest_framework import serializers
from .models import Driver,Normaluser,VehicleFares

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model= Driver       
        # fields = '__all__'
        exclude = ('password',)

class NormalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= Normaluser       
        # fields = '__all__'
        exclude = ('password',)

    
class FareSerializer(serializers.ModelSerializer):
    class Meta:
        model= VehicleFares     
        fields = '__all__'
