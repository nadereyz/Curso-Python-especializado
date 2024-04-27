""" Escribe un programa en Python que solicite al usuario ingresar el precio de un 
producto y su descuento. El programa debe calcular el precio final después del descuento y mostrar el resultado. 
Utiliza un operador ternario para manejar el caso en el que el descuento sea mayor que el precio del producto, 
en cuyo caso se mostrará un mensaje indicando que el descuento no es válido.

1. Solicita al usuario que ingrese el precio del producto y su descuento en porcentaje.
2. Utiliza un operador ternario para calcular el precio final después del descuento.
3. Si el descuento es mayor que el precio del producto, muestra un mensaje indicando que el descuento no es válido.
4. Si el descuento es válido, muestra el precio final después del descuento. """

precio_producto = float(input("Ingresa el precio del producto: "))
descuento = float(input("Ingrese el descuento en porcentaje: "))

precio_final = precio_producto - precio_producto * descuento / 100; print(f"El precio final después del descuento es:  {precio_final:.2f}") if descuento <= 100 else "descuento no es valido"
