dict1 = {
    "Nombre":"Alfonso",
    "Apellidos":"Gonzalez Gonzalez",
    "Fecha de nacimiento":"28/10/2005",
    "Ciudad de nacimiento":"Madrid",
    "Nombre del padre":"Pedro",
    "Nombre de la madre":"Maria",
    }

dict2 = dict([
    ("Nº de DNI","31243657547636F"),
    ("Fecha de expedición","13/11/2012"),
    ("Fecha de caducidad","13/11/2019"),
])

dict3 = dict(
    Nacionalidad = "Española",
    Domicilio = "Paseo de los Reyes 14, Madrid",
)

print("Tus datos antiguos son:")
print(dict1)
print(dict2)
print(dict3)

print()
for key in dict1:
    nuevo_dato=str(input(f"Introduzca su nuev@ {key}:"))
    dict1[key] = nuevo_dato
print(f"\nEstos son tus nuevos datos: {dict1}")

print()
for key in dict2:
    nuevo_dato=str(input(f"Introduzca su nuev@ {key}:"))
    dict2[key] = nuevo_dato
print(f"\nEstos son tus nuevos datos: {dict2}")

print()
for key in dict3:
    nuevo_dato=str(input(f"Introduzca su nuev@ {key}:"))
    dict3[key] = nuevo_dato
print(f"\nEstos son tus nuevos datos: {dict3}")

nombres = {dict1['Nombre'], dict1["Nombre del padre"],dict1["Nombre de la madre"]}
name = str(input("\n¿A quien quieres buscar?, di su Nombre: "))
esta = name in nombres
print(f"¿esta {name} en la base de datos?: {esta}")


# Errores Jose Luis
Conjunto_dict1 = list(dict2)
Mi_nombre = "juan"
busca = Mi_nombre in Conjunto_dict1[2] #Ofrece True, si Mi_nombre = "Nombre"