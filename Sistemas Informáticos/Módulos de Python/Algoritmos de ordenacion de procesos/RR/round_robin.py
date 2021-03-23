def run():
    return showResults(orderProcs(createProcs()))

def createProcs():
    procs = []

    while True:
        proc_name_input = input("Introduce los datos del proceso (Nombre/Llegada/CPU - 0 para terminar): ")
        proc_data = proc_name_input.split("/")
        if proc_name_input == "0":
            break
        elif proc_name_input.split("/") \
             and len(proc_data) == 3 \
             and proc_data[0].isalpha() \
             and proc_data[1].isdigit() \
             and proc_data[2].isdigit():
            if len(procs) == 0:
                procs.append(proc_data)
            else:
                for proc in procs:
                    if proc[0] != proc_data[0]:
                        existing = False
                    else:
                        existing = True
                        break
                if existing:
                    print("El proceso ya existe, inténtelo de nuevo.")
                else:
                    procs.append(proc_data)
        else:
            print("Datos de proceso erróneos, inténtelo de nuevo.\n")

    return procs

def orderProcs(procs_list):
    procs_list.sort(key = lambda x: x[1])
    return procs_list

def showResults(procs_list):
    results = [["NOMBRE", "LLEGADA", "CPU", "INICIO", "FIN", "RETORNO", "ESPERA"]]
    for proc in procs_list:
        results.append(proc)
    for result in results:
        print(*result, sep="\t")
    print("\n")
    result_string = []
    for result in results[1:]:
        for j in range(int(result[2])):
            result_string.append(result[0])
    
    print("Diagrama de Grant:", *result_string)

if __name__ == "__main__":
    run()