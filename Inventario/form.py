from django.forms import ModelForm
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class Ingresar_producto(forms.ModelForm):

	class Meta:
		model =  producto
		fields = ('Nombre_producto','Precio_compra','Precio_venta','Existencia_minima','Existencia_actual','Estado')



class modificar_producto(forms.ModelForm):

	class Meta:
		model =  producto
		fields = ('Nombre_producto','Precio_compra','Precio_venta','Existencia_minima','Existencia_actual','Estado')

