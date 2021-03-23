# Escribir una función que acepte una cadena por teclado y muestre la cuenta de los caracteres diferentes.

cad = input("Introduce una cadena de caracteres: ")
cad_list = {}

for i in cad:
    if i not in cad_list:
        cad_list[i] = cad.count(i)
    
for i in cad_list:
    print(cad_list[i], i, sep=" ", end=", ")