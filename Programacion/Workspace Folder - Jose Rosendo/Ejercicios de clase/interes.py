# Haz un programa que pida al usuario una cantidad de euros, una tasa de inter´es y un n´umero de a˜nos. Muestra por pantalla en cu´anto se habr´a convertido el capital inicial transcurridos esos a˜nos si cada a˜no se aplica la tasa de inter´es introducida. Recuerda que un capital de C euros a un inter´es del x por cien durante n a˜nos se convierten en C · (1 + x/100)n euros. (Prueba tu programa sabiendo que una cantidad de 10 000 ¤ al 4.5% de inter´es anual se convierte en 24 117.14 ¤ al cabo de 20 a˜nos.)

euros = int(input("Introduce una cantidad de euros: "))
interes = float(input("Introduce la tasa de interés: "))
anos = int(input("Introduce un número de años: "))

capital = euros*(1+interes/100)**anos

print(round(capital, 2)) # Redondea a 2 decimales