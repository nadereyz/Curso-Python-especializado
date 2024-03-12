print("*.* bienvenido al programa de almacenamiento de nombres*.*")
nombres = [] #queremos recibir una lista por entrada
nombres.append(str(input("introduce un nombre: ")))# pide nombre que es un elemento de la lista
nombres.append(str(input("introduce un nombre: ")))
nombres.append(str(input("introduce un nombre: ")))
almacen = nombres #creamos una variable para guardar la lista
longitud = (len(almacen))# nos dice cuantos elementos se han introducido
print(f"los nombres introducidos son: {longitud} ")
nombre_lista = input("comprueba si el nombre esta en la lista: ")#comprueba si el dato introducido esta en la lista
comprobarnombre = nombre_lista in nombres
print(f"el nombre esta en la lista:true y si no esta:false = {comprobarnombre}")
print("Nombres en mayúsculas:")
for elemento in almacen:
    print(f"Los nombres que están almacenados son {elemento.upper()}")
print("----------------------------------------")
print("Nombres en minúsculas:")
for elemento in almacen:
    print(f"Los nombres que están almacenados son {elemento.lower()}")
copia_almacen = almacen.copy()
#eliminar elemento de la lista de almacen
nombre_eliminar = input("introduce el nombre que quieres eliminar: ")
borrar_nombre = almacen.remove(nombre_eliminar)
print("la lista nueva ",almacen)
print(f"Copia de la almacen {copia_almacen}")
copia_almacen.clear()#borramos la copia antigua e imprimimos la lista nueva.
print(f"la lista nueva está borrada, {copia_almacen}") 