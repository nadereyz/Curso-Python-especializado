#Operador ternario: Es el operador condicional que me permite escribir un condicional de forma compacta


""" xy = 11
resultado_xy = "positivo" if xy > 0 else "negativo" """
"""
variable = -resultado si condición que se ejecuta es verdadero- + -condición booleana a evaluar (comenzando con el if)- + -else + resultado si condición que se ejecuta si es falsa-

"""

""" x = 0
if x > 0:
    resultado = "positivo"
else:
    resultado = "negativo"
print(resultado) """

#------ EJEMPLOS -------
#1- Asignación de valor a una variable basado en una condición

""" edad = int(input("Introduce tu edad"))
mensaje = "Eres mayor de edad, bienvenido, puedes acceder" if edad >= 18 else "Eres menor de edad, lo sentimos, tienes el acceso restringido"
print(mensaje) """

"""
--> Realiza el ejercicio anterior pero preguntando al usuario su año de nacimiento, y únicamente permítele entrar si es mayor de edad
"""

""" #2- Impresión condicional de un mensaje
xyz = 5
print("El número es 7" if xyz == 7 else "No es 7") """

"""
--> Solicita a un estudiante que te diga su nota, y en función de la nota imprime un mensaje diciendo que ha aprobado u otro diciendo que ha suspendido. Para ello utiliza la sintaxis del ejemplo que acabamos de ver.
"""

""" nota = float(input("Ingresa tu nota: "))

print("Has aprobado" if nota >= 5 else "Has suspendido") """


""" num = int(input("pon tu numero favorito: "))
num = num - 1 if num > 0 else num
print(num) """

edad = int(input("Pon tu año de nacimiento: "))
msg = "Eres mayor de edad" if edad <= 2006 else "Eres menor de edad"
print(msg)






















