import json
from django.shortcuts import render

from .serializer import FeedbackSerializer
from .models import Normaluser, Driver,VehicleFares, Feedback, Booking
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .form import login_form
from .serializer import DriverSerializer,NormalUserSerializer,FareSerializer, BookingSerializer
from rest_framework import status
from rest_framework import generics

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.hashers import make_password,check_password

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



@api_view(['GET'])
def signIn(request):
  email = request.GET.get('email')
  password = request.GET.get('password')
  type = request.GET.get('userType')

  if(type == 'driver'):
    try:
      driver = Driver.objects.get(email=email)
    except Driver.DoesNotExist:
      return Response(data={'status':'error', 'message': 'Email Not Registered'}, status=401)
    if check_password(password, driver.password):
      driver_details = DriverSerializer(driver).data
      return Response(data={'status':'success', 'message': 'Login successful', 'driver':driver_details, 'login_allow':False}, status=200)
    return Response(data={'status':'error', 'message':'Invalid username or password'}, status=400) 
  
  else:
    try:
      user = Normaluser.objects.get(email=email)
    except Normaluser.DoesNotExist:
      return Response(data={'status':'error', 'message': 'Email Not Registered'}, status=401)
    if check_password(password, user.password):
      user_details = NormalUserSerializer(user).data
      return Response(data={'status':'success', 'message': 'Login successful', 'user': user_details, 'login_allow':True}, status=200)
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
  email_error = serializer.errors.get('email')
  if email_error:
    return Response(data={"status": "error", "message": email_error[0]}, status=400)
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
  email_error = serializer.errors.get('email')
  if email_error:
    return Response(data={"status": "error", "message": email_error[0]}, status=400)
  return Response(serializer.data, status=400)


@api_view(['Get'])
def calculate_fare(request):
  distance=request.query_params.get('distance')
  # return Response({'vehicle_fares':distance})
  if distance is not None:
    try:
      dist=float(request.query_params.get('distance'))
      vType=request.query_params.get('vehicleType')
      vehicle=VehicleFares.objects.get(vehicleType=vType)

      vehicle_fares={}
      base_fare=vehicle.fare
      tax=calculate_percentage(20,base_fare)
      total_fare= (base_fare+tax)*dist
      vehicle_fares={'vehicleType':vehicle.vehicleType,'totalfare':round(total_fare),'base_fare':base_fare,'tax':tax,"distance":dist}
  
      return Response(data={'status':'success', 'vehicleFares': vehicle_fares}, status=200)
    
    except ValueError:
      return Response(data={'status':'error', 'error': 'Error in executing '}, status=400)
  else:
      return Response(data={'status':'error', 'error': 'Distance is null'}, status=400)

@api_view(['POST'])
def UserFeedback(request):
  serializer = FeedbackSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=200)
  return Response(serializer.data, status=400)


def calculate_percentage(part,whole):
  if whole==0:
    return 0
  return (part/100)*whole


@api_view(['POST'])
def createBooking(request):
  serializer = BookingSerializer(data=request.data)
  try:
    if serializer.is_valid():
      serializer.save()
      return Response({'status':'success', 'booking_data':serializer.data}, status=200)
    else:
      return Response(serializer.errors, status=400)
  except Exception as e:
    return Response({"status":"error", "message": str(e)}, status=400)


@api_view(['GET'])
def bookingHistory(request):
    user_id = request.GET.get('user')
    if user_id is not None:
        try:
            bookings = Booking.objects.filter(user=user_id)
            serializer = BookingSerializer(bookings, many=True)
            return Response({'status': 'success', 'bookingHistory': serializer.data}, status=200)
        except Booking.DoesNotExist:
            return Response({'status': 'error', 'message': 'No bookings found for the user'}, status=404)
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=400)
    else:
        return Response({"status": "error", "message": "user_id parameter is missing"}, status=400)
  

@api_view(['POST'])
def logOut(request):
  logout(request)
  return Response({'message':'you are successfully logged out'},status=200)