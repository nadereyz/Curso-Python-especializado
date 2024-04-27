#DOCSTRING: documentación de Funciones
"""
1- Consistencia
2- Claridad: La documentación debe reflejar siempre: qué hace la función, qué argumentos espera, qué valor devuelve y opcionalmente, las excepciones que mi función puede lanzar.
3- Concisión
4- Completitud
5- Formato: docstring de una línea, o el multilínea.
6- Sintaxis: Se forman con """ """ - triple comillas
7- Para dar formato de texto o estilo a mi documentación puedo utilizat Markdown o reStructureText.
"""

"""
Comentarios que generamos utilizando """ """  en Python se llaman docstrings. Nos sirven para documentar funciones. 
"""

def suma(a, b):
    """
    Esta función suma dos números enteros y retorna el resultado

    Argumentos: 
    · a -- El primer número entero que se va a sumar
    · b -- El segundo número entero que se va a sumar

    Retorna:
    --> El resultado de la suma de a y b
    """
    # Retornamos el resultado de la suma entre a + b
    return a + b


help(suma)  #Muestra la documentación completa de la función "suma". Para salir de la ayuda pulsaremos la tecla "Q"/ :q
print(suma.__doc__)

#Reglas más importantes recogidas en el documento PEP 257 sobre la documentación de las funciones


# --------- FUNCTION ANNOTATION ---------
"""Es una característica opcional que nos va a permitir agregar metadatos a los parámetros de entrada y de salida de una función. 
--> NO SON VERIFICACIONES EN TIEMPO DE EJECUCIÓN: No van a afectar al comportamiento de mi función. Si yo añado otro tipo de dato diferente al proporcionado en la anotación de función, la verificación no se va a realizar en tiempo de ejecución. NECESITO UNA HERRAMIENTA EXTERNA O BIBLIOTECA ESPECÍFICA 
--> AYUDAN A DOCUMENTAR EL CÓDIGO Y MEJORAR SU CLARIDAD
--> A partir de Python 3.0
"""

def suma_dos(a: int, b: int) -> int:
    print(a + b)
    return a + b 

suma_dos("Hola,", "Adios")

"""INCISO RETURN
--> Qué es: Es una palabra clave utilizada para salir de una función y devolver un valor o resultado al punto donde es llamada la función
--> Por qué es importante: Porque sin return las funcipones no van a poder comunicar resultados o realizar cualquier acción significativa no vinculada con otra función.
--> El propósito de mi sentencia return va a ser devolver un valor que ha sido calculado dentro de la función para que pueda ser utilizado fuera de la misma por otras partes del programa. También puede ser utilizado para salir antes de la función si se cumple una condición específica.
"""

#Retorno condicional
def es_positivo(numero: int):
    if numero > 0:
        return "El número es positivo :)"
    else:
        return "El número es negativo :("
    
print(es_positivo(-8))

#Retorno temprano
def dividir(n1: int, n2:int)-> float:
    if n2 == 0:
        return "Error: No puedes dividir un número entre cero"
    return n1 / n2
