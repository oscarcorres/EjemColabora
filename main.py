#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Ejercicios de la Unidad 03: Git Colaboracion
#
# Perpetrados por: Oscar Corres y Viloria

import modelo
import procesado

print('\n Creamos la lista de clientes')
clientes = modelo.crea(5)

print('\nProceso lista de clientes:')

print('\tTotal facturación: ', str(procesado.sumaFactura(clientes)))

print('\tMedia facturación: ', str(procesado.mediaFactura(clientes)))
