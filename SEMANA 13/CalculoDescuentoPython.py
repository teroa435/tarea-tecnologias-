# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calculamos el descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    # Devolvemos el monto del descuento
    return descuento

# Programa principal
# Primera llamada a la función, solo con el monto total (usando el porcentaje de descuento por defecto)
monto_total_1 = 1000  # Ejemplo de monto total
descuento_1 = calcular_descuento(monto_total_1)
monto_final_1 = monto_total_1 - descuento_1

# Segunda llamada a la función, con el monto total y un porcentaje de descuento diferente
monto_total_2 = 1500  # Ejemplo de monto total
porcentaje_descuento_2 = 15  # Ejemplo de porcentaje de descuento
descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
monto_final_2 = monto_total_2 - descuento_2

# Salida de los resultados
print(f"Compra 1:")
print(f"Monto total: ${monto_total_1}")
print(f"Descuento: ${descuento_1}")
print(f"Monto final a pagar: ${monto_final_1}\n")

print(f"Compra 2:")
print(f"Monto total: ${monto_total_2}")
print(f"Descuento: ${descuento_2}")
print(f"Monto final a pagar: ${monto_final_2}")
