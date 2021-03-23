# Se desea realizar unas estadísticas de las alturas de los alumnos. Cuando se introduzca una altura 0, debe parar de solicitar alturas y mostrar los resultados.

variable edad = entero
variable masUnoSetenta = flotante
variable entreUnoSesentaYUnoSetenta = flotante
variable entreUnoCincuentaYUnoSesenta = flotante
variable menosDeUnoCincuenta = flotante

mientras que la condicion sea cierta (while True)
    edad = introduccion numero por teclado
    si edad es distinto de 0
        si edad es mayor que 1.7
            masUnoSetenta aumentar 1
        en otro caso si edad está entre 1.6 y 1.7 incluyendo 1.7
            entreUnoSesentaYUnoSetenta aumentar 1
        en otro caso si edad está entre 1.5 y 1.6 incluyendo 1.6
            entreUnoCincuentaYUnoSesenta aumentar 1
        en otro caso si edad es menor que 1.5 incluyendo 1.5
            menosDeUnoCincuenta aumentar 1
    en otro caso si edad es igual a 0
        imprimir por pantalla masUnoSetenta, entreUnoSesentaYUnoSetenta, entreUnoCincuentaYUnoSesenta, menosDeUnoCincuenta
        terminar ejecución