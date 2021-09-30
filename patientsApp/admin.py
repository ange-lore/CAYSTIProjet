from django.contrib import admin
from .models import Hopital, HopitalAdmin
from patientsApp.models import Utilisateur

# Register your models here.
admin.site.register(Hopital, HopitalAdmin)
admin.site.register(Utilisateur)