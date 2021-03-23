# Adivinar el resultado del programa introduciendo 3, 8 y 13.

try:
    a = int(input("numero: "))
    p = True
    for n in range(2,a):
        if not a%n:
            p = False
            break
    if p:
        print("si")
    else:
        print("no")

except:
    print("no es numero")

# 3: si.
# 8: no.
# 13: si.