import sys

if len(sys.argv) > 1:
    ordered = []
    sys.argv.pop(0)

    while sys.argv[0] > range(len(sys.argv) -1):
        for i in range(len(sys.argv) - 1):
            if sys.argv[i] > sys.argv[i + 1]:
                sys.argv[i], sys.argv[i + 1] = sys.argv[i + 1], sys.argv[i]
            else:
                continue
    
    print(sys.argv)

else:
    print("Introduce una lista de números válida.")