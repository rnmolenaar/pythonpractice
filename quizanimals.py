print("Enjoy the quiz")
score = 0

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay, let's play")

answer = input("How many legs does a spider have? ")
if answer.lower() == "eight" or answer == "8":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("How many legs does a bee have? ")
if answer.lower() == "six" or answer == "6":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("How many legs does a cat have? ")
if answer.lower() == "four" or answer == "4":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("Your got" + str(score) + " questions correct")


