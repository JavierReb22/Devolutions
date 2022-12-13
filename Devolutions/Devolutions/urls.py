"""Devolutions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from Devolu.views import menu, crearVend, registrar,registrarse,listadev,registrard,registrardevo,eliminardev,devoluActualizar,editarDev,listaclient,registrarc,registrarclient,eliminarClient,clientActualizar,editarClient,listaproduct,registrarp,registrarproduct,eliminarProduct,editarProduct,productActualizar
urlpatterns = [
    path('inicio/', include('django.contrib.auth.urls')),
    path('registrarse/', registrarse),
    path('admin/', admin.site.urls),
    path('lista/',listadev),
    path('registrodev/', registrard),
    path('registrardevolucio/', registrardevo),
    path('eliminarDev/<int:id>',eliminardev),
    path('actualizarDev/<int:id>', devoluActualizar),
    path('editardevo/', editarDev),
    path('registrar/', registrar),
    path('menu/',menu),
    path('crearuser/', crearVend),
    path('listaClient/',listaclient),
    path('registrocli/',registrarc),
    path('registrarcliente/',registrarclient),
    path('eliminarcliente/<int:id>',eliminarClient),
    path('actualizarclient/<int:id>',clientActualizar),
    path('editarcliente/',editarClient),
    path('listarproduct/',listaproduct),
    path('registrarprod/',registrarp),
    path('registrarproducto/',registrarproduct),
    path('eliminarproduct/<int:id>',eliminarProduct),
    path('actualizarproduct/<int:id>',productActualizar),
    path('editarproducto/',editarProduct)
]