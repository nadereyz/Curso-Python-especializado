# COLECCIONES DE DATOS: TUPLAS ***************************
"""Tipo de estructura de datos que nos permite almacenar datos y que además son INMUTABLES, lo que las hace más rápidas a la hora de acceder a ellas"""
tupla_vacia = ()
mi_primera_tupla = (10, "Hola", True) 
mi_tupla = 1, 2, 3, "oso", False #Puedo crear una tupla sin utilizar los ()
print( "El tipo de datos de mi tupla es:", type(mi_tupla), mi_primera_tupla)

#Acceder a los elementos de mi tupla
tupla_acceso = 0, 1, 2, "Pepe", 4
print("Accediendo a mi tupla:", tupla_acceso[3])
tupla_dentro_tupla = 1, 5, 8, ("y", "w", "z"), 5, 6 #Puedo anidar tuplas dentro de tuplas
print("Tupla dentro de otra tupla:", tupla_dentro_tupla[3][0])

#Modificar los elementos de mi tupla --> ERROR: TypeError: 'tuple' object does not support item assignment
modificar_tupla = 1, 2, 3, 4, 5
"""modificar_tupla[2] = 2 
print("Intentando modificar la tupla: ", modificar_tupla)"""

#Única forma de modificar una tupla: modificando la lista anidada
modificar_tupla_dos = 1, 2, 3, 4, 5, ["hola", "adios", "pepe"]
print("Tupla antes de modificación:", modificar_tupla_dos)
modificar_tupla_dos[5][1] = "ADIOS" #La reasignaciones me admiten cualquier tipo de dato
print("Tupla después de modificación:",modificar_tupla_dos[5][1])

#Asignar el valor de los elementos de una tupla a variables
tupla_asigna = 3, 4, 5
x, y , z = tupla_asigna
print("Asignación múltiple:",x, y, z)

#Convertir una lista en una tupla --> tuple()
lista_inicial = [7, 9, 11]
lista_convertida_tupla = tuple(lista_inicial) #Casting de datos para convertir una lista en una tupla
print("Tipo de lista convertida:", type(lista_convertida_tupla), "& Tipo de lista antes de la conversión:", type(lista_inicial))


""" 
¿Se puede modificar el tipod e dato de una lista dentro de una tupla?
modificar_tupla_dos = 1, 2, 3, 4, 5, ["hola", "adios", "pepe"]
modificar_tupla_dos[5] = tuple(modificar_tupla_dos[5])
print(modificar_tupla_dos)  TypeError: 'tuple' object does not support item assignment """