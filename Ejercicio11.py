print("Bienvenido a la calculadora humana")

fecha_nacimiento = int(input("Ingresa tu año de nacimiento: "))
fecha_actual = int(input("Ingresa la fecha actual: "))

edad_actual = fecha_actual - fecha_nacimiento

edad_actual5 = edad_actual + 5

edad_actual10 = edad_actual + 10

print(f"Tienes {edad_actual} años, Aun te queda por vivir")
print(f"En 5 años tendras {edad_actual5}")
print(f"En 10 años tendras {edad_actual10}")