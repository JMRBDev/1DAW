#  Crear una función que devuelva el número de dígitos necesarios para expresar un número en binario.

def cantidad(numero_dec):
        numero_bin = bin(numero_dec).replace("0b", "")
        contador = 0

        for i in numero_bin:
                contador +=1
        
        return "Hacen falta {} dígitos para representar{} en binario.".format(contador, numero_dec)

print(cantidad(64))