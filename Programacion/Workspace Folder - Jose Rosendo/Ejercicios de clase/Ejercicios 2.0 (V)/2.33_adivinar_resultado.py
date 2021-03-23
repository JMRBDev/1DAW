# Adivina el resultado del programa introduciendo 2000, 2010, 2012 y 2100.

try:
    a = int(input("numero: "))
    if not a%400 or (not a%4 and a%100):
        print("si")
    else:
        print("no")
    print(a%400, a%4, a%100)

except:
    print("no es numero")

# 2000: si.
# 2010: no.
# 2012: si.
# 2100: no.