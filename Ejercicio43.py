print("Bienvenido")

invitados = []

while True:
    nombre = input("Pon tu nombre (si quieres finalizar escribe stop): ")
    if nombre.lower() == "stop":
        break
    invitados.append(nombre)




print("lista de invitados")
for recorrer in invitados:
    print("->", recorrer)

print("Adios cuidense")
