puntuacion = 100

print("Puntuacion Inicial:", puntuacion)

puntuacion += 10
print(f"Puntuacion despues de incrementar: {puntuacion} ----> Ha adquirido una vida extra")

puntuacion -= 5
print(f"Puntuacion despues de reducir: {puntuacion} ----> Ha sido alcanzado por un enemigo")

puntuacion *= 2
print(f"Puntuacion despues de multiplicar por 2: {puntuacion} ----> Ha recibido un bonus extra")

puntuacion /= 4
print(f"Puntuacion despues de dividir por 4: {puntuacion} ----> Ha repartido el botin entre el equipo")

puntuacion %= 3
print(f"Puntuacion despues de calcular el modulo: {puntuacion} ----> Ha perdido la parte del botin no repartida de forma equitativa entre los miembros del equipo")
