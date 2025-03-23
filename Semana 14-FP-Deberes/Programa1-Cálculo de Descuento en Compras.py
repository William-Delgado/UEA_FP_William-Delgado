#UNIVERSIDAD ESTATAL AMAZONICA
#WILLIAM DELGADO
#FUNDAMENTOS DE PROGRAMACION
#Programa 1: Cálculo de Descuento en Compras

# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado al monto total de la compra.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Llamada 1: Usando el descuento predeterminado (10%)
monto_compra_1 = 1000
descuento_1 = calcular_descuento(monto_compra_1)
monto_final_1 = monto_compra_1 - descuento_1

print(f"Compra 1 - Monto total: ${monto_compra_1}")
print(f"Descuento aplicado: ${descuento_1}")
print(f"Monto final a pagar: ${monto_final_1}")
print()

# Llamada 2: Usando un descuento personalizado (20%)
monto_compra_2 = 2000
descuento_2 = calcular_descuento(monto_compra_2, 20)
monto_final_2 = monto_compra_2 - descuento_2

print(f"Compra 2 - Monto total: ${monto_compra_2}")
print(f"Descuento aplicado: ${descuento_2}")
print(f"Monto final a pagar: ${monto_final_2}")