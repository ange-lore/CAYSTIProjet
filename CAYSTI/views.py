from django.http import HttpResponse
import requests
from django.shortcuts import render, redirect,get_object_or_404
from patientsApp.models import Hopital
from geopy.geocoders import Nominatim
#from patientsApp.models import Patients
#from django.urls import reverse
'''from geopy.geocoders import Nominatim
import time
from pprint import pprint

# instantiate a new Nominatim client
app = Nominatim(user_agent="tutorial")

# get location raw data
location = app.geocode("bastos, Cameroun").raw
# print raw data
pprint(location)

def get_location_by_address(address):
    """This function returns a location as raw from an address
    will repeat until success"""
    time.sleep(1)
    try:
        return app.geocode(address).raw
    except:
        return get_location_by_address(address)

address = "Bastos, Awae, Ekounoue, Happy"
location = get_location_by_address(address)
latitude = location["lat"]
longitude = location["lon"]
print(f"{latitude}, {longitude}")
# print all returned data
pprint(location)

def get_address_by_location(latitude, longitude, language="en"):
    """This function returns an address as raw from a location
    will repeat until success"""
    # build coordinates string to pass to reverse() function
    coordinates = f"{latitude}, {longitude}"
    # sleep for a second to respect Usage Policy
    time.sleep(1)
    try:
        return app.reverse(coordinates, language=language).raw
    except:
        return get_address_by_location(latitude, longitude)

# define your coordinates
latitude = 5.99996
longitude = 12.00005
# get the address info
address = get_address_by_location(latitude, longitude)
# print all returned data
pprint(address)'''

'''def home(request, methods=['GET','POST']):
    #return HttpResponse("hello world")
    if request.methods == "POST":
        pass
    return render(request, 'home.html')'''
def vaccination(request):
    return render(request, 'vaccination.html')
def reservation(request):
    hospital = Hopital.objects.all()
    # get user id from request.user.id
    # filter from patient model with user id
    # Patient.objects.get(pk=id)

    if not request.user.id:
        return render(request, 'login.html')
    return render(request, 'reservation.html', {"hospitals": hospital})


    #import pdb;pdb.set_trace()
   # geolocator = Nominatim(user_agent="caysti")
   # location = geolocator.geocode("bastos")
    #import pdb;pdb.set_trace()


def presentation(request):
    return render(request, 'presentation.html')
def symptomes(request):
    return render(request, 'symptome.html')
def mode_transmission(request):
    return render(request, 'transmission.html')
def geste_barrieres(request):
    return render(request, 'geste_barriere.html')
def preventions(request):
    return render(request, 'prevention.html')
def differents_vaccins(request):
    return render(request, 'differents_vaccins.html')
def statistiques(request):
    return render(request, 'statistique.html')





def home(request):
    if request.method == "POST":
        print("nous avons appuyé sur valider")
        numero_choix = int(request.POST.get("choix"))
        print(numero_choix )
        if numero_choix  == 1:
            print("inside")
            return render(request, "home.html", {"cle": numero_choix})

        elif numero_choix  == 2:
            print("inside")
            return render(request, "home.html", {"cle": numero_choix})
        elif numero_choix  == 3:
            print("inside")
            return render(request, "home.html", {"cle": numero_choix})
        elif numero_choix == 4:
            print("inside")
            return render(request, "home.html", {"cle": numero_choix})
        elif numero_choix  == 5:
            print("inside")
            return redirect("afficher", choix=numero_choix)
        elif numero_choix == 6:
            return render(request, "home.html", {"cle": numero_choix})
        elif numero_choix == 7:
            return render(request, "home.html", {"cle": numero_choix})
        elif numero_choix == 8:
            print("inside")
            return redirect("afficher", choix=numero_choix)
        elif numero_choix == 9:
            return render(request, "home.html", {"cle": numero_choix})
    numero_choix=0
    return render(request, "home.html", {"cle": numero_choix})


def about(request):
    return render(request, "page/about.html")


