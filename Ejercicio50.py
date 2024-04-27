#-- Resultado aplicando el retorno temprano --

# Definir las palabras clave
palabras_clave = ["secreto", "confidencial", "urgente", "importante"]

# Definir la función buscar_palabras_clave
def buscar_palabras_clave(mensaje):
    for palabra in palabras_clave:
        if palabra in mensaje:
            return "Se han encontrado palabras clave en el mensaje"
    return "No se han encontrado palabras clave en el mensaje"

# Solicitar al usuario que ingrese las frases
mensaje1 = str(input("Ingresa una frase para evaluar:\n"))
mensaje2 = str(input("Ingresa una frase para evaluar:\n"))
mensaje3 = str(input("Ingresa una frase para evaluar:\n"))

print(buscar_palabras_clave("Mensaje 1:", mensaje1))  
print(buscar_palabras_clave("Mensaje 2:", mensaje2))  
print(buscar_palabras_clave("Mensaje 3:", mensaje3)) 

#------------

# Definir las palabras clave
palabras_clave = ["secreto", "confidencial", "urgente", "importante"]

# Definir la función buscar_palabras_clave
def buscar_palabras_clave(mensaje):
    for palabra in palabras_clave:
        if palabra in mensaje:
            return "Se han encontrado palabras clave en el mensaje"
    else:
        return "No se han encontrado palabras clave en el mensaje"

# Solicitar al usuario que ingrese las frases
mensaje1 = str(input("Ingresa una frase para evaluar:\n"))
mensaje2 = str(input("Ingresa una frase para evaluar:\n"))
mensaje3 = str(input("Ingresa una frase para evaluar:\n"))

print(buscar_palabras_clave(mensaje1))
print(buscar_palabras_clave(mensaje2))
print(buscar_palabras_clave(mensaje3))
