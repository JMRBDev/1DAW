# Pide peso en kg, altura en m y género. Calcula el IMC con la fórmula (peso/altura^2) si no introduce género, y con la fórmula h(altura-100-((altura-150)/4)) o m(altura-100-((altura-150)/2)) para el peso ideal. Luego compara el peso ideal con el peso real para saber el sobre peso o el bajo peso

peso = float(input("Introduce tu peso: "))
alturaM = float(input("Introduce tu altura: "))
alturaCm = alturaM*100
genero = (input("Introduce tu género: "))
edad = int(input("Introduce tu edad: "))

listaEdad = {"19-24":"19 y 24","25-34":"20 y 25","35-44":"21 y 26","45-54":"22 y 27","55-64":"23 y 28","65 o más":"24 y 29"}

pesoIdeal = int

if edad >= 19 and edad <= 24:
    print("\nTu IMC debe estar entre", listaEdad["19-24"])
elif edad >= 25 and edad <= 34:
    print("\nTu IMC debe estar entre", listaEdad["25-34"])
elif edad >= 35 and edad <= 44:
    print("\nTu IMC debe estar entre", listaEdad["35-44"])
elif edad >= 45 and edad <= 54:
    print("\nTu IMC debe estar entre", listaEdad["45-54"])
elif edad >= 55 and edad <= 64:
    print("\nTu IMC debe estar entre", listaEdad["55-64"])
elif edad >= 65:
    print("\nTu IMC debe estar entre", listaEdad["65 o más"])
else:
    pass

if not genero:
    print("\nTu IMC es:",peso/(alturaM**2))

else:
    if genero.lower() == "hombre" or "varón" or "niño" or "masculino" or "chico":
        pesoIdeal = alturaCm-100-((alturaCm-150)/4)

    elif genero.lower() == "mujer" or "hembra" or "niña" or "femenino" or "chica":
        pesoIdeal = alturaCm-100-((alturaCm-150)/2)

    print("\nTu peso ideal es:",pesoIdeal)
    print("\nTu peso ideal dista",pesoIdeal-peso,"de tu peso actual\n")