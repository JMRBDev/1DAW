# Crear un programa para gestionar una agenda de contactos. El funcionamiento será el siguiente:
# • El programa pedirá introducir algo por teclado:
# o Si se introduce un número de teléfono comprobará si existe, si es así mostrará a quién pertenece. Si no
# existe pedirá el nombre del contacto para darlo de alta.
# o Si se introduce un contacto debe comprobar si existe, si es así mostrará el número de teléfono. Si no
# existe pedirá el número de teléfono para darlo de alta.
# • Debe reconocer números de teléfono con espacios entre los dígitos o no y con el símbolo + al principio para
# indicar prefijo de país.
# • Los nombres deben comenzar por letras y pueden contener números y caracteres especiales imprimibles.
# • Comandos especiales:
# o adios: Sale del programa
# o listado: Muestra el listado completo de contactos ordenados por nombre
# o consulta texto: Muestra el listado de los contactos que contengan texto o “Ningún contacto” si no hubiera
# ninguno.

import string

contacts = {"Test1":1111, "Test2":2222, "Test3":3333}

def showContacts(userInput):
    if userInput == "listado":
        return contacts
    else:
        return contacts[userInput]

def showContactsByPhone(userInput):
    for i, key in enumerate(list(contacts.items())):
        if str(key[1]) == str(userInput):
            itExists = True
            break
        else:
            itExists = False
    
    if itExists:
        return "{}: {}".format(key[0], key[1])
    else:
        contactName = input(f"\nNombre para el contacto {userInput}: ")
        return newContactByPhone(userInput, contactName)

def showContactsPrefix(userInput):
    userInputNoPrefix = userInput[3::]
    for i, key in enumerate(list(contacts.items())):
        if str(key[1]) == str(userInputNoPrefix):
            itExists = True
            break
        else:
            itExists = False
    
    if itExists:
        return "{}: {}".format(key[0], key[1])
    else:
        contactName = input(f"\nNombre para el contacto {userInput}: ")
        return newContactByPhone(userInputNoPrefix, contactName)

def newContactByName(userInput, contactPhone):
    contacts[userInput] = contactPhone
    return "Contacto {} añadido".format(userInput)

def newContactByPhone(userInput, contactName):
    contacts[contactName] = userInput
    return "Contacto {} añadido".format(userInput)

if __name__ == "__main__":
    while True:
        userInput = input("Input: ")

        if userInput == "listado":
            print(showContacts(userInput))

        elif userInput == "adios":
            print("Chao")
            exit()

        elif userInput == "consulta texto":
            if len(contacts) == 0:
                print("Ningún contacto")
            else:
                print(showContacts("listado"))

        elif userInput[0] in string.ascii_letters:
            if userInput in contacts:
                print(f"{userInput}:", showContacts(userInput),"\n")
            else:
                contactPhone = input(f"\nNúmero para el contacto {userInput}: ")
                print(newContactByName(userInput, contactPhone), "\n")
        
        elif userInput[0] not in string.ascii_letters and userInput[0].count("+") == 0:
            print(showContactsByPhone(userInput), "\n")
        
        elif userInput[0] not in string.ascii_letters and userInput[0].count("+") == 1:
            print(showContactsPrefix(userInput), "\n")