
"""
 EJERCICIO RETO DE PROGRAMACIÓN II - ¡ENCUENTRA LOS FALLOS! (Revisado)
 AUTORES: Manuel,Juan,Rafael y Jordi. 
 Enunciado: 
 Diseñar un avanzado algoritmo o programa en Python que acepte el registro de
 un propietario de una comunidad de vecinos y muestre por pantalla los datos. 


 """

# Recogida de datos para un propietario usando un diccionario
propietario = { # en vez de parentesis tiene que ser corchetes + camel case
    "nombre": str(input("Introduce el nombre del propietario: ")),
    "piso": int(input("Introduce el piso: ")), # tiene que ser " para ser como sintaxis total + sobra espacio antes del int
    "puerta": str(input("Introduce la puerta: ")),
    "moroso": bool(input("¿Es moroso? (True/False): ")),  # Falta la coma final + sobra el == True
    "garaje": bool(input("¿Tiene garaje? (True/False): ")) # en vez de boolean tiene que ser bool + input  + == True
}

# Mostrando los datos recogidos
print("/nDatos del propietario recogidos: ")
for clave, valor in propietario.items(): # camel case
    print(f"{clave.capitalize()}: {valor}") # tiene que ser minuscula (capitalize)

