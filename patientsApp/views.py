from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .formulaire import CreateUserForm

#from .formulaire import PatientsForm
from django.contrib.auth.decorators import login_required
from .models import Utilisateur
from django.contrib.auth.forms import UserCreationForm

"""
CODE POUR DEBUGER
import pdb; pdb.set_trace()"""

# from .models import Patients

# Create your views here.

"""
creation de fonction register_patient qui va nous permettre d'afficher notre formulaire de creation de compte patient 
"""
def register_patient(request):
    if request.user.is_authenticated:
        return redirect('reservation')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')


    #import pdb; pdb.set_trace()
    return render(request, 'login.html', )


def sign_in(request):
    print("TRUE")
    if request.method == 'POST':
        print("POST")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("IS NOT NONE")
            login(request, user)
            #return render(request, 'reservation.html') # redirect 'reservation'
            return redirect ('reservation')
        else:
            print("messages")
            messages.info(request, "il y'a une erreur dans le nom de l'utilisateur ou le mot de passe")

    return render(request, 'login.html')

