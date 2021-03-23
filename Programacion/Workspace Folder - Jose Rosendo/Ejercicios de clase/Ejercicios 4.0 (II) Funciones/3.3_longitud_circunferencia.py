# Calcula la longitud de una circunferencia

import math

def longitud(radio):

    return "La longitud de una circunferencia de radio {}cm y diámetro {}cm es de {}cm".format(radio, radio*2, radio*2*math.pi)

print(longitud(4))