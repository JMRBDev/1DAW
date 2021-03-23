import random
from events import *
from characters import *
from items import *

# Events
class Game:
    username = str
    password = str

    def __init__(self, username, paassword):
        self.username = username
        self.password = password

class Engine:
    currentYear = 476
    questionsList = {"Do you want to hire one Soldier?" : ["Yes", "No"],
                     "Do you want to hire one Farmer?" : ["Yes", "No"],
                     "Do you want to hire one HandCrafter?" : ["Yes", "No"],
                     "Do you want to hire one Priest?" : ["Yes", "No"],
                     "Do you want to hire one Innkeeper?" : ["Yes", "No"]}
    eventsList = {"barbAttack", "falseProphet", "streetFight",
                  "plague", "birth", "collect", "drought"}

    def showInfo(self):
        currentYear = self.currentYear, "A.C"
        return currentYear

    def ask(self):
        questionsList = self.questionsList
        question = random.choice(list(questionsList.keys()))
        return question

    def createEvent(self):
        eventsList = self.eventsList
        event = random.choice(list(eventsList.keys()))
        print(event)

    def run(self):
        print(self.showInfo())
        print(self.ask())

if __name__ == "__main__":
    print("----- Medieval Game -----")
    username = input("Username: ")
    password = input("Password: ")
    myGame = Game(username, password)
    myEngine = Engine()
    
    myEngine.run()