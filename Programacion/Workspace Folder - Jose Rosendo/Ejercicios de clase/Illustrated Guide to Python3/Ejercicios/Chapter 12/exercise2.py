# Create a variable, name, set to your name. Create another variable, second_half, that tests whether the name would be classified in the second half of the alphabet? What do you need to compare it to?

name = "jose"
second_half = False
dictionary = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k" ,"l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

dictionarySecondHalf = (dictionary[len(dictionary)//2:])

nameInList = list(name)

for i in dictionarySecondHalf:
    if nameInList[0] == i:
        second_half = True
    else:
        pass

print(second_half)