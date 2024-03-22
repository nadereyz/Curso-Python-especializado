"""PROGRAMA GESTION DE INVENTARIO. """


inventario = [
    {"nombre1": "Laptop Dell", "precio": 800.99, "cantidad": 7},
    {"nombre2": "Tablet iPad", "precio": 600.99, "cantidad":  15},
    {"nombre3": "Teclado Razer BlackWidow Chroma", "precio": 250.99, "cantidad": 10},
    {"nombre4": "Mouse Logitech G502", "precio": 100.99, "cantidad": 5},
]
print("Inventario de productos:\n", inventario)
print("\n")

inventario.append({"nombre: Telefono Samsung S22, precio: 600, cantidad: 3"})
print("Aqui tenemos el inventario actualizado despues de añadir;Samsung S22: \n",inventario)

inventario[1]['cantidad'] -= 5 
print(f"\nCantidad disponible de {inventario[1]['nombre2']}: {inventario[1]['cantidad']}")
print("Aqui tenemos el inventario actualizado: \n",inventario)
print("\n")

print("Producto eliminado: ", inventario[2])
inventario.remove(inventario[2]) 
print("Aqui tenemos el inventario actualizado: \n",inventario)
print("\n")

producto_buscado = {"nombre1": "Laptop Dell", "precio": 800.99, "cantidad": 7} in inventario
print (producto_buscado)




""" inventario = sorted(inventario)
print("El inventario ordenado alfabeticamente: \n", inventario)
print("\n")
 """
#- Cuenta cuántos productos tienes en el inventario.
  
  

print("\n")

