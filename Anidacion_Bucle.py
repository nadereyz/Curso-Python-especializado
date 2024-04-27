#-------ANIDACIÓN EN LOS BUCLES-----------
""""""

nombres = ["Juan", "María", "Carlos"]
saludos = ["Hola", "Adiós"]

for nombre in nombres: #El bucle externo es el que controla el flujo general de la iteración
    for saludo in saludos: #Se ejecuta completamente en cada ciclo del bucle externo
        print(saludo, nombre)


for numero in range(1, 6):
    for numero_dos in range(1, 11):
        print(numero * numero_dos, end="\t") #Por defecto, el caracter de salida al final de un print() siempre es un salto de línea
    print()

#-----------------------------
    

for i in range(5):
    for j in range(i+1):
        print("*", end="\t")
    print(i)