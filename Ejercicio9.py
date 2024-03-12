print("Bienvenido!")

dato_precio =  float(input("Ingrese el precio del producto: "))

dato_descuento = float(input("Ingresa el numero para aplicar el descuento: "))

precio_final = dato_precio - (dato_precio * dato_descuento / 100)

print(f"Precio del producto: {dato_precio}€")
print(f"Descuento aplicado: {dato_descuento}%")
print(f"Precio final: {precio_final:.2f}€")