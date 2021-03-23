def addNumbers():
    nums = []
    with open('numeros.txt', 'r', encoding='utf8') as f:
        for line in f:
            nums.append(int(line))

    return sum(nums)

print(addNumbers())
