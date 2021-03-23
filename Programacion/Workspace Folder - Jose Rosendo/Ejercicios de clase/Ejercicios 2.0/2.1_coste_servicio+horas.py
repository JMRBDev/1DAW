# Dale 1.5 veces la tarifa horaria para las horas trabajadas que excedan 40

precioPorHora = float(input("¿Cuánto se cobra por hora? "))
horasTrabajadas = float(input("¿Cuántas horas se ha trabajado? "))
horasExcedidas = float
precioMayorCuarenta = precioPorHora*1.5

if horasTrabajadas >= 40:
    horasExcedidas=horasTrabajadas-40
    print("El importe total es de", (horasExcedidas*precioMayorCuarenta)+(40*precioPorHora), "euros.")
else:
    print("El importe total es de", horasTrabajadas*precioPorHora, "euros.")