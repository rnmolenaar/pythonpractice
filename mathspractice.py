squares = []
for number in range(1, 101):
    square = number**6
    squares.append(square)
print(squares)

--
from random import randint
number = randint(1, 100) 

if number % 2 != 0:
    print("odd")
else:
    print("even")
    
