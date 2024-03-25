
tareas_pendientes = ['dormir', 'jugar', 'limpiar', 'hablar', 'comer']
lista_compras = {'pan', 'leche', 'huevos', 'queso', 'frutas'}
agenda_contactos = {'Juan': '123456789', 'María': '987654321', 'Pedro': '456789123', 'Laura': '321654987', 'Carlos': '654321987'}


tareas_pendientes.append('mirar')
tareas_pendientes.remove('limpiar')
tareas_pendientes.sort()
#tareas_pendientes.clear()



lista_compras.add('arroz')
lista_compras.discard('pan')
#lista_compras.clear()


agenda_contactos.update({'Ana': '111111111', 'Luis': '222222222'})
sorted_contacts = sorted(agenda_contactos.items())
agenda_contactos.pop('Juan')
#agenda_contactos.clear()


print("\nTareas Pendientes: ", tareas_pendientes)
print("\nLista de Compras: ", lista_compras)
print("\nAgenda de Contactos: ", agenda_contactos)
print("Contacto en orden: ",sorted_contacts)


salir = input("\nEscribe si o no para salir del programa:\n").lower()
print((salir == "si") and (salir, "Saliendo...") or (salir == "no") and (salir, "Pues nada, quedate xD."))


