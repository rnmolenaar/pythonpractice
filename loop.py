msg = input("Speak: ")

while msg != "stop":
    print(msg)
    msg = input()
print("Okay, chill")

###

import random

random_number = random.randint(1, 20)
guess = None

while guess != random_number:
    guess = input("Guess a number ")
    guess = int(guess)
    if guess < random_number:
        print("It's too low")
    elif guess > random_number:
        print("It's too high")
    else :
        print("You guessed it")

