 # Haz un programa que haga una lista. Que pida un número de palabras, y añada esa cantidad a la lista.

numeroPalabras = int(input("Número de palabras que tendrá la lista: "))
listaPalabras = []

if numeroPalabras < 0:
    print("El número es menor que cero.")
    exit
else:
    for i in range(numeroPalabras):
        palabra = input("Introduce una palabra: ")
        listaPalabras.append(palabra)
    
    for x in listaPalabras:
        print(x)