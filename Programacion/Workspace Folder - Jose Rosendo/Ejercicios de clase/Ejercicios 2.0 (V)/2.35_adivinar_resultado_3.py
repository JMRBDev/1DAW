# Adivinar el resultado del programa introduciendo 3, aa y 6

try:
    n = int(input("numero: "))

except:
    n = 3

a = 1
for i in range(n, 0, -1):
    print(" "*i+"*"*a)
    a += 2
print(" "*(n-1)+"*"*3)


# 3: *
#   ***
#  *****
#   ***

# aa: *
#    ***
#   *****
#    ***

# 6:   *
#     ***
#    *****
#   *******
#  *********
# ***********
#     ***