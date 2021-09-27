from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

'''definition des differents choix du sexe
... sex_choice=
        dictionnaire des differents choix de sexe.
'''


sex_choice = {
    ('FEMININ', 'feminin'),
    ('MASCULIN', 'masculin'),
}
'''
creation de notre model
creation de la classe Patients pour creer notre model
'''


class Utilisateur(models.Model):
    user = models.ForeignKey(User,
                             related_name="%(app_label)s_%(class)s_patient_id",
                             on_delete=models.CASCADE,
                             default=1)

    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=500, default="")
    sex = models.CharField(max_length=200, default="", choices=sex_choice)
    birth_date = models.DateField()
    password1 = models.CharField(max_length=200, default="", null=False, blank=False)
    password2 = models.CharField(max_length=200, default="", null=False, blank=False)


# Create your models here.
class PatientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address', 'sex', 'birth_date', 'password1', 'password2')
    list_filter = ('name',)
    search_fields = ['name', 'email']

class Hopital(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=30, decimal_places=20)
    longitude = models.DecimalField(max_digits=30, decimal_places=20)

class HopitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    list_filter = ('name',)
    search_fields = ['name', 'address']

"""class Reservation(models.Model):
    hospital = models.CharField(max_length=200)
    reservation_date = models.CharField(max_length=200)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('hospital', 'reservation_date')
    list_filter = ('hospital',)
    search_fields = ['hospital', 'reservation_date']"""