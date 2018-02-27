# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .form import *
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.

def Ingresarproducto(request):
	if request.method == "POST":
		form_registro_producto = Ingresar_producto(request.POST or None)
		if form_registro_producto.is_valid():
			newProducto = producto(Nombre_producto = request.POST['Nombre_producto'], Precio_compra =request.POST['Precio_compra'],
			Precio_venta=request.POST['Precio_venta'],Existencia_minima=request.POST['Existencia_minima'],Existencia_actual=request.POST['Existencia_actual'],
			Estado=request.POST['Estado'])
			newProducto.save()
	else:
		form_registro_producto = Ingresar_producto()
	return render(request,'RegistrarProducto.html',{'formulario':form_registro_producto})


#@login_required(login_url='/ingresar')
def modificar(request):
	context = {}
	if request.method == "POST":
		try:
			lproducto = producto.objects.get(Nombre_producto = request.POST.get('Nombre_producto'))
			context = {"lproducto": lproducto}
			form_modificar = modificar_producto(request.POST or None)
			print "aqui estoy"
			if form_modificar.is_valid():
				print "aqui despues del if"
				newProducto = producto(Nombre_producto = request.POST['Nombre_producto'], Precio_compra =request.POST['Precio_compra'],
				Precio_venta=request.POST['Precio_venta'],Existencia_minima=request.POST['Existencia_minima'],Existencia_actual=request.POST['Existencia_actual'],
				Estado=request.POST['Estado'])
				newProducto.save()
		except:
			return HttpResponseRedirect('no_existe')
	else:
		form_modificar = modificar_producto()

	return render(request,'modificar.html',context)


def no_existe(request):
	return render(request,'noexiste.html')