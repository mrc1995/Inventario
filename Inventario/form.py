from django.forms import ModelForm
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class Ingresar_producto(forms.ModelForm):

	class Meta:
		model =  producto
		fields = ('Nombre_producto','Precio_compra','Precio_venta','Existencia_minima','Existencia_actual','Estado')


class modificar_producto(forms.Form):
	Nombre_producto = forms.CharField(required = True)
	Precio_compra = forms.CharField(required = True)
	Precio_venta = forms.CharField(required = True)
	Existencia_minima = forms.CharField(required = True)
	Existencia_actual = forms.CharField(required = True)
	Estado= forms.CharField()

class loginForm(forms.Form):
	username = forms.CharField(max_length=25,required = True)
	password = forms.CharField(max_length=25,required = True)
