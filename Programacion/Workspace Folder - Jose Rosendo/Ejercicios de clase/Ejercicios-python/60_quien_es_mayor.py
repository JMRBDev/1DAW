# Diseña un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda. Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.

edad1 = int(input("Introduce la edad de la primera persona: "))
edad2 = int(input("Introduce la edad de la segunda persona: "))

if edad1 < edad2:
    print("La primera persona es más joven que la segunda.")
elif edad1 == edad2:
    print("Las dos personas tienen la misma edad.")
else:
    print("La segunda persona es más joven que la primera.")