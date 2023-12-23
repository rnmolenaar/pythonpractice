

# bool

check_bool = 0

print(bool(check_bool))

# input

name = input("What is your name?: ")

print("Hello " + name)

# input + int/float

age = int(input("What is your age?: "))

print("You are " +str(age) + " years old")

#enumerate; to loop over something with an automatic counter

def reverse_string(str):
    re = ''
    for leter, char in enumerate(str[::-1]):
        re += char
    return re
print(reverse_string("this is not a palindrome"))

# Len + input

hilde = len(input("what is your name? "))
print(hilde)

# len() + integer gives a type error

len(272)

# list()

snake = "python"

print(list(snake))

# open() functions to read files. Parameters: file is mandatory. there are many others

file = open("filename.txt")
file.read()

# round() to round up a number. Behind the comma, you put the amount of decimals

happy = round(8/9, 3)

# str() to type convert something to a string

# type() to see what data type it is 

print(type(True))




