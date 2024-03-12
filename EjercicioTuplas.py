nombre = str(input("Ingrese el nombre del usuario: "))
edad = int(input("Ingrese la edad del usuario: "))
ciudad_nacimiento = input("Ingrese la ciudad de nacimiento del usuario: ")
ciudad_residencia = input("Ingrese la ciudad de residencia del usuario: ")

usuario = (nombre, edad, ciudad_nacimiento, ciudad_residencia)

print("\nDatos del usuario:")
print(f"Nombre: {usuario[0]}")
print(f"Edad: {usuario[1]}")
print(f"Ciudad de nacimiento: {usuario[2]}")
print(f"Ciudad de residencia: {usuario[3]}")