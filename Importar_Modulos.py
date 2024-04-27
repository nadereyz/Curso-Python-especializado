""" import usuarios


resultado_suma = usuarios.suma(3, 5)
print(resultado_suma) """
#import pandas as pd
import os #Proporciona funciones para interactuar con el SO: leer archivos, escribir archivos, manipular directorios, obtener información sobre el entorno del sistema..
import string
import sys #Proporciona acceso a variables y funciones específicas del intérprete de Python
import math #contiene funciones matemáticas
import random

#Ejemplo de uso de módulo os para mostrar el directorio actual
""" cwd = os.getcwd()
print("el directorio actual es: ", cwd) """

#Ejemplo de uso del módulo sys para obtener los argumentos de la línea de comandos

""" argumentos = sys.argv
print("Los argumentos de la línea de comandos son: ", argumentos)

version = sys.version
print("La versión de Python es: ", version) """

#Calcular el seno del angulo en radiantes
angle = math.pi / 4
sin_value = math.sin(angle) #Esta función sin() toma un angulo en radianes como argumento y nos devuelve su seno
print("Seno de π/4: ", sin_value)


#Calcular la raiz cuadrada de un número
raiz_cuadrada = math.sqrt(25)
print("La raiz cuadrada es: ", raiz_cuadrada)
""" 
1- División por funcionalidades o componentes: dividir en directorios que representen diferentes funcionalidades o componentes del sistema. 
mi proyecto
    autenticación
        __init__.py
        usuarios.py
        roles.py
    facturación
        __init__.py
        facturas.py
        pagos.py
    utilidades
        __init__.py
        funciones_básicas.py
        funciones_avanzadas.py
    __init__.py
    main.py

2- Nombres descriptivos: no utilizar modulo1 o paquete1. Los nombres deben reflejar el propósito o la funcionalidad del módulo. 
3- División por capas o niveles de abstracción: SE utiliza en proyectos grandes. Divido en el nivel más global de mi programa. 
mi_proyecto
    presentacion
    logica_aplicacion
    acceso_datos
4- Módulos de configuración y constantes: 
mi_proyecto
    configuracion
        __init__.py
        settings.py -> configuración del proyecto (BBDD, APIs...)
    constantes
        __init__.py
        constantes.py --> constantes globales de todo mi proyecto
"""

#print(dir(math))
#help(math)
#help(os)
#help(sys)

#Módulo random: funciones para generar números aleatorios y también realizar operaciones relacionadas con la aleatoriedad. 
"""    - random(): Devuelve un número aletorio en el rango (0.0, 1.0) 
       - randint(a, b): Devuelve un número aletorio en el rango [a, b] incluyendo los números dados como parámetros a la función
       - uniform(a, b)
       - choice(secuencia "seq")
       - shufefle..
       -sample..
"""
#Generar un número aleatorio entre 0.0 y 1.0
numero_random = random.random()
print("El número random es: ", numero_random)

#Generar un número aleatorio entre dos números dados
numero_random_dado = random.randint(1, 100) #Devuelve un int
print("El número random entre 1 y 100 es: ", numero_random_dado)

#Generar un número aleatorio de punto flotante entre dos números flotantes dados
numero_random_float = random.uniform(2.6, 7.8) #Devuelve un float
print("El número random entre 2.6 y 7.8 es: ", numero_random_float)

#Elegir un elemento aleatorio de una lista con choice
mi_lista = [1, 2, 3, 4, 5]
elemento_random = random.choice(mi_lista)
print("El número random de mi secuencia es: ", elemento_random)

#--> choice con string
mi_lista_dos = ["hola", "adios"]
elemento_random_str = random.choice(mi_lista_dos)
print("El elemento random de mi secuencia es: ", elemento_random_str)

#--> choice con una secuencia de datos de diferente tipo
mi_lista_tres = ["hola", "adios", 4, True]
elemento_random_mix = random.choice(mi_lista_tres)
print("El elemento random de mi secuencia es: ", elemento_random_mix)

#EJEMPLO MINIJUEGO PARA ADIVINAR NÚMEROS

def adivinar_numeros(intentos, numero_secreto):
    print("Bienvenido al minijuego de adivinar números")
    for i in range(intentos):
        intento = int(input("Introduce tu intento:"))
        
        if intento == numero_secreto:
            print("Has ganado")
            return True
        elif intento < numero_secreto:
            print("El número secreto es más alto")
        else:
            print("El número secreto es más bajo")
    
    print("Has perdido, el número secreto era: ", numero_secreto)
    return False        

intentos_permitidos = 6
numero_secreto = random.randint(1, 100)
   
adivinar_numeros(intentos_permitidos, numero_secreto)