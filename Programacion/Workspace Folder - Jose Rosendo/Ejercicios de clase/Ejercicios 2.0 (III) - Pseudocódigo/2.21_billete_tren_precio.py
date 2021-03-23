#Determinar el precio de un billete de ida y vuelta en tren, conociendo la distancia a recorrer y sabiendo que si el número de días de estancia es superior a siete y la distancia superior a 800 km el billete tiene una reducción del 30%. El precio por kilómetro es de 10€.

variable precioKm = 10
variable distancia = introduccion numero por teclado
variable dias = introduccion numero por teclado

precioInicial = precioKm*distancia
precioTotal = entero

si distancia es mayor que 800 y dias es mayor a 7
    precioTotal += 30*100/precioTotal
    imprimir por pantalla precioTotal
en cualquier otro caso
    imprimir precioInicial