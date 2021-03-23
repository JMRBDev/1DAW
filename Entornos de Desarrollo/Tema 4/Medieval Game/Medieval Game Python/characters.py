from items import *

# Characters
class Character:
    charName = str
    charAlias = str
    charType = str

    def __init__(self, charName, charAlias, charType):
        self.charName = charName
        self.charAlias = charAlias
        self.charType = charType

class Farmer(Character):
    foodGenerationRate = float

    def __init__(self):
        pass

    def generateFood(self):
        foodCount += 1

    def haveChildren(self):
        childrenCount += 1

class Handcrafter(Character):
    def __init__(self):
        pass

    def craftArmor(self):
        pass

    def craftWeapon(self):
        pass

    def haveChildren(self):
        pass

class Soldier(Character):
    kind = str
    armor = str
    weapon = str

    def __init__(self, kind, armor, weapon):
        self.kind = kind
        self.armor = armor
        self.weapon = weapon

    def fight(self):
        pass

class Priest(Character):
    def __init__(self):
        pass

    def waste(self):
        pass

class Innkeeper(Character):
    numHandcrafters = int
    tavernName = str

    def __init__(self):
        pass

    def cookHydrohoney(self):
        pass