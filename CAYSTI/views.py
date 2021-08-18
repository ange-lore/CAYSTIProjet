# from django.http import HttpResponse
from django.shortcuts import render, redirect

# from django.urls import reverse
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


def home(request):
    if request.method == "POST":
        print("nous avons appuyé sur valider")
        numero_choix = int(request.POST.get("choix"))
        print(numero_choix )
        if numero_choix  == 1:
            print("inside")
            return redirect("afficher", choix=numero_choix )

        elif numero_choix  == 2:
            print("inside")
            return redirect("afficher", choix=numero_choix )
        elif numero_choix  == 3:
            print("inside")
            return redirect("afficher", choix=numero_choix )
        elif numero_choix == 4:
            print("inside")
            return redirect("afficher", choix=numero_choix )
        elif numero_choix  == 5:
            print("inside")
            return redirect("afficher", choix=numero_choix )
    return render(request, "home.html")


def about(request):
    return render(request, "page/about.html")


def afficher(request, choix):
    if choix == 1:
        print(choix)
        return render(request, "page/symptomes.html")
    elif choix == 2:
        print(choix)
        return render(request, "page/transmission.html")
    elif choix == 3:
        print(choix)
        return render(request, "page/geste_barriere.html")
    elif choix == 4:
        print(choix)
        return render(request, "page/prevention.html")
    elif choix==5:
        print(choix)
        return render(request, "page/vaccination.html")
    else:
            print("Oops!  That was no valid number.  Try again...")


'''MCV
Model: gere l'interaction avec la bd ou vas chercher dans la bd
View: afficharge presentation des information ou un peu comme le marketing
Controleur:le boss celui qui donne les directives'''
