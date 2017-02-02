import random
from random import *
import sys
import time
'''
    fw = open("levels.UR", "r+")
    line = fw.readline()
    if ( line == "1" ):
        Line.replace( "1", "2" )
    fw.close()
'''
def states():
    
    global level
    level=0
    return
    if level == 1:
        spider()
    elif level == 2:
        jungle()
    elif level == 3:
        desert()
    elif level == 4:
        House()
    elif level == 5:
        shop()
    elif level == 6:
        gremlin()
    elif level == 7:
        goblin()
    elif level == 8:
        Tundra()

    
def stats():
    if game.hp <= 0:
        restart = ("You Died! Do you want to return to a previous checkpoint " + "Yes or No?")
        if (restart.lower() == "no"):
            if game.checkpoint == int(0):
                game()
            elif game.checkpoint == int(1):
                desert()       
            elif game.checkpoint == int(2):
                gremlin()
        

def commands():
    commands.self = input("Check your Stats now using \"Stats\".")
    
    if (commands.self == "Gold"):
        print(game.gold)
    elif (commands.self == "Water"):
        print(game.water)
    elif (commands.self == "Food"):
        print(game.food)
    elif ( commands.self == "Health"):
        print(game.hp)
    elif (commands.self.lower() == "Stats"):
        print("You have a HP level of :" + str(game.hp) + "\n" + "You have a Gold level of: " + str(game.gold) + "\n" + "You have a Water level of: " + str(game.water) + "\n" + "You have a Food level of: " + str(game.food))

def age():
    try:
        agea = int(input("Whats Your age? "))
        if (int(agea) <= int(10)):
            print("Your too young")
            sys.exit("Too Young.")
        else:
            game()
                
    except ValueError:
        print("Error! Enter An age")
        age()

def pregame():
    print("Neurotic Studios Presents!")
    print()
    age()
    game()
    
def game():
    print("The time is two past the hour, You better Get going")
    print("You meet an elderly man, He ask's what is your name?")
        
    game.playerName = input("Enter Your Name: ")
    print(game.playerName + "?")
        
    game.hp = int(100)
    game.gold = int(100)
    game.water = int(100)
    game.food = int(100)
    game.bow = int(0)
    game.checkpoint = int(0)
    time.sleep(10)
    level + 1
    spider()
        #Jungle()
    
def spider():
    print("A giant arachnid appears! What do you do?")
    print("Press A To Attack.")
    spider.Input = input()
    if (spider.Input.lower() == "b"):
        print("You ran!")
    if (spider.Input.lower() == "a"):
        print("You attacked!")
        print("You hit. The Spider Died. But you got poisned!")
        print("You lost 10 HP!")
        SpiderHP = game.hp - 10
    else:
        error()
        spider()
    commands()
    print()
    level + 1
    jungle()
        
def jungle():
    #chanceToHit
    print("You stumble after that attack and find your self standing in frount of a Cougar")
    print("Press A To Attack.")
    print("Press B to Run")
    jungle.Input = input()
    if (jungle.Input.lower() == "b"):
        print("You Ran But hit a Fork in the Road!")
        forkRoad()
    elif (jungle.Input.lower() == "a"):
        print("You Find a Rock on the Floor, you use the Rock to attack!")
    else:
        error()
        jungle()
    desert()
    level + 1
    
def desert():
    print("You have made your way to the desert." + "\n Do you go left or do you go right?" + "\n Press L to go left or R to go right.")
    desert.Input = input()
    if (desert.Input.lower() == "r"):
        print("You went Right!" + "\n But you found a House")
        house()
    elif (desert.Input.lower() == "l"):
        print("You went left!" + "\n But you found a Shop")
        shop()
    else:
        error()
        desert()
    level + 1
    
