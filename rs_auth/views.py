from django.shortcuts import render

from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .form import login_form
from .serializer import DriverSerializer
from .serializer import NormalUserSerializer
from rest_framework import status

from django.contrib.auth import authenticate, login, logout

@api_view(['GET'])
def signIn(request):
  # form = login_form({"email":"ranjith@gmail.com", "password": "12345678", "confirmPassword": "12345678"})
  # print(form)

  email = "ranjith@gmail.com"
  password = "Ran@1234"

  user = authenticate(request, username = email, password= password)
  if(user is not None):
    login(request, user)
    return Response({"status":"success", "message": "Login Success"})
  else:
    return Response(status = 401,data={"status":"error", "message": "Login Failed"})

@api_view(['POST'])
def signUpDriver(request):
  serializer = DriverSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
  return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)  

@api_view(['POST'])
def signUpNormalUser(request):
  serializer = NormalUserSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
  return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)