
import time
import random
# intro info
time.sleep(1)
print("Hi, this is the character customization setup, please follow the instructions excatly as instructed, to avoid crashes")
time.sleep(3)
print("choose your gender, press 1 for guy, and 2 for girl. Then press enter.")

# a list that contains genders, with 1 and 2 being the right options as sellection options is defined. So that the player can sellect gender by inputing 1 or 2.

Gender = ["none", "guy", "girl"]
numberlist1 = input()

if Gender[int(numberlist1)]:
    GenderChosen = Gender[int(numberlist1)]

    print("Your gender is", GenderChosen)



print("enter your name")
YourName = input()
print("hi", YourName)

# a hairtype list is defined, so that the player can sellect hairtypes directly from the list, with the numberlist input variable.

print("Choose your haritype. 1=black, 2=red, 3=golden, 4=white, 5=brown. Type the number, then press Enter")

Hairs = ["redundant", "black", "red", "golden", "white", "brown"]

numberlist = input()

if Hairs[int(numberlist)]:
    HairType = Hairs[int(numberlist)]

    TellMe = "none"

if GenderChosen == "guy":
    TellMe = "handsome"
else:
    TellMe = "beutifull"

    # For good measure, a print statement that contains the cracters chosen hairtype, name, politically correct adressing form and gender.

print(" Hello", YourName, "you are a", TellMe, GenderChosen, "with" , HairType,"hair")

time.sleep(3)
print("Now", TellMe, "please enter your weight in kg")
weight = input()

time.sleep(3)
print("now", YourName, "i will need to know your height in cm")
height = input()



if int(weight) < int(height) / 3:
    setclass = "Thief"
elif int(weight) * 2 < int(height):
    setclass = "archer"
elif int(weight) * 3 < int(height):
    setclass = "squire"
elif int(weight) * 2 > int(height):
    setclass = "patron"
else:
    setclass = "mystic"

print("your class is thereby:", setclass)

# the damage variables are defined to ensure that they are changed with respect to the value 0
Damage = 0
Hp = 0
Luck = 0

# The answer and chance variables are defined, chance relates to wether or not a situation will make.
chance = random.randint(1,10)
answer = ["q","Y","N"]
# The classes get their hp, damage and luck atributtes defined.
if setclass == "Thief":
    Damage = Damage + 10
    Hp = Hp + 50
    Luck = Luck + 8

elif setclass == "archer":
    Damage = Damage + 12
    Hp = Hp + 70
    Luck = Luck + 4

elif setclass == "squire":
    Damage = Damage + 18
    Hp = Hp + 100
    Luck = Luck + 3

elif setclass == "patron":
    Damage = Damage + 10
    Hp = Hp + 50
    Luck = Luck + 6

elif setclass == "mystic":
    Damage = Damage + 24
    Hp = Hp + 20
    Luck = Luck + 9

ArmouredMan = 100

time.sleep(3)
# Here the story unfolds, with regards to the selected class. Under each if statement, a story is composed with all unique starts. The if statements for setclass decides which story takes place, for the respective class.

if setclass == "Thief":
    print("you find yourself standing on a road with a purse in one hand and a bloody knife in the other. An armoured man aproaches you")
    time.sleep(2)
    print("do you a run away, or fight the armoured man?")
    time.sleep(1)
    print("typy 1 for Run away, type 2 for fight")

    #choice variable for flee or fight is defined with respect to the answer list. It can be either 1 or 2 to sellect an element from lists.
    choice1 = input()

    if answer[int(choice1)] == 1:
        print("you escaped fromt the man, but you are hungry and tired. Where do you go to now?")
        print(input())
    elif answer[int(choice1)] == 2:

        print("you violently attack the Armoured man")
    if chance + Luck > 10:
        print("You somehow mannage to kill the man. You have won.")
        time.sleep(3)
        print("you decide to steal the mans purse aswell, you are now quite wealthy.")
        print("you can now decide to either travel to a nearby kingdom and try your luck, or walk allong the road")

    elif chance + Luck < 10:
        print("you done fucked it up, you can´t penetrate his armour, he takes a swing and kills you")
        time.sleep(6)
        print("Game Over")
        time.sleep(6)


elif setclass == "archer":
    print("you are standing at a shooting range. You are trying to impress the commander of the camp by hitting the bullseye. What aproach do you take?")

elif setclass == "squire":
    print("You are a squire for a famed knight called Sir Malloward. The two of you are traveling together by horse, but suddently you are attaked by bandits. How do you act?")

elif setclass == "patron":
    print("You are trading with a merchant in the city of Dulkadir. The merchant tries to sell you a special gem. How do you act?")

elif setclass == "mystic":
    print("You Wake up naked in the wild, your red skin shines in the dailight, a group of people are standing 30 m away by a road. Do you approach them?")
