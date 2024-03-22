contacto_tlf = {
    "Pepito": "123456789",
    "Kevinito": "987654321",
    "Carlitos": "1111111111"
}
print("\nAgenda de telefono actual:")
print(contacto_tlf)

print("el numero de juan es -->", contacto_tlf["Pepito"])

contacto_tlf["Laurita"] = "111222333"

contacto_tlf["Carlitos"] = "999888777"

del contacto_tlf["Kevinito"]

print("\nAgenda de telefono actualizado:")
print(contacto_tlf)
