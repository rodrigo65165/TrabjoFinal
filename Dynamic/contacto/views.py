from django.shortcuts import render,redirect,HttpResponse
from .models import Project
from django.contrib import messages
# Create your views here.

def Contacto(request):
    return render(request, "contacto/contacto.html" )

def GuardarSolicitud(request):
    e_ruc=request.POST['ruc']
    e_representante=request.POST['representante']
    e_razonsocial=request.POST['razonsocial']
    e_mail=request.POST['email']
    e_fono=request.POST['fono']
    e_descripcion=request.POST['txtdesc']
    solicitud = Project.objects.create(ruc=e_ruc, representante=e_representante, razonsocial=e_razonsocial, correo=e_mail, telefono=e_fono,descripcion=e_descripcion)
    return redirect('/contacto/')    

def my_view(request):
  messages.add_message(request, messages.INFO, 'Solicitud Enviada')
  return render(request, 'my_template.html')