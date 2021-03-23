# Solicitar un número en decimal por teclado y convertirlo a binario. Si no se conoce la forma de hacerlo, localizar el algoritmo en internet.

potencia = 1 #Posicion en la que nos encontramos en el binario

binario = input("Introduce un número binario: ") #Introduce un número en binario
for i in binario:
    binarioOrdenado = binario[::-1] #Ordena el número al revés
    resultado = 0 #Define resultado como 0
    for i in binarioOrdenado: #Para cada caracter en el número:
        if i == "0": #Si el caracter es 0, obvialo
            pass
        elif i == "1": #Si el caractes es 1,
            resultado += potencia #Sumamos la potencia al resultado
        potencia = potencia*2 #Potencia*2 para aumentar la posicion en 1
    break

print(binario, " en decimal es ", resultado, ".\n\n", sep="")


#Definir la posición en la que estamos contando
#Pedir por teclado el número binario
#Para cada carácter del número binario,
#Ordenar el número del revés en una variable nueva
#Crear variable 0 para incrementarla luego
#Para cada carácter en el número binario ordenado del revés,
#Si el carácter es igual que 0,
#No hacer nada y pasar a la siguiente condición
#En otro caso, si el carácter es igual que 1,
#Sumar al resultado, la potencia de esta iteración
#Incrementar potencia multiplicándolo *2
#Imprimir por pantalla el resultado del binario en decimal
#
#
#










