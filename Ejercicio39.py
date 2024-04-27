inicio = int(input("Pon numero inicial: "))
fin = int(input("Pon numero final: "))
hay_pares = False
if inicio <= 0:
    print("Numero inicial desde 0.")
elif fin <= 0:
    print("Numero final desde fin.")
elif inicio >= fin:
    print("A ver ahio")
else:
    hay_pares 
 

    print("Los numeros pares:")
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:
            print(numero)
            hay_pares = True
        
    else:
        print("No hay mas pares dentro de este rango.")
        


