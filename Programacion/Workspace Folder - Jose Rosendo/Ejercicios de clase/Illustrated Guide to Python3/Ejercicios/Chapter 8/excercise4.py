# Determine if 1800, 1900, 1903, 2000 and 2002 where leap years.

years = [1800, 1900, 1903, 2000, 2002]

for i in years:
    if (i%4 == 0 and i%100 != 0) or (i%4 == 0 and i%100 == 0 and i%400 == 0):
        print("El año", i, "es bisiesto.")
    else:
        pass