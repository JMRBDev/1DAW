# Pide peso en kg y altura en m. Calcula el IMC (peso/altura^2)

peso = float(input("Introduce tu peso: "))
altura = float(input("Introduce tu altura: "))

print("Tu IMC es:",peso/(altura**2))