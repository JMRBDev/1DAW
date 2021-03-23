class File:
    """Crea instancias de tipo File. Se encarga de corregir posibles errores en apertura y cierre de ficheros
    
    Returns:
        File -- Fichero con el que se puede trabajar cómodamente
    """
    def __init__(self, filename, method):
        """Composición inicial de cualquier objeto File
        
        Arguments:
            filename {str} -- Nombre del fichero que se está creando
            method {str} -- Write or read (escritura o lectura - w/r)
        """
        self.file = open(filename, method)

    def __enter__(self):
        """Abre el archivo creado para poder trabajar con él
        
        Returns:
            File -- Fichero con el que se puede trabajar cómodamente
        """
        return self.file

    def __exit__(self, type, value, traceback):
        """Cierra el fichero para que no se quede abierto y cause problemas en futuras ejecuciones
        
        Arguments:
            type {type} -- Tipo de fichero que se está cerrando (necesario para el control de Exceptions)
            value {value} -- Valor del fichero que se está cerrando (necesario para el control de Exceptions)
            traceback {traceback} -- Traceback que se devuelve en caso de Exception (necesario para el control de Exceptions)
        """
        self.file.close()


def run():
    """Ejecución inicial del programa
    
    Returns:
        String -- Contenido del archivo de salida
    """
    input_file = File("input_file.txt", "r")
    output_file = File("output_file.txt", "w")

    print("El Script se ha ejecutado con éxito.")

    return showResults(orderProcs(readProcs(input_file)), output_file)

def readProcs(input_file):
    """Lee los procesos almacenados en el archivo de entrada / inserción de datos
    
    Arguments:
        input_file {File} -- Archivo del cuál se van a leer los datos de los procesos a ordenar
    
    Returns:
        List -- Lista de procesos válidos sin ordenar
    """
    procs = []

    with input_file as input_f:
        for line in input_f:
            proc_data = str(line).rstrip().split("/")

            if proc_data \
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
                    
                    if not existing:
                        procs.append(proc_data)
                    else:
                        print("El proceso {} ya existe, no se añadirá a la lista de procesos.".format("/".join(proc_data)))

            else:
                print("El proceso {} es erróneo, no se añadirá a la lista de procesos.\n".format("/".join(proc_data)))
    
    return procs

def orderProcs(procs_list):
    """Ordena los procesos de la lista de procesos desordenada según el tiempo de llegada
    
    Arguments:
        procs_list {List} -- Lista de procesos desordenados, anteriormente leídos del archivo de entrada / inserción de datos
    
    Returns:
        List -- Lista de procesos oordenados según el tiempo de llegada (FIFO)
    """
    procs_list.sort(key = lambda x: x[1])
    return procs_list

def showResults(procs_list, output_file):
    """Escribe los resultados en el archivo de salida
    
    Arguments:
        procs_list {List} -- Lista de procesos ordenados anteriormente según el tiempo de llegada
        output_file {File} -- Archivo de salida / muestra de datos
    """
    results = [["NOMBRE", "LLEGADA", "CPU"]]

    with output_file as output_f:

        for result in results:
            for part in result:
                output_f.write(str(part) + "\t")
        output_f.write("\n")
        for proc in procs_list:
            for part in proc:
                output_f.write(str(part) + "\t")
            output_f.write("\n")
        result_string = []
        for proc in procs_list:
            for data in range(int(proc[2])):
                result_string.append(proc[0][0])

        output_f.write("\n\nDiagrama de Grantt: ")
        for result in result_string:
            output_f.write(str(result) + " ")


if __name__ == "__main__":
    run()