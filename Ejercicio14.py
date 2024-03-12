

estudiante = int(input("Ingresa aqui tu nota: "))

aprobado = estudiante >= 60

print(f"Puntuacion del estudiante: {estudiante}")
print(f"El estudiante ha aprobado: {aprobado}")

#---------
admin = True
premium = False
acceso_usuario = admin or premium

print(f"\nUsuario es administrador: {admin}")
print(f"Usuario tiene suscripción premium: {premium}")
print(f"El usuario tiene acceso: {acceso_usuario}")
#-----------

numero_evaluar = 45
num_positivo = 0 < numero_evaluar < 100
print(f"\nNúmero a evaluar: {numero_evaluar}")
print(f"El número es positivo: {num_positivo}")

#--------

goles_favor = int(input("Ingresa gol a favor: "))
goles_contra = int(input("ingresa gol a contra: "))
equipo_gana = goles_favor >= 3 and goles_contra == 0
print(f"\nGoles a favor: {goles_favor}")
print(f"Goles en contra: {goles_contra}")
print(f"El equipo ha ganado: {equipo_gana}")





