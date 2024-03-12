#Esto es un comentario de una sola línea

"""Esto
es un comentario
en bloque: Los comentarios son fragmentos de código que son ignoradas por el intérprete. Para crear un bloque de código comentado, podemos seleccionarlo y pulsar el atajo
"""

print("Estoy programando en Python ")

#Ejemplos de tiposd e datos

_numero = 3 #Los nombre de variables no pueden comenzar por un número ni por un caracter especial, a excepción del _
numero = 42

#Puedo declarar varias variables a la vez
nombre, edad, altura = "Juan", 30, 1

print(nombre)

#namning de las variables --> Minúyscula + snake_case

mi_nombre_es = "Alejandra" #str (String)
dato_numero = 2888 #int (Entero)
dato_decimal = 345.234 #float (Decimal)
dato_cadena_de_caracteres = "esto es una cadena"
dato_cadena_de_caracteres_dos = 'esto es una cadena'

""" EJERCICIO 1
Crea 3 variables, una de tipo número que represente tu edad, otra de tipo string que represente tu nombre y otra de tipo decimal que represente tu peso.
Imprime estas variables utilizando la función print() """

edad = 33
nombre = "Alejandra"
peso = 23.67

print("Mi nombre es " , nombre , " y mi edad es " , edad) #Conversión de variables

#Siempre antes y después de un operador, tengo que incluir un espacio (el símbolor = es en Python el operador de asignación, el que utilizamos para asignar un valor a una variable)

edad = 25
nombre = "Nader"
peso = 110.5
print("mi nombre es: ", nombre , "y mi edad es ", edad , "mi peso actualmente" , peso)

""" EJERCICIO 2

Crea un cuento modelo que incluya al menos 10 datos diferentes personalizados del niño o niña al que va dirigido el cuento. La declaración de variables debe ser en bloque. Ejemplo:

ciudad, year, nombre_niño = "Bogotá", 2021, "Nicolás"
print("Amanece en " + ciudad + "en el año " + str(year)+ "..." ) """  #El naming de una variable no puede empezar con un número, ni con un caracter especial a excepción de _


city, years, girl_name, girl_age, gender, favorite_animal, favorite_color, favorite_food, favorite_hobby, best_friend = "Madrid", 2010, "Sofia", 14, "girl", "cat", "red", "vegetables", "dancing", "Pepito"

print(f"Habia una ciudad que se llama {city}, en los anyos {years}, vivia una ninya llamada {girl_name}.") 
print(f"A sus {girl_age} años, {girl_name} era una {gender} muy alegre y curiosa. ")
print(f"Su animal favorito era el {favorite_animal}, de un color {favorite_color} brillante, y le encantaba comer {favorite_food}. ")
print(f"Su pasatiempo favorito era {favorite_hobby} y su mejor amigo se llamaba {best_friend}. Juntos, vivian muchas aventuras emocionantes en {city}.")


