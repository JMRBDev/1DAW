# Realiza un programa que calcule el desglose en billetes y monedas de una cantidad exacta de euros. Hay billetes de 500, 200, 100, 50, 20, 10 y 5 ¤ y monedas de 2 y 1 ¤. Por ejemplo, si deseamos conocer el desglose de 434 ¤, el programa mostrar´a por pantalla el siguiente resultado:

cantidad = int(input("Introduce la cantidad total de dinero: "))
billetes = [500, 200, 100, 50, 20, 10, 5]
monedas = [2, 1]

resto = cantidad


for i in billetes:    
    if i < resto:
        if resto/i >= 1:
            print("Hay", int(resto/i), "billetes de", i, "euros")
            resto = int(resto%i)

for i in monedas:    
    if i <= resto:
        if resto/i >= 1:
            print("Hay", int(resto/i), "monedas de", i, "euros")
            resto = int(resto%i)