def alphabet_position(text):

    solucion = []

    for i in text.lower():
        if i <= "z" and i >= "a":
            solucion.append(ord(i)-96)

    solucionFinal = " ".join(map(str, solucion))
    return solucionFinal
            
print(alphabet_position("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))