"""Dynamic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from core import views as core_views
from contacto import views as contacto_views
from trabajador import views as trabajador_views



urlpatterns = [
    path('',core_views.home,name="home"),
    path('nosotros/',core_views.nosotros,name="nosotros"),
    path('contacto/',contacto_views.Contacto ,name="contacto"),
    path('guardarsolicitud/',contacto_views.GuardarSolicitud,name="Guardar Solicitud"),
    path('login/', trabajador_views.login, name="login"),
    path('logear/',trabajador_views.logear,name="logear"),
    path('index/',trabajador_views.index,name="index"),
    path('solicitudes/',trabajador_views.solicitudes,name="solicitudes"),
    path('admin/', admin.site.urls),

  
    ]