#*************** DICCIONARIOS **********************
"""
Colecciones de datos que nos van a permitir almacenar elementos con formato "clave":valor.

    · Clave --> KEY, keys(): Siempre van entre comillas dobles, pueden ir también entre comillas simples, pero las reglas de estilo recomiendan dobles para las claves
    · Valor --> VALUE, values() :Siempre van entre comillas, pueden ir entre comillas dobles o simples, pero las reglas de estilo recomiendan simples para las claves
    · Elementos  --> Entries, items()

Características de los diccionarios:
    - Pueden ser anidados
    - Mantienen el orden de inserción
    - Son indexados: se accede a los valores a través de su clave.
    - Son mutables: Pueden añadir, eliminar o modificar los elementos.



diccionario_vacio = {} #creamos un diccionario vacio
#conjunto_vacio = set()
mi_primer_diccionario = {
    "Nombre": 'pepe',
    "Edad":  30,
    "Ciudad": "Málaga"
}
print(mi_primer_diccionario)

#Crear un diccionario con método constructor dict()
mi_segundo_diccionario = dict([ 
    ("Nombre","Juan"), #Utilizamos comas para separar las claves y el valor
    ("apellido","Rodríguez"), #utilizamos comas para separar cada uno de los elementos de nuestros diccionarios (pares clave,valor), los cuales incluímos entre paréntesis
    ("Edad", 12)
])
print(mi_segundo_diccionario)

#Crear un diccionario con método constructor dict() versión II:
mi_tercer_diccionario = dict(
    Nombre='paco el de las naranjas', #Las claves no utiliza comillas en esta versión
    Edad=45, #Para separar clave y valor utilizamos el símbolo =
    Ciudad="Madrid" #Se separan los elementos con comas
)
print(mi_tercer_diccionario)

#Los diccionarios pueden ser anidados
diccionario_anidado = {
    "clave": {
        "valor1": "dato1",
        "valor2": "dato2",
        "valor3": "dato3" #El último elemento de mi diccionario puede no incluir la coma
    },
    "clave2": "string1",
    "clave3": 36
}

#Accedo a los valores de un diccionario por clave en formato index
valor_nombre = mi_tercer_diccionario["Nombre"] 
print(valor_nombre)

#Accedo a los valores de un diccionario por clave con el método get() al cual le pasamos como parámetro la clave a la que quiero acceder.
valor_edad = mi_tercer_diccionario.get("Edad")
print("La edad de Paco el de las naranjas es:", valor_edad)

#Modificar un diccionario
diccionario_modificable = {
    "Nombre": "Pepa",
    "Edad": 50,
    "Ciudad": "Barcelona"
}
diccionario_modificable["Nombre"] = "María" 
#diccionario_modificable.get("Edad") = 23 --> SyntaxError porque get() directamente no me va a permitir cambiar el dato
diccionario_modificable["Carnet"] = True #Cuando accedo a un KEY que no existe, se añade automáticamente al diccionario
print(diccionario_modificable)
"""


#INCISO

valor_nombre = "hola xd"
#Modificar la cadena a capitalize()
nombre_capitalize = valor_nombre.capitalize()
print("Esto es un capitalize:",nombre_capitalize)

#Modificar la cadena a title()
nombre_title = valor_nombre.title()
print("Esto es un título:",nombre_title)





#Iterar un diccionario

