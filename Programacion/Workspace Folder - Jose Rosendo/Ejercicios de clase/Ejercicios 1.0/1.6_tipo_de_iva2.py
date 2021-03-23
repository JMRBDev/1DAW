# Pide importe final, clacula e imprime el IVA pagado y el importe sin IVA. Suponemos que el tipo de IVA es del 10%.

importeFinal = float(input("Importe final del artículo: "))
tipoIva = float(0.10)

ivaPagado = importeFinal-importeFinal*tipoIva

importeSinIva = importeFinal-ivaPagado

print("El IVA pagado es",ivaPagado, "€.")
print("El importe sin IVA es", importeSinIva, "€.")