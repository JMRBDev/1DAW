    # Jose Rosendo

def rgb(cmyk):
    r = 255 * (1-float(cmyk[0])/100) * (1-float(cmyk[3])/100)
    g = 255 * (1-float(cmyk[1])/100) * (1-float(cmyk[3])/100)
    b = 255 * (1-float(cmyk[2])/100) * (1-float(cmyk[3])/100)
    rgbList = []
    #return f"{round(r)} {round(g)} {round(b)}\n"
    for i in round(r), round(g), round(b):
        rgbList.append(i)
    
    return rgbList

def cmyk(rgb):
    rc = float(rgb[0])/255
    gc = float(rgb[1])/255
    bc = float(rgb[2])/255
    k = 1-max(rc, gc, bc)
    c = 100 * (1-rc-k) / (1-k)
    m = 100 * (1-gc-k) / (1-k)
    y = 100 * (1-bc-k) / (1-k)
    cmykList = []
    #return f"{round(c)} {round(m)} {round(y)} {round(k*100)}\n"
    for i in round(c), round(m), round(y), round(k*100):
        cmykList.append(i)

    return cmykList

if __name__ == "__main__":
    while True:
        userInputRaw = input("Introduzca un color (salir): ")
        userInput = userInputRaw.split(" ")

        if len(userInput) == 3:
            for i in userInput:
                if float(i) in range(0, 256):
                    isCorrect = True
                else:
                    isCorrect = False
                    print("Introduzca un valor válido.\n")
                    break
            if isCorrect:
                print("Color CMYK: ",cmyk(userInput),"\n")

        elif len(userInput) == 4:
            for i in userInput:
                if float(i) in range(0, 101):
                    isCorrect = True
                else:
                    isCorrect = False
                    print("Introduzca un valor válido.\n")
                    break
            if isCorrect:
                print("Color RGB: ",rgb(userInput),"\n")

        elif userInputRaw.lower() == "salir":
            exit()

        else:
            print("Introduzca un valor válido.\n")