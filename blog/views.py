from django.shortcuts import render
# django.contrib import messages
#from .forms import *

from .bocks import Post


POSTS = [
        {"id": 1, "title": "First Post", "body": "this is my first post"},
        {"id": 2, "title": "Second Post", "body": "this is my Second post"},
        {"id": 3, "title": "Third Post", "body": "this is my Third post"},
    ]

# Create your views here.
def index(request):
    #posts= ["First Post", "Second Post", "Third Post"]
    #return render(request,"blog/index.html", {"posts": posts})
    #posts = Post.all()

    return render(request, "blog/index.html", {"posts": POSTS})

def show(request, id):
    post =Post.find(id, Post)
    return render(request, "blog/show.html", {"post": post})

'''def ajouter(request):
    form=PatientForm
    if request.method=='POST':
        patForm=PatientForm(request.POST)
        if patForm.is_valid():
            patForm.save()
            messages.success(request, 'data has been added')
            return redirect('/')
    return render(request, 'ajouter.html', {
        'form': form
    })



def doctor(request):
    form=DoctorForm()
    if request.method=='post':
        doctorForm=PatientForm(request.POST)
        if doctorForm.is_valide():
            doctorForm.save()'''
            #messages.success(request, 'Form has been added')
           # return redirect('/doctor')
    #return render(request, 'docteur.html', {'form':form})