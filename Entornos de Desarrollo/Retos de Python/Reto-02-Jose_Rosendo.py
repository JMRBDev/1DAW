# -*- coding: utf-8 -*-
# En este texto hay 7 países escondidos. Encuéntralos.
import re
import unicodedata
import string

texto="Por tu galante compañía no ruega más Norita. Liada está: vende y cobra sillas. No se estanca nada y piensa en su buen vivir antes que en otra cosa. ¿Y sabes qué? ¡No se deja ponderar!"


paises = ["Afganistán", "Albania", "Alemania", "Andorra", "Angola", "Antigua y Barbuda", "Arabia Saudita", "Argelia", "Argentina", "Armenia", "Australia", "Austria", "Azerbaiyán", "Bahamas", "Bangladés", "Barbados", "Baréin", "Bélgica", "Belice", "Benín", "Bielorrusia", "Birmania", "Bolivia", "Bosnia y Herzegovina", "Botsuana", "Brasil", "Brunéi", "Bulgaria", "Burkina Faso", "Burundi", "Bután", "Cabo Verde", "Camboya", "Camerún", "Canadá", "Catar", "Chad", "Chile", "China", "Chipre", "Ciudad del Vaticano", "Colombia", "Comoras", "Corea del Norte", "Corea del Sur", "Costa de Marfil", "Costa Rica", "Croacia", "Cuba", "Dinamarca", "Dominica", "Ecuador", "Egipto", "El Salvador", "Emiratos Árabes Unidos", "Eritrea", "Eslovaquia", "Eslovenia", "España", "Estados Unidos", "Estonia", "Etiopía", "Filipinas", "Finlandia", "Fiyi", "Francia", "Gabón", "Gambia", "Georgia", "Ghana", "Granada", "Grecia", "Guatemala", "Guyana", "Guinea", "Guinea ecuatorial", "Guinea-Bisáu", "Haití", "Honduras", "Hungría", "India", "Indonesia", "Irak", "Irán", "Irlanda", "Islandia", "Islas Marshall", "Islas Salomón", "Israel", "Italia", "Jamaica", "Japón", "Jordania", "Kazajistán", "Kenia", "Kirguistán", "Kiribati", "Kuwait", "Laos", "Lesoto", "Letonia", "Líbano", "Liberia", "Libia", "Liechtenstein", "Lituania", "Luxemburgo", "Macedonia del Norte", "Madagascar", "Malasia", "Malaui", "Maldivas", "Malí", "Malta", "Marruecos", "Mauricio", "Mauritania", "México", "Micronesia", "Moldavia", "Mónaco", "Mongolia", "Montenegro", "Mozambique", "Namibia", "Nauru", "Nepal", "Nicaragua", "Níger", "Nigeria", "Noruega", "Nueva Zelanda", "Omán", "Países Bajos", "Pakistán", "Palaos", "Panamá", "Papúa Nueva Guinea", "Paraguay", "Perú", "Polonia", "Portugal", "Reino Unido", "República Centroafricana", "República Checa", "República del Congo", "República Democrática del Congo", "República Dominicana", "Ruanda", "Rumanía", "Rusia", "Samoa", "San Cristóbal y Nieves", "San Marino", "San Vicente y las Granadinas", "Santa Lucía", "Santo Tomé y Príncipe", "Senegal", "Serbia", "Seychelles", "Sierra Leona", "Singapur", "Siria", "Somalia", "Sri Lanka", "Suazilandia", "Sudáfrica", "Sudán", "Sudán del Sur", "Suecia", "Suiza", "Surinam", "Tailandia", "Tanzania", "Tayikistán", "Timor Oriental", "Togo", "Tonga", "Trinidad y Tobago", "Túnez", "Turkmenistán", "Turquía", "Tuvalu", "Ucrania", "Uganda", "Uruguay", "Uzbekistán", "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Yibuti", "Zambia", "Zimbabue"]

# Eliminar símbolos de la String texto
texto = re.sub(r'[^\w]', ' ', texto)
# Juntar todas las palabras de la String texto y pasarlas a minúsculas
textoJunto = ''.join(texto).replace(' ', '').lower()

# Eliminar todas las tildes de la String textoJunto
textoNfkd = unicodedata.normalize('NFKD', textoJunto)

# Crear lista resultado para mejorar el formateo de cómo se muestran los datos en la terminal
# y que sea más fácil controlar como se muestran los países (comodidad)
resultado = []

# Bucle para ver si cada país de la lista de todos los paises del mundo se encuentra en la String textoNfkd
for pais in paises:
    # La condición es un poco extraña porque se quitan las tildes de cada país aquí dentro y así me ahorro una variable
    # y es todo más sencillo (comodidad y supongo que ahorro en cuanto a almacenamiento en memoria por tener una variable menos 👀)
    if ''.join(x for x in unicodedata.normalize('NFKD', pais) if x in string.ascii_letters).lower() in textoNfkd:
        # En caso de que el país esté en la String textoNfkd, se añade a la lista resultado
        resultado.append(pais)

# Mostrar los paises del resultado en una fString separados por comas y con una frase como introducción
print(f'Los países del texto son: {", ".join(resultado)}')