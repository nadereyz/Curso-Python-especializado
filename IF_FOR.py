#------------- ESTRUCTURAS DE CONTROL-------------
"""Gracias a las estructuras de control podemos cambiar el flujo de ejecución de un programa"""

#CONDICIONAL IF: Nos permite tomar decisiones basadas en condiciones. Vamos a poder ejecutar un bloque de código si una condición dada para evaluacióne s tomada como verdadera. 
"""
SINTAXIS: 
if condicion:
    #Bloque de código que se va a ejecutar si la condicón evaluada es verdadera

· La expresión que sigue a if debe ser una expresión booleana, algo que pueda ser tomado como verdadero o falso.
· Si la condición es verdadera, se va a ejecutar el bloque de código identado debajo del if. Si la condición es tomada como falsa, el bloque de código del if se omite, y solo se ejecutará el bloque de código dentro de "else" en caso de que exista.
· En este tipo de estructyura solo se ejecutará el primer bloque de código cuya condición sea verdadera. 
"""

numero = int(input("Introduce un número"))
#verificar si el número es positivo o negativo
if numero >= 0: #numero > 0 or numero = 0
    print("El número es positivo")
else:
    print("El número es menor o igual a cero")
print("Estoy fuera del condicional") #La identación es fundamental para definir el bloque de código que pertene a nuestra estructura de control. En este caso el print que esta fuera se va a ejecutar siempre. 



"""
numero = int(input("Introduce un número"))
#verificar si el número es positivo o negativo
if numero > 0: 
    print("El número es mayor que cero")
elif numero < 0: #elif es la forma simplificada de "if else"
    print("El número es negativo")
elif numero == 7:
    print("El número es 7")
else:
    print("El número es cero")
print("Estoy fuera del condicional") #La identación es fundamental para definir el bloque de código que pertene a nuestra estructura de control. En este caso el print que esta fuera se va a ejecutar siempre. 


#Verificar si un número es par o impar:
numero_dos = 7
if  numero_dos % 2 == 0:
    print("Es par")
else:
    print("Es impar")"""

#Calculadora básica
print("Bienvenido a la calculadora del curso PYTHON")

#Solicitamos al usuario los operandos
num1 = float(input("\nIntroduce el primer operando\n"))
num2 = float(input("\nIntroduce el segundo operando\n"))

#Operaciones disponibles
print("operaciones disponibles:")
print("\n1. Suma")
print("\n2. Resta")
print("\n3. Multiplicación")
print("\n4. División")

#Pedimos al usuario que seleccione una operación
opcion = int(input("\nElige una operación (1/2/3/4):\n "))

""" if type(opcion) == str:
    print("Oye, que no puedes meter letras, introduce un número")
if type(opcion) == int:
    print("Oye, que no puedes meter números, introduce una letra")
if type(opcion) == float:
    print("Oye, que no puedes meter números con decimales, introduce un número entero") """

#Realizamos la operación seleccionada ys e la mostramos al usuario
if opcion == 1:
    resultado = num1 + num2
    print("El resultado de la suma es: ",resultado)
elif opcion == 2:
    resultado = num1 - num2
    print("El resultado de la resta es: ",resultado)
elif opcion == 3:
    resultado = num1 * num2
    print("El resultado de la multiplicación es: ",resultado)
elif opcion == 4:
    if num2 != 0:
        resultado = num1 / num2 
        print("El resultado de la división es: ",resultado)
    else:
        print("No es posible dividir entre cero")
else:
    print("Opción no válida, por favor indica el número correspondiente a la operación que deseas realizar.")


#FUNCIÓN range(): Genera una secuencia de números enteros. Puede tomar argumentos

for i in range(5):
    print(i)

for i in range(4, 8): #Me devuelve una iteración del 1 al 4, porque el número final no lo incluye
    print(i)

for i in range(0, 10, 2): #Devuele los numeros pares del 0 al 8 (inicio, final, incremento)
    print(i)

""" personas = int(input("Introduce el nunero de personas"))

for i in range(personas):
    print("Otra persona") """













