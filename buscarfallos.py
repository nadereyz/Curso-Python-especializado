tareas_pendiente = ['lavar ropa', 'compra', 'tintoreria', 'limpieza', 'comidas']
lista_compras = ['fiambre', 'pollo', 'carne', 'pescado', 'fruta']
agenda_contactos = {
    "jose":"625515986",
    "pepe":"756894423",
    "laura":"895447896",
    "esther":"345982654",
    "paula":"654988723"
}

tareas_pendiente.append('baños')
tareas_pendiente.remove("limpieza")
tareas_pendiente.sort()
print("\nTareas pendientes: \n",tareas_pendiente)
tareas_pendiente.clear()
print("\ntareas pendientes está vacia:\n", tareas_pendiente)

"""añadir_a_lista_compras = {'naranjas', 'peras', 'piña'}.add(lista_compras)
"""

print("\nAñadiendo a la lista de compras:\n", lista_compras)


actualizar_agenda_contactos = {'patri':'658989865', 'isabel':'789098765','luis':'456987563'}
actualizar_agenda_contactos.update(agenda_contactos)
print("\nAgenda de contactos actualizada", actualizar_agenda_contactos)