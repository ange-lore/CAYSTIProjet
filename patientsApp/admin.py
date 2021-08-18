from django.contrib import admin
from .models import Patients, PatientsAdmin
admin.site.register(Patients, PatientsAdmin)
# Register your models here.
