# 1
peliculas = {}

print("Escribe 5 peliculas:")
for ingresar in range(5):
    titulo = input(f"Titulo de pelicula: ")
    anyo = int(input(f"anyo de lanzamiento de {titulo}: "))
    peliculas[titulo] = anyo
    ingresar+1

# 2
print("\nTítulos de las películas:")
for titulo in peliculas.keys():
    print(titulo)

# 3 21339
print("\nTítulos de las películas con sus anyos de lanzamiento:")
for titulo, anyo in peliculas.items():
    print(f"{titulo}: {anyo}")

# 4
print("\nanyos de lanzamiento de las películas:")
for anyo in peliculas.values(): # intente usar varias operadores y nada, solo funciona con la agrupacion *
    mayor_2000 = (anyo > 2000) 
    divisible_5 = (anyo % 5 == 0) 
    igual_1995 = (anyo == 1995) 
    print(f"{anyo} {mayor_2000} {divisible_5} {igual_1995}")

# 5
print("\nCOMPLETADO :D")