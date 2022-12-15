from django.shortcuts import redirect, render
from contacto.models import Project

# Create your views here.

def login(request):
    return render(request, "trabajador/login.html")

def logear(request):
    e_username=request.POST['username']
    e_password=request.POST['password']
    if e_username == 'jhor' :
        if e_password == "jhor" : 
            return redirect('/index/')
        else :
            return redirect('/login/')
    else:
        return redirect('/login/')

def index(request):
    return render(request, "trabajador/index.html")

def solicitudes(request):
    projects = Project.objects.all()
    return render(request, "trabajador/solicitudes.html",
    {'projects':projects})

def EliminarVisita(request):
    projects = Project.objects.all()
    return render(request, "/eliminarVisita/",
    {'projects':projects})