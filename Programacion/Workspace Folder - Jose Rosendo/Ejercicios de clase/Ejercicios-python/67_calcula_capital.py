# Un capital de C euros a un interés del x por cien anual durante n años se convierte en C ·(1 + x/100)n euros. Diseña un programa Python que solicite la cantidad C y el interés x y calcule el capital final sólo si x es una cantidad positiva.

capitalInicial = int(input("Introduce la cantidad inicial: "))
interes = float(input("Introduce el interés anual: "))
anos = int(input("¿Cuántos años? "))

if interes > 0:
    capitalFinal = capitalInicial*(1+interes/100)**anos
    print("El capital final es de",capitalFinal,"euros.")
else:
    print("El interés es negativo")