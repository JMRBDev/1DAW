# Traductor binario a decimal y viceversa.

def calculo(): #Función para poder ejecutar el programa indefinidamente

    operacion = input("¿Qué operación quieres hacer? 'Binario a Decimal' o 'Decimal a Binario':\n")
    potencia = 1 #Posicion en la que nos encontramos en el binario

    try:

        if operacion.lower() == "binario a decimal":
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

        if operacion.lower() == "decimal a binario":
            decimal = int(input("Introduce un número decimal: ")) #Introduce un número en decimal
            decimalInicial = decimal #Guarda el decimal para el resultado, para que no cambie
            resultado = [] #Define resultado como una lista
            while decimal >= 1: #Mientras que el decimal sea mayor o igual que 1,
                resultado.append(decimal%2) #Añade el resto del decimal entre 2 al resultado
                decimal = decimal//2 #Divide el resultado entre 2 para seguir con la ejecución
            print(decimalInicial, " en binario es ", *resultado[::-1], ".\n\n", sep="")

    except ValueError:
        print("El valor introducido es incorrecto\n")



while True: #Ejecución indefinida del programa
    calculo()