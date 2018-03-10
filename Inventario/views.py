# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .form import *
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login, authenticate, logout
# Create your views here.
#admininventario
#inventario12345

def Ingresarproducto(request):
	if request.method == "POST":
		form_registro_producto = Ingresar_producto(request.POST or None)
		if form_registro_producto.is_valid():
			newProducto = producto(Nombre_producto = request.POST['Nombre_producto'], Precio_compra =request.POST['Precio_compra'],
			Precio_venta=request.POST['Precio_venta'],Existencia_minima=request.POST['Existencia_minima'],Existencia_actual=request.POST['Existencia_actual'],
			Estado=request.POST['Estado'], Mult1 = request.POST['Mult1'], Mult2 = request.POST['Mult2'])
			newProducto.save()
	else:
		form_registro_producto = Ingresar_producto()
	return render(request,'RegistrarProducto.html',{'formulario':form_registro_producto})


#@login_required(login_url='/ingresar')
def modificarproducto(request):
	context = {}
	if request.method == "POST":
		try:
			lproducto = producto.objects.get(Nombre_producto = request.POST.get('Nombre_producto'))
			context = {"lproducto": lproducto}
			form_modificar = modificar_producto(request.POST or None)
			#print "aqui estoy"
			if form_modificar.is_valid():
			#	print "aqui despues del if"
				newProducto = producto(Nombre_producto = request.POST['Nombre_producto'], Precio_compra =request.POST['Precio_compra'],
				Precio_venta=request.POST['Precio_venta'],Existencia_minima=request.POST['Existencia_minima'],Existencia_actual=request.POST['Existencia_actual'],
				Estado=request.POST['Estado'], Mult1 = request.POST['Mult1'], Mult2 = request.POST['Mult2'])
				newProducto.save()
		except:
			return HttpResponseRedirect('no_existe')
	else:
		form_modificar = modificar_producto()

	return render(request,'modificar.html',context)


def no_existe(request):
	return render(request,'noexiste.html')


def loginstart(request):
	form = loginForm(request.POST or None)
	if form.is_valid():
		data = form.cleaned_data
		username= data.get("username")
		password = data.get("password")
		acceso = authenticate(username = username,password = password)
		if acceso is not None:
			if acceso.is_active:
				login(request,acceso)
				return HttpResponseRedirect('/privado')
				#return HttpResponse("Bienvenido {}".format(username))
			else:
				return render(request,'noactivo.html')
		else:
			return render(request,'nousuario.html')
	else:
	 	form = loginForm()
	return render(request, 'login.html')

#@login_required(login_url='/ingresar')
def privado(request):
	username = request.user
	return render(request,'base.html')
	

#@login_required(login_url='/ingresar')
def endsesion(request):
	logout(request)
	return HttpResponseRedirect('/loginstart')

#@login_required(login_url='/ingresar')
def cabecera(request):
	username = request.user
	return render(request,'cabecera.html')

#@login_required(login_url='/ingresar')
def contenido(request):
	username = request.user
	return render(request,'contenido.html')

def desplegar(request):
	context = {}
	if request.method == "POST":
		ver_producto = producto.objects.all()
		context = {"ver_producto":ver_producto}
	return render (request, 'ver.html',context)