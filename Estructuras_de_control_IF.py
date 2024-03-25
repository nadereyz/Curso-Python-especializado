"""
hola = "hola"

if hola  == "hola":
    print("Es igual")
else:
    print("No es igual")
"""


num1 = float(input("pon tu primer numero: "))
num2 = float(input("pon tu segundo numero: "))
print("\n")

print("operaciones disponibles: ")

print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")
opcion=int(input("Selecciona 1 - 2 - 3 - 4: "))

if opcion==1:
    print("la suma es: ", num1+num2)
elif opcion==2:
         print("la resta es: ", num1-num2)
elif opcion==3:
   print("la multiplicacion es: ", num1*num2)
elif opcion==4:
        print("La división es: ", num1/num2)
else:
        print("no se puede dividir entre cero")