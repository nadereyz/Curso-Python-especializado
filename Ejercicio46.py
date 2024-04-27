altura = int(input("Pon numeros: "))

for i in range(1, altura + 1): # empiezo con la primera posicion hasta la posicion que escribe altura
    for j in range(altura - i):
        print(" ", end="") # cada vez que imprimo pues elimino  el espacio de la ultima columna.
    for k in range(i):
        print("*", end="") # y aqui pues se crea # 
    print()
