compras_enero = (14.5, 220.5, 9.25, 70.75, 45.0)

total_enero = sum(compras_enero)

precio_mas_caro_enero = max(compras_enero)

compras_febrero = (2.0, 2.5, 1.75, 3.5, 7.8, 4.2, 5.3)

# No entiendo que tengo que poner (PREGUNTAR A ALEJANDRA EN CLASE!)
#cantidad_producto_febrero = compras_febrero.count()

precio_mas_alto = max(compras_enero + compras_febrero)

total_compras = sum(compras_enero + compras_febrero)

precios_orden = sorted(compras_enero + compras_febrero)


print("Total gastos en enero:", total_enero)
print("Producto mas caro en enero:", precio_mas_caro_enero)
#print("Las Veces que compro en febrero:", cantidad_producto_febrero)
print("Precio mas alto entre enero y febrerro:", precio_mas_alto)
print("Gasto total en ambos meses:", total_compras)
print("Precios ordenados en entre enero y febrero:", precios_orden)
