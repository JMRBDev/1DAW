try:
    eleccion = input("¿Qué operación quieres realizar? ")
    x = float(input("Introduce un número: "))
except ValueError:
    print("Error. Los datos introducidos no son correctos.")
    exit()

def raiz(x):
    r = x
    t = 0
    while t!= r:
        t = r
        r = 0.5*((x/r)+r)
    
    return r

def cuadrado(x):
    return x*x


if eleccion == "raiz":
    print(raiz(x))
elif eleccion == "cuadrado":
    print(cuadrado(x))
else:
    print("La operación que desea realizar no existe.")