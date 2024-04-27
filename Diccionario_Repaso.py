
#***** REPASO***********

#   1. Diccionarios

diccionario = {
    "clave": 'valor', #esto es un elemento
    "clave_dos": 'valor', 
    "diccionario_anidado": {
        "clave": 'valor_dos'
    }
}
diccionario_dos = {
    "clave": 'valor', #esto es un elemento
    "clave_dos": 'valor', 
    "diccionario_anidado": {
        "clave": 'valor_dos'
    }
}
#Accedemos a un valor de un elemento de mi diccionario
print(diccionario["clave"])

#Modificamos el valor de un elemento de mi diccionario
diccionario["clave"] = "nuevo valor"
print(diccionario["clave"])

#Accedo a un valor de un diccionario anidado
print(diccionario["diccionario_anidado"]["clave"])

diccionario["diccionario_anidado"]["clave"] = 'nuevo valor dos'
print(diccionario["diccionario_anidado"]["clave"])

conjunto1 = {1, 2, 3}
conjunto2 = {1, 2, 3}
diccionarios = [diccionario_dos, diccionario]
lista_conjuntos = [conjunto1, conjunto2]

diccionario_listas = {
    "diccionarios" : diccionarios,
    "lista_dos" : lista_conjuntos, 
    "lista": [1, 2, 3]
}

#Método para añadir elemento a mi diccionario
diccionario["elemento_aniadido"] = "María"
print(diccionario)

diccionario["diccionario_anidado"]["nombre"] = "Paco"
print(diccionario)

diccionario.pop("elemento_aniadido")
print(diccionario)

diccionario["diccionario_anidado"].pop("nombre")
print(diccionario)


#   2. Clases

""" 
CLASE: Representación en mi programa de un objeto del mundo real (real o imaginario)que tiene AL MENOS una serie de características (atributos) y comportamientos (métodos).

Las clases en Python me van a permitir crear un modelo-molde-plantilla de ese objeto, y a partir de ese modelo-molde-plantilla crear copias-objetos(instancias) con las que trabajar en mi programa.

USUARIO = [pepe, juan, maría, bernarda, demetrio... x 100.000]

Quiero guardar --> nombre, telefono, dirección.

usuario = {
    'nombre': 'Pepe'
    'telefono': '666666666'
    'direccion': 'asdsadasdasd'
}
usuario = {
    'nombre': 'Pepe'
    'telefono': '666666666'
    'direccion': 'asdsadasdasd'
}
usuario = {
    'nombre': 'Pepe'
    'telefono': '666666666'
    'direccion': 'asdsadasdasd'
}
"""
class Usuario:
    #Atributos de clase: Su valor será el mismo para todas las instancias que se creen de esta clase
    especie = "ser humano"
    numero_total = 7000000
    #Atributo de instancia: sus valores serán diferentes para cada una de las instancias que se cree de esta clase
    def __init__(self, nombre, telefono, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        
    def hablar(self):
        print(f"{self.nombre} esta hablando")
    
    @classmethod
    def incremento(cls, incremento):
        Usuario.numero_total = Usuario.numero_total + incremento
        return f"Este año el nº de seres humanos se a incrementado y el total actual es: {Usuario.numero_total}"
    
    @classmethod
    def nadar(cls):
        return "Los usuarios nadan"


usuario_uno = Usuario("Pepe", 66666666, "sdfdsfdsfdsfsdf")
usuario_dos = Usuario("Juan", 66666666, "sdfdsfdsfdsfsdf")
usuario_tres = Usuario("María", 66666666, "sdfdsfdsfdsfsdf")
usuario_cuyat = Usuario("Bernarda", 66666666, "sdfdsfdsfdsfsdf")
usuario_cinco = Usuario("Demetrio", 66666666, "sdfdsfdsfdsfsdf")
print(f"El usuario que mejor me cae es {usuario_uno.nombre}. Este usuario es de la especie: {Usuario.especie}")


usuario_uno.hablar()
print(Usuario.incremento(3000))
print(Usuario.numero_total)
print(Usuario.nadar())







