from django.shortcuts import render, redirect
from .formulaire import PatientsForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Patients

"""
CODE POUR DEBUGER
import pdb; pdb.set_trace()"""

# from .models import Patients

# Create your views here.

"""creation de fonction register_patient qui va nous permettre d'afficher notre formulaire de creation de compte 
patient """


def register_patient(request):
    # declaration de la variable form
    form = PatientsForm()
    if request.method == "POST":
        # form=patientsAppForm(request.POST)
        form = PatientsForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
            phone = form.cleaned_data.get('phone')
            email= form.cleaned_data.get('email')
            address= form.cleaned_data.get('address')
            sex = form.cleaned_data.get('sex')
            birth_date = form.cleaned_data.get('birth_date ')
            password1= form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            patient1 = Patients(username,phone, email, address, sex, birth_date, password1, password2 )
            patient1.save()
            messages.success(request, "compte créer avec succés")
            return render(request, 'login.html')
        else:
            error="l'un est des champs est mal remplit"
            print(error)
            return render(request, 'register_patient.html',  {'form': form})
    else:
        form = PatientsForm()
        # form=patientForm()
    return render(request, 'register_patient.html', {'form': form})


"""
creation de fonction login qui va nous permettre d'afficher notre formulaire de creation de login
"""


def sign_in(request):
    print("TRUE")
    if request.method == 'POST':
        print("POST")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        p1 = Patients.objects.get(name=username, password1=password)
        print(p1)
        if p1 is not None:
            print("IS NOT NONE")
            login(request, user)
            return redirect('/acceuil',)
        else:
            print("error")
            error="il y'a une erreur dans le nom de l'utilisateur ou le mot de passe"
            messages.info(request, error )
    return render(request, 'login.html')
