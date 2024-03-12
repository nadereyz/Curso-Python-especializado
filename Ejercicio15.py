print("Bienvenido al calculador de impuestos trimestrales para autónomos")

ingresos_totales = float(input("Ingrese sus ingresos totales del trimestre: "))
gastos_deducibles = float(input("Ingrese sus gastos deducibles del trimestre: "))
otros_gastos_no_deducibles = float(input("Ingrese otros gastos no deducibles del trimestre: "))

base_imponible = ingresos_totales - gastos_deducibles - otros_gastos_no_deducibles

impuesto = 0.10 * base_imponible


print("\nResultados del cálculo de impuestos:")
print(f"Ingresos totales: {ingresos_totales:.2f}€")
print(f"Gastos deducibles: {gastos_deducibles:.2f}€")
print(f"Otros gastos no deducibles: {otros_gastos_no_deducibles:.2f}€")
print(f"Base imponible: {base_imponible:.2f}€")
print(f"Impuesto a pagar: {impuesto:.2f}€")
