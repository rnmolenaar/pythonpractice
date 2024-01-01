

# square root. To get to 3.0

9 ** 0.5

# // integer division rounds up or down to get to a whole number
10//3


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

#How to find factors

def find_factors(num):
    factors_of_number = []
    i = 1
    while i <= num:
        if num % i == 0:
            factors_of_number.append(i)
        i += 1
    return factors_of_number


print(find_factors(4987))
