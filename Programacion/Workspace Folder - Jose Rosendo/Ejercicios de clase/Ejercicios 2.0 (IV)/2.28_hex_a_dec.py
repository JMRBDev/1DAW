# Solicitar por teclado un número en hexadecimal y calcular su valor en decimal. Se debe comprobar la corrección de número introducido.

hexadecimal = input("Introduce un número hexadecimal: ") #Introduce un número en hexadecimal

hexad = int(hexadecimal, 16)

print(hexadecimal, " en decimal es ", hexad, ".\n\n", sep="")



#Pseudocódigo
#Pedir por teclado un número hexadecimal
#Pasarlo a decimal
#Imprimir por pantalla el resiltado