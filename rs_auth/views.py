import json
from django.shortcuts import render

from .models import Normaluser, Driver
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .form import login_form
from .serializer import DriverSerializer
from .serializer import NormalUserSerializer
from rest_framework import status

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.hashers import make_password,check_password



@api_view(['POST'])
def signIn(request):
  json_data = json.loads(request.body)
  email = json_data.get('email')
  password = json_data.get('password')
  type = json_data.get('type')

  if(type == 'driver'):
    try:
      user = Driver.objects.get(email=email)
    except Driver.DoesNotExist:
      return Response(data={'status':'error', 'message': 'Invalid EMail'}, status=401)
    if check_password(password, user.password):
      return Response(data={'message': 'Login successful'}, status=200)
    return Response(data={'status':'error', 'message':'Invalid username or password'}, status=400) 
  
  else:
    try:
      user = Normaluser.objects.get(email=email)
    except Normaluser.DoesNotExist:
      return Response(data={'status':'error', 'message': 'Invalid EMail'}, status=401)
    if check_password(password, user.password):
      return Response(data={'message': 'Login successful'}, status=200)
    return Response(data={'status':'error', 'message':'Invalid username or password'}, status=400) 


@api_view(['POST'])
def signUpDriver(request):
  serializer = DriverSerializer(data=request.data)
  if serializer.is_valid():
    driver_data = serializer.data
    password = driver_data.pop('password')
    hashed_password = make_password(password) 
    driver = Driver.objects.create(**driver_data, password=hashed_password)
    return Response(data={"status":"success", "message":"Driver Created Successfully"}, status=201)
  return Response(serializer.data, status=400)  

@api_view(['POST'])
def signUpNormalUser(request):
  serializer = NormalUserSerializer(data=request.data)
  if serializer.is_valid():
    user_data = serializer.data
    password = user_data.pop('password')
    hashed_password = make_password(password) 
    user = Normaluser.objects.create(**user_data, password=hashed_password)
    return Response(data={"status":"success", "message":"User Created Successfully"}, status=201)
  return Response(serializer.data, status=400)

@api_view(['GET'])
def GetFares(fareData):
  data={
    'distance':'1',
    'fare':'50'
  }
  return Response(data);