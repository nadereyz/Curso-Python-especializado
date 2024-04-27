salario_anual = float(input("Ingresa tu salario anual: "))

if salario_anual <= 10000:
    impuesto = salario_anual * 0.05
elif salario_anual <= 50000:
    impuesto = salario_anual * 0.10
elif salario_anual <= 100000:
    impuesto = salario_anual * 0.15
else:
    impuesto = salario_anual * 0.20

print(f"Tu salario anual es de ${salario_anual}")
print(f"El impuesto correspondiente es del {(impuesto / salario_anual) * 100:.0f}%, lo que equivale a ${impuesto:.2f}\n")

print("Impuestos para diferentes rangos de ingresos:")
for i in range(0, 200001, 10000):
  if i <= 10000:
    impuesto_rango = i * 0.05
  elif i <= 50000:
    impuesto_rango = i * 0.10
  elif i <= 100000:
    impuesto_rango = i * 0.15
  else:
    impuesto_rango = i * 0.20
  print(f"Salario anual de ${i} - ${i + 10000}: ${impuesto_rango:.2f}")




