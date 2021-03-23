    # Jose Rosendo

pacientes = {}
cita = {}

def mostrarListaEspera():
    for i in range(len(pacientes.keys())):
        prioridad = int(len(pacientes.keys())) - 1 + int(userInput[2]) - int(userInput[1])
        cita.update({list(pacientes.keys())[i]:prioridad})
        print(f"{i+1}.- {list(pacientes.keys())[i]} {prioridad}")

if __name__ == "__main__":
    while True:
        userInputRaw = input("¿Qué desea hacer?: ")
        userInput = userInputRaw.split(" ")

        if userInputRaw.lower() == "salir":
            exit()
        elif userInputRaw.lower() == "cita" and len(pacientes.keys()) > 0:
            print(f"Se atiende a {list(pacientes.keys())[0]}")
            pacientes.pop(list(pacientes.keys())[0])
            print(f"Espera media {len(list(pacientes.keys())*15)} minutos")
        else:
            pacientes.update({userInput[0]:{userInput[1]:userInput[2]}})
            mostrarListaEspera()