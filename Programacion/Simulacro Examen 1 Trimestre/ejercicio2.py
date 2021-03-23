diccionario = {"Lounganis":0, "Xiao":0, "Perez":0, "Gordon":0, "Chan":0}

def votaciones(lista):
    entrada = input("¿Qué desea hacer? ")
    global diccionario

    if entrada.lower() == "salir":
        exit()

    elif entrada.lower() == "saltos":
        for k , v in diccionario.items(): # iterating freqa dictionary
            print(f'{k:<4} {v}')

    elif entrada.lower() == "clasificacion":
        pass

    else:
        entradaList = entrada.split(" ")
        if len(entradaList) == 6:
            for i in entradaList:
                if entradaList.count(i) == 1:
                    continue
                else:
                    print("Introducción inválida.")
                    break
            for i in entradaList[1::]:
                if int(i) <= 40:
                    if "lounganis" in entrada.lower():
                        diccionario["Lounganis"] = entradaList[1::]
                        break
                    elif "xiao" in entrada.lower():
                        diccionario["Xiao"] = entradaList[1::]
                        break
                    elif "perez" in entrada.lower():
                        diccionario["Perez"] = entradaList[1::]
                        break
                    elif "gordon" in entrada.lower():
                        diccionario["Gordon"] = entradaList[1::]
                        break
                    elif "chan" in entrada.lower():
                        diccionario["Chan"] = entradaList[1::]
                        break
                    else:
                        print("Introducción inválida.")
                else:
                    print("Introducción inválida.")
                    break

if __name__ == "__main__":
    while True:
        votaciones(diccionario)