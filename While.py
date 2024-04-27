# --------- BUCLE WHILE -------------
""" 
En python se utiliza para ejecutar un bloque de cíodigo de forma repetida mientras se interprete como verdadera la condición dada

while -condicion-:
    #Código que vamos a ejecutar mientras la condición sea verdadera
"""

numero = 7
while numero <= 20:
    print("El número es", numero)
    numero += 1 

infinito = 0
while True:
    print("bucle infinito")
    infinito += 1
    if infinito == 15:
        break
print("C'est fini")

"""
--> Utiliza una condición diferente para implementar el bucle infinito
"""
