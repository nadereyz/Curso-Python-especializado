datos_basicos = {
    "Nombre": "Nader",
    "Apellidos": "El Yacoubi",
    "Fecha de nacimiento": "1998",
    "Ciudad de nacimiento": "Madrid",
    "Nombre del padre": "Papa",
    "Nombre de la madre": "Mama"
}

datos_dni = {
    "Dni": "x123456789",
    "Fecha de expedicion": "20/20/1000",
    "Fecha de caducidad": "11/11/1111"
}

datos_personales = dict(
    Nacionalidad = "Ekisde",
    Domicilio = "Opesidke"
)

print("-------------------------------------------------------------------------------------------------------------")

print("Datos antiguos del diccionario:")
print("Datos básicos:", datos_basicos)
print("Datos del DNI:", datos_dni)
print("Datos personales:", datos_personales)

print("-------------------------------------------------------------------------------------------------------------")

datos_basicos["Nombre"] = str(input("Ingrese el nuevo valor para 'Nombre': "))
datos_basicos["Apellidos"] = str(input("Ingrese el nuevo valor para 'Apellidos': "))
datos_basicos["Fecha de nacimiento"] = str(input("Ingrese el nuevo valor para 'Fecha de nacimiento': "))
datos_basicos["Ciudad de nacimiento"] = str(input("Ingrese el nuevo valor para 'Ciudad de nacimiento': "))
datos_basicos["Nombre del padre"] = str(input("Ingrese el nuevo valor para 'Nombre del padre': "))
datos_basicos["Nombre de la madre"] = str(input("Ingrese el nuevo valor para 'Nombre de la madre': "))

datos_dni["Nº de DNI"] = str(input("Ingrese el nuevo valor para 'Nº de DNI': "))
datos_dni["Fecha de expedición"] = str(input("Ingrese el nuevo valor para 'Fecha de expedición': "))
datos_dni["Fecha de caducidad"] = str(input("Ingrese el nuevo valor para 'Fecha de caducidad': "))

datos_personales["Nacionalidad"] = str(input("Ingrese el nuevo valor para 'Nacionalidad': "))
datos_personales["Domicilio"] = str(input("Ingrese el nuevo valor para 'Domicilio': "))

print("-------------------------------------------------------------------------------------------------------------")

print("\nDatos actualizados del diccionario:")
print("Datos básicos:", datos_basicos)
print("Datos del DNI:", datos_dni)
print("Datos personales:", datos_personales)
