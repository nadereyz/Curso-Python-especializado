# SOLUCIÓN DE FRAN

#Solicita al usuario que introduzca un límite para la suma
limite = int(input("Introduzca un límite para la suma: "))

# Inicializa la variable suma parcial
suma = 0

# Utiliza un bucle while para permitir al usuario introducir números
while True:
    # Solicita al usuario que introduzca un número
    numero = int(input("Introduzca un número: "))

    # Sume el número a la suma parcial
    suma += numero

    # Muestre la suma parcial
    print(f"Suma parcial: {suma}")

    # Si la suma alcanza o supera el límite, muestre un mensaje
    if suma >= limite:
        print(f"¡Has alcanzado el límite de {limite}!")
        break

# Agradece al usuario por jugar a nuestro juego
print("Gracias por jugar a nuestro juego interactivo de suma 😊.")