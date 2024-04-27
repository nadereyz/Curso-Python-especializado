import random


numeros_posibles = list(range(1, 51))

numero_randint = random.randint(1, 50)
print(f"Número seleccionado con randint: {numero_randint}")


numero_uniform = int(random.uniform(1, 50))
print(f"Número  con uniform (convertido a entero): {numero_uniform}")


numero_choice = random.choice(numeros_posibles)
print(f"Número seleccionado con choice: {numero_choice}")
