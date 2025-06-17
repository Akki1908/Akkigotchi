import random
from random import randint
import time


class akkigotchi:
    def __init__(self, name, colour):
        self.__name = name
        self.__colour = colour
        self.__health = random.randint(6, 10)
        self.__happiness = 10
        self.__age = 0
        self.__smart = random.randint(2, 5)
        self.__clean = random.randint(4, 6)
        self.__alive = True
        self.__stage = "Egg"
        self.__hunger = random.randint(3, 5)
        self.__energy = 10
    
    def setName(self):
        return self.__name
        
    def setColour(self):
        return self.__colour
        
    def setAge(self):
        return self.__age
        
    
        
    def displaymenu(self):
        print('')
        print('************************* MENU *************************')
        print('1.Create New Akkigotchi').center(55)
        print('2.Check Status').center(55)
        print('3.Feed').center(55)
        print('4.Play').center(55)
        print('5.Shower').center(55)
        print('6.Sleep').center(55)
        print('7.Watching Craig n Dave').center(55)
        print('')
        option=int(input("What would you like to do?").center(55))
        print('********************************************************')
        if option == 1:
            name = input("Enter name: ")
            colour = input("Enter colour: ")
            self.__init__(name, colour)
        elif option == 2:
            self.displaystats()
        elif option == 3:
            self.feed()
            
    
    
    def newDay(self, day=1):
        self.__age += day
        self.whatstage()
        if self.__stage == "Toddler":
            self.__energy += 1
        elif self.__stage in ["Teenager", "Adult", "Grandma"]:
            self.__energy -= 1
        
    def whatstage(self):
        if self.__age > 65:
            self.__stage = "Grandma"
        elif self.__age > 18:
            self.__stage = "Adult"
        elif self.__age > 13:
            self.__stage = "Teenager"
        elif self.__age > 3:
            self.__stage = "Toddler"
        else:
            self.__stage = "Egg"
        return self.__stage
            
    def displaystats(self):
        print('')
        print('********************* CURRENT STATS ********************')
        print(("Name = " + self.__name).center(55))
        print(('Colour ='+ self.__colour).center(55))
        print(('Stage ='+ self.__stage).center(55))
        print(('Health ='+ str(self.__health)).center(55))
        print(('Happiness ='+ str(self.__happiness)).center(55))
        print(('Age ='+ str(self.__age)).center(55))
        print(('Smart ='+ str(self.__smart)).center(55))
        print(('Energy ='+ str(self.__energy)).center(55))
        print(('Hunger ='+ str(self.__hunger)).center(55))
        print('********************************************************')

    def feed(self):
        print('')
        print('*********************** feeding... ************************')
        print('nom nom nom'.center(55))
        self.__hunger+=randint(2,4)
        self.__clean-=randint(1,4)
        self.__energy+=randint(1,3)
        self.__age+=1
        self.displaystats()

akki = akkigotchi("akki", "red")       
while True:
    akki.displaymenu()       


