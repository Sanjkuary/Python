#Guess the number

import random

target = random.randint(1, 100)

while True:
    userChoise = int(input("Guess the target : "))
    if (userChoise == target):
        print("Sucess : Correct Guess!")
        break

    elif(userChoise < target):
        print("Your numbeer is too small, guess again..")
    else:
        print("Your number is too big, guess again..")

print("-------Gmae Over------")

import random

target = random.randint(1, 100)

while True:
    userChoice = (input("Guess the target or Quit : "))
    if (userChoice == "Quit"):
        break

    userChoice = int(userChoice)
    if (userChoice == target):
        print("Sucess : Correct Guess!")
        break

    elif(userChoice < target):
        print("Your numbeer is too small, guess again..")
    else:
        print("Your number is too big, guess again..")

print("-------Gmae Over------")


