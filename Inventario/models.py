
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class producto(models.Model):
	#id_producto = models.CharField(primary_key=True, max_length=12, unique = True)
	Nombre_producto = models.CharField(max_length = 35, primary_key=True,unique=True)
	Precio_compra = models.CharField(max_length = 35)
	Precio_venta = models.CharField(max_length = 35)
	Existencia_minima = models.CharField(max_length = 35)
	Existencia_actual = models.CharField(max_length = 35)
	Estado = models.CharField(max_length = 35)
	Mult1 = models.CharField(max_length = 35)
	Mult2 = models.CharField(max_length = 35)