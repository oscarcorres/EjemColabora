# -*- coding: utf-8 -*-

class cliente:
    #comentario
    def __init__(self, nombre, direccion, telf, email, facturacion_anual ):
        self.nombre = nombre
        self.direccion = direccion
        self.telf = telf
        self.email = email
        self.facturacion_anual = facturacion_anual



def crea(n):


    cliente1 = cliente("pepe", "direccion", "telf", "email", "facturacion_anual")
    cliente2 = cliente("pepe", "direccion", "telf", "email", "facturacion_anual")
    cliente3 = cliente("pepe", "direccion", "telf", "email", "facturacion_anual")
    cliente4 = cliente("pepe", "direccion", "telf", "email", "facturacion_anual")
    listaClientes = [cliente1, cliente2, cliente3, cliente4]

    return listaClientes