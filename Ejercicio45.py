# Mensaje de bienvenida
print("Bienvenido a la lista de la compra.")

# Lista para almacenar los elementos de la compra
lista_compra = []

# Bucle para solicitar los elementos de la compra
while True:
    elemento = input("Introduce un elemento que deseas comprar (o escribe 'fin' para terminar): ")
    if elemento.lower() == 'fin':
        break  # Salir del bucle si el usuario escribe 'fin'
    else:
        lista_compra.append(elemento)  # Agregar el elemento a la lista de la compra

# Mensaje de despedida y lista de la compra
print("\nLista de la compra:")
for item in lista_compra:
    print("-", item)

print("\nGracias por usar la lista de la compra. ¡Que tengas un buen día!")
