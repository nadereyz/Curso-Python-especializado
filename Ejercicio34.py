almacen = [ #lista + tupla   la posicion seria "producto" -> "precio" -> "cantidad"
    ("Camisa", 23.5, 50),
    ("Pantalon", 31.2, 30),
    ("Zapatos", 26.7, 20),
    ("Corbata", 15, 40),
    ("Calcetines", 10, 100)
]
print("\n-----------------almacen------(ANTIGUO)-----")
for nombre, precio, cantidad in almacen:
    print(f"{nombre}          {precio}        {cantidad}")


# AÑADOR
almacen.append(("Gafas", 150, 10))

# ACTUALIZAR
almacen[almacen.index(("Camisa", 23.5, 50))] = ("Camisa", 20.0, 40)

# ELIMINAR
almacen.remove(("Calcetines", 10, 100))

# BUSCAR Y COMPROBAR SI EXISTE O NO
producto_buscado = ("Zapatos", 26.7, 20) in almacen



#ORDENAR
almacen.sort()
#CANTIDAD
cantidad_productos = len(almacen)

# PARA BUSCAR LA POSICION ---> PREGUNTAR PORQUE NO TENGO NI IDEA EL PORQUEEE
posicion_pantalones = (almacen.index(("Pantalon", 31.2, 30)) == almacen) # este no funciona
posicion_pantalones = almacen.index(("Pantalon", 31.2, 30)) >= 0 # pero este si funciona wtf xD


print("\n-----------------almacen------(ACTUAL)-----")
print("Nombre:         Precio:       Cantidad:")
for nombre, precio, cantidad in almacen:
    print(f"{nombre}          {precio}        {cantidad}")

print(f"\nCantidad de productos en almacen: {cantidad_productos}")
print(f"Posición de Pantalón en el almacen: {posicion_pantalones}")
print(f"Producto encontrado (zapatos): {producto_buscado}")

