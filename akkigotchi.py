import random
from random import randint
import time
from time import sleep 

class akkigotchi:
    
    def __init__(self, name):
        self.__name = name
        self.__colour = colour
        self.__health = random.randint(6, 10)
        self.__happiness = 10
        self.__age = 0
        self.__smart = random.randint(2, 5)
        self.__clean = random.randint(4, 6)
        self.__alive = True
        self.__stage = "Baby"
        self.__hunger = random.randint(2, 4)
        self.__energy = 10
        
    def setName(self):
        return self.__name
        
    def setColour(self):
        return self.__colour
        
    def setAge(self):
        return self.__age
            
    def newDay(self, day=1):
        self.__age += day
        self.whatstage()
        if self.__stage == "Toddler":
            self.__energy += 1
        elif self.__stage in ["Teenager", "Adult", "Grandma"]:
            self.__energy -= 1
        
    def whatstage(self):
        if self.__age > 10:
            self.__stage = "Grandma"
        elif self.__age > 7:
            self.__stage = "Adult"
        elif self.__age > 5:
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

    def limitStats(self):
        if self.__health > 10:
            self.__health = 10
        if self.__health < 0:
            self.__health = 0
        if self.__happiness > 10:
            self.__happiness = 10
        if self.__happiness < 0:
            self.__happiness = 0
        if self.__smart > 10:
            self.__smart = 10
        if self.__smart < 0:
            self.__smart = 0
        if self.__clean > 10:
            self.__clean = 10
        if self.__clean < 0:
            self.__clean = 0
        if self.__energy > 10:
            self.__energy = 10
        if self.__energy < 0:
            self.__energy = 0
        if self.__hunger > 10:
            self.__hunger = 10
        if self.__hunger < 0:
            self.__hunger = 0

    def feed(self):
        print('')
        
        print('*********************** feeding... *********************')
        print('nom nom nom'.center(55))
        print('')
        print('********************************************************')
        self.__health += randint(1, 2)
        self.__energy += randint(1, 3)
        self.__happiness += randint(1, 3)
        self.__hunger -= randint(2, 4)
        self.__clean -= randint(1, 4)
        self.__age += 1
        self.limitStats()
        self.displaystats()

    def play(self):
        print('')
        print('************* playing uno and football... **************')
        print('YAY i won :)'.center(55))
        print('i am a bit dirty though oops'.center(55))
        print('')
        print('********************************************************')
        if self.__hunger < 4:
            self.__health -= randint(1, 2)
            self.__colour = "sick brown"
        self.__hunger += randint(2, 4)
        self.__health += randint(1, 2)  
        self.__smart += 1
        self.__happiness += randint(1, 3)
        self.__clean -= randint(1, 3)
        self.__energy -= randint(1, 3)
        self.__age += 1
        self.limitStats()
        self.displaystats()

    def shower(self):
        print('')
        print('************** POV:singing in the shower ***************')
        print('SQUEAKY CLEAN'.center(55))
        print('')
        print('********************************************************')
        self.__hunger += randint(0, 2)
        self.__health += 1
        self.__clean += randint(3, 5)
        self.__energy -= 1
        self.__age += 1
        self.__happiness += 1
        self.limitStats()
        self.displaystats()

    def sleep(self):
        print('')
        print('********************* zzzzz... ************************')
        print('')
        print('********************************************************')
        self.__hunger += randint(3, 5)
        self.__health += 1
        self.__clean -= 2
        self.__energy += 4
        self.__age += 1
        self.__happiness += 1
        self.limitStats()
        self.displaystats()

    def gotoschool(self):
        print('')
        self.__hunger += randint(0, 2)
        self.__health += 1
        self.__clean += randint(3, 5)
        self.__energy -= 1
        self.__age += 1
        self.__happiness += 1
        self.__smart += 1
        self.limitStats()
        if self.__smart > 8:
            print('')
            print('*mr murphy & mr holdie praising me cause i am too good:)*')
            print('A* student frfr'.center(55))
        elif self.__smart > 4:
            print('')
            print('******i just got told off for talking in class******')
            print('Still need to do a bit of work'.center(55)) 
        else:
            print('')
            print('*i just got suspended for fighting with another student**')
            print('need to redeem myself ASAP'.center(55))
        print('********************************************************')
        self.displaystats()

akkis = []

def createnew():
    name = input('What is the name of your akki? ')
    
    new_akki = akkigotchi(name)
    akkis.append(new_akki)

def displaymenu():
    print('')
    print('************************* MENU *************************')
    print('1. Create new Akki'.center(55))
    print('2. Feed all '.center(55))
    print('3. Play with all '.center(55))
    print('4. Shower all '.center(55))
    print('5. Sleep all'.center(55))
    print('6. Send all Akkis to school'.center(55))
    print('7. Show stats for one Akki'.center(55))
    print('8. Show stats for all Akkis'.center(55))
    print('********************************************************')

def menu():
    while True:
        displaymenu()
        option = input('What would you like to do? ')
        print('')
        if option == '1':
            createnew()
        elif option == '2':
            for akki in akkis:
                print("Feeding " + akki.setName())
                akki.feed()
        elif option == '3':
            for akki in akkis:
                print("Playing with " + akki.setName())
                akki.play()
        elif option == '4':
            for akki in akkis:
                print("Showering " + akki.setName())
                akki.shower()
        elif option == '5':
            for akki in akkis:
                print("Putting " + akki.setName() + " to sleep")
                akki.sleep()
        elif option == '6':
            for akki in akkis:
                print("Sending " + akki.setName() + " to school")
                akki.gotoschool()
        elif option == '7':
            name = input('Enter the name of the Akki to check: ')
            found = False
            for akki in akkis:
                if akki.setName() == name:
                    akki.displaystats()
                    found = True
            if not found:
                print('No Akki with that name found.')
        elif option == '8':
            for akki in akkis:
                akki.displaystats()
        else:
            print('Invalid option. Try again.')

def rules():
    print('************************************************************')
    print('🌟 WELCOME TO THE WORLD OF AKKIGOTCHI 🌟'.center(55))
    print('************************************************************')
    print('📜 OFFICIAL RULEBOOK & TOTALLY LEGIT USER GUIDE 📜'.center(55))
    print('1. You are now the proud parent of an *Akkigotchi*, a highly unpredictable, occasionally dramatic, and always adorable digital creature with very real (fake) emotions.'.center(55))
    print('2. Your mission is to keep it alive. Simple? Absolutely not.')
    print('3. Feed it or face the consequences. A hangry Akkigotchi is more dangerous than a Year 9 on Red Bull.'.center(55))
    print('4. Play with it.')
    print('5. Showers are optional... for you. Not for them.')
    print('6. Sleep is sacred. Do not disturb unless you are into digitally-induced tantrums.')
    print('7. School attendance is required. Bribes optional.')
    print('8. If it gets too smart, it might turn on u. Be warned.')
    print("")
    print('*********************BONUS CHARACTERS**********************')
    print('- Shami: Megamind with horror vision.')
    print('- Chloe: Ancient soul trapped in eternal battle with her mother-in-law.')
    print('- Pheebs: Silent, deadly, and constantly lost.')
    print('************************************************************')
    print("")
    print('Have fun. And remember:')
    print('If your Akkigotchi dies... it is probably your fault.')
    start=input("To start press enter:")
rules()
menu()

