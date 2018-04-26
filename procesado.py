#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Ejercicios de la Unidad 04: GIT Colaboracion
#
# Perpetrados por: Oscar Corres y Viloria

def sumaFactura(*args: Union[List, modelo.cliente]):
    totalFacturacion = 0
    for arg in args:
        if isinstance(arg, modelo.cliente):
            totalFacturacion += arg.facturacion
        else:
            for x in arg:
                totalFacturacion += sumaFactura(x)
    return totalFacturacion



def mediaFactura():