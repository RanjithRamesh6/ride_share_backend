from rest_framework import serializers
from .models import Driver,Normaluser,VehicleFares,Feedback

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model= Driver       
        fields = '__all__'
        #exclude = ('password',)

class NormalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= Normaluser       
        fields = '__all__'
        #exclude = ('password',)
    
class FareSerializer(serializers.ModelSerializer):
    class Meta:
        model= VehicleFares     
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model= Feedback       
        fields = '__all__'
