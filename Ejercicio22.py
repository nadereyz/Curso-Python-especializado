categorias_gastos = ["Comida", "Juegos", "Peliculas", "Servicios", "Otros"]

total_gastos = 0
gastos_por_categoria = {}

for categoria in categorias_gastos:
    gasto = float(input("Ingrese el importe de gasto para " + categoria + ": "))
    total_gastos += gasto
    gastos_por_categoria[categoria] = gasto

print("Resumen de Gastos Mensuales:")
for categoria, gasto in gastos_por_categoria.items(): #es para mostrar todo el elemento dentro de gastos_por_categoria
    print(f"{categoria}: {gasto:.2f} euritos")

print(f"Total de Gastos Mensuales: {total_gastos:.2f} euritos")
j