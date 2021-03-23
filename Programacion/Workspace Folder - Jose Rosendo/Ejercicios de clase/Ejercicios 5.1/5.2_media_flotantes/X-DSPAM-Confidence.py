# Escribe un programa que pida el nombre de un archivo y después lo lea buscando líneas que tengan la forma:
# X-DSPAM-Confidence: 0.8475
# El programa debe extraer de esta línea el valor numérico flotante y calcular la media de todos los valores de este
# tipo en el archivo.

import sys

def average():
    nums = []
    with open(fileName, 'r', encoding='utf8') as f:
        for line in f:
            nums.append(line.rstrip("\n").split(" ")[1])

    print("Floats are:", *nums)

    for i in range(len(nums)):
        nums[i] = float(nums[i])

    return sum(nums) / len(nums)



if __name__ == "__main__":
    fileName = sys.argv[1]

    print("\nAverage float:", average())