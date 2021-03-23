# Detectar si un input es palíndromo

import sys
import string
import unicodedata

if len(sys.argv) > 1:
    myinput = sys.argv[1]
    isTrue = True

    mystring_normalized = unicodedata.normalize("NFKD", myinput.lower().replace(" ", "")).encode("ascii", "ignore").decode("ascii")
    slicedstring = mystring_normalized[len(mystring_normalized)::-1].lower()

    for letters in mystring_normalized:
        if letters in string.ascii_lowercase and mystring_normalized == slicedstring:
            isCorrect = True
        else:
            isCorrect = False
            break

    if isCorrect:
        print("{} es palíndromo.".format(myinput))
    else:
        print("{} no es palíndromo.".format(myinput))

else:
    print("Introduce una palabra o frase válida.")