# Diseña un programa Python que lea un carácter cualquiera desde el teclado, y muestre el mensaje "Es una MAYÚSCULA" cuando el carácter sea una letra mayúscula y el mensaje "Es una MINÚSCULA" cuando sea una minúscula. En cualquier otro caso, no mostrará mensaje alguno. (Considera ́Únicamente letras del alfabeto inglés.)

letra = input("Introduce una letra: ")

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in letras:
    if letra == i:
        print("Es una MAYÚSCULA")
    elif letra == i.lower():
        print("Es una MINÚSCULA")
    else:
        pass