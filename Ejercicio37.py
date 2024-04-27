"""
1. Define un diccionario llamado **`enciclopedia_plantas`** que contenga 
información sobre diferentes plantas. Cada planta será representada por un diccionario anidado con las siguientes claves: 
"nombre", "especie", "familia", "origen", "altura" y "usos". Puedes agregar al menos 3 plantas con esta estructura.


2. Crea una lista llamada **`nombres_plantas`** que contenga los nombres de todas las plantas presentes en la enciclopedia.


3. Agrega una nueva planta a la enciclopedia. 
Para ello, solicita al usuario que ingrese los detalles de la nueva planta y agrégalos al diccionario principal **`enciclopedia_plantas`**.




4. Imprime la información de todas las plantas de la enciclopedia. Recorre la lista de nombres de plantas 
(**`nombres_plantas`**) y utiliza cada nombre para acceder al diccionario correspondiente en **`enciclopedia_plantas`** y mostrar toda la información de la planta.



5. Finalmente, muestra el número total de plantas presentes en la enciclopedia. Utiliza la función **`len()`** para determinar la longitud de la lista de nombres de plantas.

"""

enciclopedia_plantas = {
    "girasol": {
        "nombre": "Girasol",
        "especie": "Helianthus annuus",
        "familia": "Asteraceae",
        "origen": "América del Norte",
        "altura": "Hasta 3 metros",
        "usos": "Alimentacion, aceite"
    },
    "Orquideas": {
        "nombre": "Orquideas",
        "especie": "Orchidaceae",
        "familia": "Orchidaceae",
        "origen": "Diversos lugares del mundo",
        "altura": "Varía según la especie",
        "usos": "Ornamental"
    },
    "Margaritas": {
        "nombre": "Margaritas",
        "especie": "Leucanthemum vulgare",
        "familia": "Asteraceae",
        "origen": "Europa, Asia, África",
        "altura": "Hasta 1 metro",
        "usos": "Ornamental"
    }
}

nombre_planta = enciclopedia_plantas

añadir_planta = {}

print("escribe nuevos datos a la nueva planta")
añadir_planta["nombre"] = str(input("Inserta nombre: "))
añadir_planta["especie"] = str(input("Inserta especie: "))
añadir_planta["familia"] = str(input("Inserta familia: "))
añadir_planta["origen"] = str(input("Inserta origen: "))
añadir_planta["altura"] = str(input("Inserta altura: "))
añadir_planta["usos"] = str(input("Inserta usos: "))

enciclopedia_plantas["planta4"] = añadir_planta

print("\nInformación de todas las plantas en la enciclopedia:")
for nombre_planta in nombre_planta:
    planta = enciclopedia_plantas[nombre_planta]
    print(f"\nNombre: {planta['nombre'].capitalize()}")
    print(f"Especie: {planta['especie'].capitalize()}")
    print(f"Familia: {planta['familia'].capitalize()}")
    print(f"Origen: {planta['origen'].capitalize()}")
    print(f"Altura: {planta['altura'].capitalize()}")
    print(f"Usos: {planta['usos'].capitalize()}")

num_plantas = len(enciclopedia_plantas)
print("\nNumero total de plantas en la enciclopedia:", num_plantas)








