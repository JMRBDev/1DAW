# Diseñar un programa que a partir de una fecha introducida por teclado con el formato día, mes, año, se obtenga la fecha del día siguiente.

variable fechaDia = introduccion numero por teclado
variable fechaMes = introduccion numero por teclado
variable fechaAño = introduccion numero por teclado

si fechaMes es igual a enero
    si fechaDia es mayor que 31
        imprimir por pantalla: Introduce una fecha válida
    en caso de que fechaDia sea igual a 31
        fechaDia = 1
        fechaMes = febrero
    en cualquier otro caso
        imprimir por pantalla: mañana es fechaDia+1, de fechaMes, de fechaAño

si fechaMes es igual a febrero
    si fechaDia es mayor que 28
        imprimir por pantalla: Introduce una fecha válida
    en caso de que fechaDia sea igual a 28
        fechaDia = 1
        fechaMes = marzo
    en cualquier otro caso
        imprimir por pantalla: mañana es fechaDia+1, de fechaMes, de fechaAño

si fechaMes es igual a marzo
    si fechaDia es mayor que 31
        imprimir por pantalla: Introduce una fecha válida
    en caso de que fechaDia sea igual a 31
        fechaDia = 1
        fechaMes = abril
    en cualquier otro caso
        imprimir por pantalla: mañana es fechaDia+1, de fechaMes, de fechaAño

si fechaMes es igual a abril
    si fechaDia es mayor que 30
        imprimir por pantalla: Introduce una fecha válida
    en caso de que fechaDia sea igual a 30
        fechaDia = 1
        fechaMes = mayo
    en cualquier otro caso
        imprimir por pantalla: mañana es fechaDia+1, de fechaMes, de fechaAño

si fechaMes es igual a mayo
    si fechaDia es mayor que 31
        imprimir por pantalla: Introduce una fecha válida
    en caso de que fechaDia sea igual a 31
        fechaDia = 1
        fechaMes = junio
    en cualquier otro caso
        imprimir por pantalla: mañana es fechaDia+1, de fechaMes, de fechaAño

si fechaMes es igual a junio
    si fechaDia es mayor que 30
        imprimir por pantalla: Introduce una fecha válida
    en caso de que fechaDia sea igual a 30
        fechaDia = 1
        fechaMes = julio
    en cualquier otro caso
        imprimir por pantalla: mañana es fechaDia+1, de fechaMes, de fechaAño

si fechaMes es igual a julio
    si fechaDia es mayor que 31
        imprimir por pantalla: Introduce una fecha válida
    en caso de que fechaDia sea igual a 31
        fechaDia = 1
        fechaMes = agosto
    en cualquier otro caso
        imprimir por pantalla: mañana es fechaDia+1, de fechaMes, de fechaAño

si fechaMes es igual a agosto
    si fechaDia es mayor que 31
        imprimir por pantalla: Introduce una fecha válida
    en caso de que fechaDia sea igual a 31
        fechaDia = 1
        fechaMes = septiembre
    en cualquier otro caso
        imprimir por pantalla: mañana es fechaDia+1, de fechaMes, de fechaAño

si fechaMes es igual a septiembre
    si fechaDia es mayor que 30
        imprimir por pantalla: Introduce una fecha válida
    en caso de que fechaDia sea igual a 30
        fechaDia = 1
        fechaMes = octubre
    en cualquier otro caso
        imprimir por pantalla: mañana es fechaDia+1, de fechaMes, de fechaAño

si fechaMes es igual a octubre
    si fechaDia es mayor que 31
        imprimir por pantalla: Introduce una fecha válida
    en caso de que fechaDia sea igual a 31
        fechaDia = 1
        fechaMes = noviembre
    en cualquier otro caso
        imprimir por pantalla: mañana es fechaDia+1, de fechaMes, de fechaAño

si fechaMes es igual a noviembre
    si fechaDia es mayor que 30
        imprimir por pantalla: Introduce una fecha válida
    en caso de que fechaDia sea igual a 30
        fechaDia = 1
        fechaMes = diciembre
    en cualquier otro caso
        imprimir por pantalla: mañana es fechaDia+1, de fechaMes, de fechaAño

si fechaMes es igual a diciembre
    si fechaDia es mayor que 31
        imprimir por pantalla: Introduce una fecha válida
    en caso de que fechaDia sea igual a 31
        fechaDia = 1
        fechaMes = enero
        fechaAño = fechaAño+1
    en cualquier otro caso
        imprimir por pantalla: mañana es fechaDia+1, de fechaMes, de fechaAño