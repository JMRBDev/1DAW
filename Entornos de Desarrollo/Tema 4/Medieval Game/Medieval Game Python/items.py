foodCount = 0
childrenCount = 0

# Items

class Weapon:
    weaponName = str
    damage = float

    def __init__(self, weaponName, damage):
        self.weaponName = weaponName
        self.damage = damage

class Armor:
    armorName = str

    def __init__(self, armorName):
        self.armorName = armorName

class Food:
    foodName = str

class Show:
    showName = str

    def __init__(self, showName):
        self.showName = showName

class Tavern:
    taverName = str
    taverCapacity = int

    def __init__(self, tavernName, tavernCapacity):
        self.taverName = tavernName
        self.taverCapacity = tavernCapacity