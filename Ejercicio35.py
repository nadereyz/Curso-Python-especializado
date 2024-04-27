# 1
peliculas = {}

print("Escribe 5 peliculas:")
for ingresar in range(5):
    titulo = input(f"Titulo de pelicula: ")
    anyo = int(input(f"anyo de lanzamiento de {titulo}: "))
    peliculas[titulo] = anyo
    ingresar += 1

# 2
print("\nTitulos de las películas:")
for titulo in peliculas.keys():
    print(titulo)

# 3 
print("\nTitulos de las películas con sus anyos de lanzamiento:")
for titulo, anyo in peliculas.items():
    print(f"{titulo}: {anyo}")

# 4
print("\nanyos de lanzamiento de las películas:")
for anyo in peliculas.values(): # intente usar varias operadores y nada, solo funciona con la agrupacion *
    print("Año antes de 2000 -> ",anyo > 2000)
    print("Divisible por 5:", anyo % 5 == 0)
    print("Igual a 1995:", anyo == 1995)


# 5
print("\nCOMPLETADO :D")