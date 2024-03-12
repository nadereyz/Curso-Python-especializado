"""Ejercicio de andar por casa -
Crea una colección de datos inmutable, que me permita añadir los siguientes datos de usuario:
- Nombre y apellidos
- Edad
- Ciudad de nacimiento
- Ciudad de residencia."""


tupla_andar_casa = ["nombre", "apellidos"], [0], ["ciudad residencia"], ["ciudad nacimiento"]

tupla_andar_casa[0][0] = str(input("Introduce un nombre: "))
tupla_andar_casa[0][1] = str(input("Introduce un apellido: "))
tupla_andar_casa[1][0] = int(input("Introduce una edad: "))
tupla_andar_casa[2][0] = str(input("Introduce una ciudad de residencia: "))
tupla_andar_casa[3][0] = str(input("Introduce una ciudad de nacimiento: "))

print(tupla_andar_casa)

# --------------- MÉTODOS DE TUPLAS -----------------------

#Método count(): Este método nos devuelve el número de veces que aparece un valor en la tupla

tupla_count = (1, 2, 3, 1, 2, 3, 1, 2, 3)
veces_dos = tupla_count.count(2)
print("\nNúmero de veces que aparece el valor 2: ",veces_dos)

#Método index(valor, [inicio], [fin]): Devuelve el índice de la primera ocurrencia de un valor en la tupla
tupla_index = 10, 20, 30 , 40, 10, 50, 90, 10, 30, 40
indice = tupla_index.index(10)
print("\nIndex de la primera ocurrencia de 10: ", indice)
indice_dos = tupla_index.index(10, 1)
print("\nIndex de la segunda ocurrencia de 10: ", indice_dos)
indice_tres = tupla_index.index(10, 5, 8)
print("\nIndex de la ocurrencia de 10 entre los index 5 y 7: ", indice_tres)
