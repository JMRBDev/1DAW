#Solicitar por teclado una cantidad de dinero con decimales hasta los céntimos y calcular el cambio en billetes y monedas de curso legal.

cantidad = float(input("Introduce la cantidad total de dinero: "))
billetes = [500, 200, 100, 50, 20, 10, 5]
monedas = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

resto = round(cantidad, 2)


for i in billetes:    
    if i <= resto:
        if resto/i >= 0:
            print("Hay", int(resto/i), "billetes de", i, "euros")
            resto = float(round(resto%i, 2))

for i in monedas:    
    if i <= resto:
        if resto/i >= 0:
            print("Hay", int(resto/i), "monedas de", i, "euros")
            resto = float(round(resto%i, 2))




#Pseudocódigo

#Pedir cantidad de dinero en euros y céntimos
#Listar los billetes y las monedas en curso

#Para todos los billetes, si el billete es menor o igual que la cantidad de dinero que tengo,
#Si la cantidad de dinero que tengo entre el billete en cuestión es mayor o igual a 0,
#Imprimir que hay X billetes de esa cantidad y cambiar la cantidad por la cantidad restante.

#Para todas las monedas, si la moneda es menor o igual que la cantidad de dinero que tengo,
#Si la cantidad de dinero que tengo entre la moneda en cuestión es mayor o igual a 0,
#Imprimir que hay X monedas de esa cantidad y cambiar la cantidad por la cantidad restante.