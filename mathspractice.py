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


# to get the square root of a number, use the math.sqrt() method. Insert the number between ()
math.sqrt()
