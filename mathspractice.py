#pemdas is the order of calculating things

squares = []
for number in range(1, 101):
    square = number**6
    squares.append(square)
print(squares)

#  simple odd and even checker

from random import randint
number = randint(1, 200) 

if number % 2 != 0:
    print("odd")
else:
    print("even")

# ** to the power of

2**46

# to get the square root of a number, use the math.sqrt() method. Insert the number between ()
math.sqrt()

# floor division // to get an integer back
print(8//7)
