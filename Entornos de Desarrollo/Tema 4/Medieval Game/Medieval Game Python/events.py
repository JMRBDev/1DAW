# Events
class Event:
    eventName = str

    def __init__(self, eventName):
        self.eventName = eventName

class BarbAttack(Event):
    soldiersPercentage = float

    def __init__(self, soldiersPercentage):
        self.soldiersPercentage = soldiersPercentage

    def lowerCitizens(self, soldiersPercentage):
        pass

class FalseProphet(Event):
    numPriests = int

    def __init__(self, numPriests):
        self.numPriests = numPriests

    def loseCitizens(self):
        pass

class StreetFight(Event):
    numTaverns = int

    def __init__(self, numTaverns):
        self.numTaverns = numTaverns

    def mutiny(self): # amotinaje
        pass

    def callSoldiers(self):
        pass

    def loseCitizens(self):
        pass

class Plague(Event):
    workingDays = int

    def __init__(self, workingDays):
        self.workingDays = workingDays

    def loseCitizens(self, workingDays):
        pass

class Birth(Event):
    numWorkingDay = int
    birthRate = float

    def __init__(self, workingDay, birthRate):
        self.numWorkingDay = workingDay
        self.birthRate = birthRate

    def birthCitizens(self):
        pass

class Collect(Event):
    taxes = float

    def __init__(self, taxes):
        self.taxes = taxes

    def buildTavern(self):
        pass

    def buildShow(self):
        pass

    def askForTaxes(self, taxes):
        pass

class Drought(Event):
    percentage = float

    def lowerHarvest(self, percentage):
        pass