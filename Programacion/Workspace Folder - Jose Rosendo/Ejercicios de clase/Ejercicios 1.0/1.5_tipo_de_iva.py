# Pide el importe final y el tipo de IVA de un artículo, imprime el precio final

importe = float(input("¿Cuál es el importe del artículo? "))
iva = float(input("¿Cuál es el IVA a aplicar? "))/100

print("El importe del artículo con IVA es de:", importe+(iva*importe), "€.")