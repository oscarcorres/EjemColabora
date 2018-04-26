#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Ejercicios de la Unidad 04: GIT Colaboracion
#
# Perpetrados por: Oscar Corres y Viloria

def sumaFactura(listaClientes = []):
    totalFacturacion = 0
    for cliente in listaClientes:
            totalFacturacion += cliente.facturacion_anual
    return totalFacturacion

def mediaFactura(listaClientes = []):
    return sumaFactura(listaClientes)/len(listaClientes)