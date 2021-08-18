from django.forms import ModelForm
from .models import Patients

"""
creation de la classe PatientsApp qui permet d'afficher nos different champs dans notre formulaire
"""


class PatientsForm(ModelForm):
    class Meta:
        model = Patients
        fields = ['name', 'phone', 'email', 'address', 'sex', 'birth_date', 'password1', 'password2']