def House():
    print("Your in a house with a Room full of gold!" + "\n \n You found a Huge ammount of Gold you found 600 Gold!")
    house.Input = input("\n Type Left to go L or R to go right!")
    if (house.Input.lower() == "l"):
        warlock()
    if (house.Input.lower() == "r"):
        gremlin()
    else:
        error()
        House()
    level + 1
    
def forkRoad():
    print("OH NO! Which way do you go?")

def error():
    print("You didnt exactly use what the Narrator said earlier...")
    
def shop():
    print("Hi what cha want?")
    print("a = 100 hp - 50 gold")
    print("b = 50 food - 60 gold")
    print("c = 50 water - 100 gold")
    print("d = 1 bow - 200 gold")
    shop.Input = input("What would you like?")
    if (shop.Input.lower() == "a" ):    
        if (game.gold > 49):
            game.gold - 50
            game.hp + int(100)
        else:
            print("You dont Have enough gold :( \n Pick something else.")
    
    if (shop.Input.lower() == "b"):
        if (game.gold > 59):
            game.gold - 60
            game.food + int(50)    

    if (shop.Input.lower() == "c"):
        if (game.gold > 99):
            game.gold - 100
            game.water + int(50)
    if (shop.Input.lower() == "d"):
        if (game.gold > 99):
            game.gold - 200
            bow()
            
    elif (shop.Input.lower() == "exit"):
        house()
    else:
        error()
    level + 1
    
def gremlin():
    print("OH NO! You have a 20\%\ chance to attack him. \n HE'S TOO SMALL!")
    gremlin.Input = input("use A to attack and R to run")
    chance  = random.randint(1, 100)
    if (gremlin.Input.lower() == "a"):
        if (chance <= 20):
            print("You attack and kill the gremlin with a punch to the face.")
            
        else:
            print("You didn't hit.")
            print("You lost 25 hp!")
            game.hp - 25
            gremlin()

    if (gremlin.Input.lower() == "b"):
        print("You cant Run, Your Cornered")
        gremlin()

    else:
        error()
        gremlin()
    
    level + 1
        
def bow():
    print("This is a bow it upps your chances to get a hit on an enemy.")
    game.bow = int(1)

    
    
def Goblin():
    
    chance = random.randint(1, 100)
    print("after your escape your escape:")
    print("You ran into a rogue Goblin! It scrapes you with its claws and you loose 10HP!")
    print("You lost 10 hp!")
    game.hp - 10
    Goblin.Input = input("Would you like to attack him or run? Use A to attack and R to run")
    if (Goblin.Input.lower() == "a"):
        if (chance <= 20):
            print ("The Goblin dodged your attack and chucks acid at you -10HP!")
        else:
            print ("You have succesfuly killed the Goblin and you found 2 weak health potions! +10XP, +5GOLD")
    if (Goblin.input.lower() == "r"):
        print ("You have ran succsesfuly!")
    level + 1

def Tundra():
    print("After that match with a Gremlin you find your self tumbling down a hill and into Tundra forest.\nyou look around and try to regain your posture, but your too weak. \nYou find a monster staring you in the face you stuggle to make out what it is but then you realise that its a warlock\n the friendliest creature of all!")
    print("The warlock says:")
    print("You can join me, You can be my partner or you can be an unknown asalent which will it be?")
    print("You chose to join him!")
    print("Now Follow me, \nyou follow him into the dungeon of the warlocks and find that...")
    print("Your Now unconsious..")
    print("You awoke with a warlock staring at you again!\nHe pull a level and your body is stretched and you hear a snap and a searing pain through your body!")
    time.sleep(2)
    WouldyouDo = input("Do you \"struggle\" or \"lie limp?")
    if WouldyouDo.lower() == "struggle":
        print("you lose 10 hp but break free from shackles.")
        game.hp - 10
        goblin()
    if WouldyouDo.lower() == "lie limp":
        print("You let them pull limb from limb and die..")
        game.hp = 0
        stats()
    else:
        Tundra()
    level + 1

pregame()
