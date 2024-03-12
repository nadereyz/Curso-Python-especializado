print("Bienvenido!")
ingresar = float(input("Ingresa el monto total de la factura del restaurante: "))
propina_porcentaje = float(input("Ingresa la propina que quieres dejar: "))

propina = ingresar * (propina_porcentaje / 100)

ingresar_total = ingresar + propina

print(f"\nIngreso de restaurante: {ingresar}€") 
print(f"Porcentaje de propina: {propina_porcentaje}%")
print(f"Ingreso final: {ingresar_total:.2f}€")

