from django.forms import ModelForm
from .models import Utilisateur
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
"""
creation de la classe PatientsApp qui permet d'afficher nos different champs dans notre formulaire
"""
class CreateUserForm(UserCreationForm):
	class Meta:
		model = get_user_model()
		#fields = ['username', 'password1', 'password2']
		fields = ['username', 'email','phone', 'address', 'sex', 'birth_date', 'password1', 'password2']

