
saldo_inicial = float(input("Ingrese su saldo inicial: "))

print("Bienvenido al registro de gastos y ahorros.")
print("Saldo inicial:", saldo_inicial)

registro = []
gasto = float(input("Ingrese el importe del gasto: "))
saldo_inicial = saldo_inicial - gasto
registro.append(-gasto)


print("Saldo actualizado:", saldo_inicial)

ahorro = float(input("Ingrese el importe del ahorro: "))

saldo_inicial = saldo_inicial + ahorro

registro.append(ahorro)

print(f"Saldo final: {saldo_inicial}")
print(f"Registro de gastos y ahorros: {registro}")
