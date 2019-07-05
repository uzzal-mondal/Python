
import random


# this is call for random num generate.
# random.random * 100

for x in range(1,6):
    gues = int(input("Enter your gues"))
    randomNum = random.randint(1,10)

    if gues == randomNum:
     print("You have won",randomNum)

    else:
     print("You have loss",randomNum)

