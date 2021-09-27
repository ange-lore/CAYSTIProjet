#from django.forms import ModelForm
#from .models import Patients
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

"""
creation de la classe PatientsApp qui permet d'afficher nos different champs dans notre formulaire
"""
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

# class PatientsForm(ModelForm):
#     class Meta:
#         model = Patients
#         fields = ['name', 'phone', 'email', 'address', 'sex', 'birth_date', 'password1', 'password2']
