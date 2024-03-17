"""
URL configuration for ride_share project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rs_auth import views
from rs_auth.views import signUpDriver, signUpNormalUser,UserFeedback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signin', views.signIn),
    path('api/GetFares',views.calculate_fare),
    path('api/Driver/create', signUpDriver, name='signUpDriver'),
    path('api/NormalUser/create', signUpNormalUser, name='signUpNormalUser'),
    path('api/Feedback/create', UserFeedback, name='UserFeedback'),
    path('api/bookRide', views.createBooking),
    path('api/bookingHistory', views.bookingHistory),
    path('api/sign-out', views.logOut),
]


