# Jose Rosendo

from math import pow
from tabulate import tabulate

class Calculadora:

	num1 = 0
	num2 = 0

	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

	def suma(self):
		return "{} + {} = {}".format(self.num1, self.num2, self.num1 + self.num2)

	def resta(self):
		return "{} - {} = {}".format(self.num1, self.num2, self.num1 - self.num2)

	def multiplicacion(self):
		return "{} * {} = {}".format(self.num1, self.num2, self.num1 * self.num2)

	def division(self):
		return "{} / {} = {}".format(self.num1, self.num2, self.num1 / self.num2)

	def resto(self):
		return "El resto de {} / {} es {}".format(self.num1, self.num2, self.num1 % self.num2)

	def porcentaje(self):
		return "El {}% de {} es {}".format(self.num1, self.num2, self.num1*100/self.num2)

	def potencia(self):
		return "{}^{} = {}".format(self.num1, self.num2, self.num1**self.num2)
	
	def raiz(self):
		return "La raíz {} de {} es {}".format(self.num1, self.num2, pow(self.num2,1/self.num1))

eleccion = 1
while eleccion != 0:
	print(tabulate([["0.-", "Salir"], ["1.-", "Sumar"], ["2.-", "Restar"], ["3.-", "Multiplicar"], ["4.-", "Dividir"], ["5.-", "Resto"], ["6.-", "Porcentaje"], ["7.-", "Potencia"], ["8.-", "Raiz"]], headers=["Número", "Opción"], tablefmt="orgtbl"))
	eleccion = int(input("Selecciona una opción: "))

	if eleccion == 1:
		MiCalculadora = Calculadora(float(input("Primer valor: ")), float(input("Segundo valor: ")))
		resultado = MiCalculadora.suma()
		print(resultado, "\n")
	elif eleccion == 2:
		MiCalculadora = Calculadora(float(input("Primer valor: ")), float(input("Segundo valor: ")))
		resultado = MiCalculadora.resta()
		print(resultado, "\n")
	elif eleccion == 3:
		MiCalculadora = Calculadora(float(input("Primer valor: ")), float(input("Segundo valor: ")))
		resultado = MiCalculadora.multiplicacion()
		print(resultado, "\n")
	elif eleccion == 4:
		MiCalculadora = Calculadora(float(input("Primer valor: ")), float(input("Segundo valor: ")))
		resultado = MiCalculadora.division()
		print(resultado, "\n")
	elif eleccion == 5:
		MiCalculadora = Calculadora(float(input("Primer valor: ")), float(input("Segundo valor: ")))
		resultado = MiCalculadora.resto()
		print(resultado, "\n")
	elif eleccion == 6:
		MiCalculadora = Calculadora(float(input("Primer valor: ")), float(input("Segundo valor: ")))
		resultado = MiCalculadora.porcentaje()
		print(resultado, "\n")
	elif eleccion == 7:
		MiCalculadora = Calculadora(float(input("Base: ")), float(input("Exponente: ")))
		resultado = MiCalculadora.potencia()
		print(resultado, "\n")
	elif eleccion == 8:
		MiCalculadora = Calculadora(float(input("Radicando: ")), float(input("Índice: ")))
		resultado = MiCalculadora.raiz()
		print(resultado, "\n")