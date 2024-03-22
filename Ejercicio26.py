# Defino los conjuntos
aventura = set()
accion = set()
estrategia = set()
deportes = set()

# Preguntar al usuario y rellnar informacion
aventura_input = str(input("Pon juegos de aventuras (separa con ,): ").lower())
aventura.update(aventura_input.split(','))

accion_input = str(input("Pon juegos de accion (separa con ,): ").lower())
accion.update(accion_input.split(','))

estrategia_input = str(input("Pon juegos de estrategia (separa con ,): ").lower())
estrategia.update(estrategia_input.split(','))

deportes_input = str(input("Pon juegos de deportes (separa con ,): ").lower())
deportes.update(deportes_input.split(','))

print("\nResumen de las categorías de videojuegos:")
print(f"Aventura: {aventura} ----> Hay en total cantidad: {len(aventura)}")
print(f"Accion: {accion} ----> Hay en total cantidad: {len(accion)}")
print(f"Estrategia: {estrategia} ----> Hay en total cantidad: {len(estrategia)}")
print(f"Deportes: {deportes} ----> Hay en total cantidad: {len(deportes)}")


print(f"\nVideojuegos de acción y aventura: {accion.intersection(aventura)}")

print(f"Videojuegos de estrategia que no están en deportes: {estrategia.difference(deportes)}")

todos_los_videojuegos = aventura.union(accion, estrategia, deportes)
print(f"Todos los videojuegos únicos: {todos_los_videojuegos}")
