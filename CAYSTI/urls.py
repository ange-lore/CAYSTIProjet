"""CAYSTI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from patientsApp import views as patientsAppviews


urlpatterns = [
    path('blog/', include('blog.url')),
    path('admin/', admin.site.urls),
    path('', views.home),
    path('page/', views.vaccination, name='vaccination'),
    path('presentation/', views.presentation, name= 'presentation'),
    path('symptômes/', views.symptomes, name='symptomes'),
    path('transmission/', views.mode_transmission, name='mode_transmission'),
    path('gestes barrières/', views.geste_barrieres, name='gestes_barrieres'),
    path('preventions/', views.preventions, name='preventions'),
    path('vaccination/', views.vaccination, name='vaccination'),
    path('différents vaccins/', views.differents_vaccins, name='differents_vaccins'),
    path('statistique/', views.statistiques, name='statistiques'),
    path('reservation/', views.reservation, name='reservation'),
    path('page/', views.about, name="home"),
    path('patientsApp/', patientsAppviews.register_patient, name="sign_up"),
    path('login/', patientsAppviews.sign_in, name="login"),


]
