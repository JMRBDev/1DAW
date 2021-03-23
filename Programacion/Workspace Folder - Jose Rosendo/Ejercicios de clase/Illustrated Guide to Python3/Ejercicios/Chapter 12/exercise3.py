# Create a list, names, with the names of people in a class. Write code to print 'The class is empty!' or 'Class has enrollments.', based on whether there are values in names. (See the tip in this chapter for details).

names = ["Jose", "Perico", "María", "Natalia", "Julio"]
isEmpty = True

if len(names) == 0:
    isEmpty = True
    print("The class is empty!")
else:
    isEmpty = False
    print("Class has enrollments.")
    