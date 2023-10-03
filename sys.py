import sys

#Packaged with Python. 

def joke():
    print("How old are you?")
    age = int(sys.stdin.readline())
    if age >= 30 and age <= 50:
        print("What is the result of 30 + 76 + 83 + 90 * 50?")
    else:
        print("What are you talking about?")

joke()

sys.exit() 
