playlist_a = {"color caramelo", "barrio", "fondo flamenco", "me voy de la ciudad", "mi estrella blanca"}
playlist_b = {"fondo flamenco", "brillando sin luz", "big dog", "milo j", "trueno"}

playlist_a.add("nueva cancion")

playlist_b.discard("big dog")

union_playlist = playlist_a.union(playlist_b)

comprobar_playlist = playlist_a.intersection(playlist_b)

diferencia_playlist = playlist_a.difference(playlist_b)

print("\nLista de reproduccion A:", playlist_a)
print("\nLista de reproduccion B:", playlist_b)
print("\nJuntar listas de canciones:", union_playlist)
print("\nCanciones que estan repetidas en las listas de reproducción:", comprobar_playlist)
print("\nDiferencia entre las listas de A y B:", diferencia_playlist)
