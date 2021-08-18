from django.db import models
from django.contrib import admin
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


class Patients(models.Model):
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
