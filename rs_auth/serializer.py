from rest_framework import serializers
from .models import Driver,Normaluser

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model= Driver       
        fields = '__all__'

class NormalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= Normaluser       
        fields = '__all__'