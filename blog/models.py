'''from django.db import models
class Patient(models.Model):
    name=models.CharField(max_length=200)
    telephone = models.IntegerField(max_length=200)
    email=models.CharField(max_length=200, null=True)
    adress=models.TextField(max_length=500, null=True)
    sexe = models.CharField(max_length=200, null=True)
    date_naissance = models.DateTimeField(max_length=200)


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    roll_no=models.CharField(max_length=300)
    email = models.CharField(max_length=200)
    adress = models.TextField(max_length=500)
    specialite = models.TextField(max_length=500)'''