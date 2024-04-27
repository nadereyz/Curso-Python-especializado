"""
Solicitar al usuario que ingrese la cantidad de personas cuyas edades desea evaluar.
Utilizar un bucle for para iterar sobre cada persona y solicitar su edad.
Utilizar un condicional if dentro del bucle para evaluar la edad de cada persona y mostrar un mensaje dependiendo del rango de edad:
Si la edad está entre 0 y 12 años (inclusive), mostrar el mensaje "Eres un niño".
Si la edad está entre 13 y 19 años (inclusive), mostrar el mensaje "Eres un adolescente".
Si la edad está entre 20 y 64 años (inclusive), mostrar el mensaje "Eres un adulto".
Si la edad es 65 o mayor, mostrar el mensaje "Eres un adulto mayor".
Mostrar el mensaje correspondiente al rango de edad detectado para cada persona.
"""

personas = int(input("Cuantas personas quieres para evaluar? \n"))

for msg in range(personas):
    edad = int(input(f"Escribe tu edad: \n"))
    if edad <= 13:
        print("Eres un niño")
    elif edad <= 19:
        print("Eres un adolescente")
    elif edad <= 64:
        print("Eres un adulto")    
    else: print("Eres un abuelit@ <3")




        