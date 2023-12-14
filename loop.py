msg = input("Speak: ")

while msg != "stop":
    print(msg)
    msg = input()
print("Okay, chill")

#To import random and create a random number generator
import random

random_number = random.randint(1, 20)
guess = None

#to guess a random number

while guess != random_number:
    guess = input("Guess a number ")
    guess = int(guess)
    if guess < random_number:
        print("It's too low")
    elif guess > random_number:
        print("It's too high")
    else :
        print("You guessed it")
        continue_game = input("do you want to play again? (y/n) ")
        if continue_game == "y":
            random_number =random.randint(1,10)
            guess = None
        else:
            print("see you next time")

# test for loop. iterable/iterators

def test_iterable(iterable):
    iterator = iter(iterable)
    While True:
    try:
        item = next(iterator)
    except: StopIteration:
        break
    else: 
        func(item)
        
test_iterable(["dog", "cat", "rat"], print )

