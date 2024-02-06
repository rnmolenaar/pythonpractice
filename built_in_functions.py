# any() if any is truthy


# all(): returns True if all values are truthy or empty in an iterable

def all_list_check(values):
    return all(type(list) == list for list in values)

# bool()

check_bool = 0

print(bool(check_bool))

# chr() gets the unicode of a character

# dir() shows you all the methods of an object. Is handy to use with a module as well. 

import random

print(dir(random))

#enumerate; to loop over something with an automatic counter. The index number will be printed if you do this: 
games = ["Zelda", "Mario", "Final Fantasy", "Street Fighter"]

for x, element in enumerate(games):
    print(x, element)

# dict() to create a dictionary

TRex = dict(name = "Rexie", food = "meat", size = "big")

# second enumerate() example

def reverse_string(str):
    re = ''
    for leter, char in enumerate(str[::-1]):
        re += char
    return re
print(reverse_string("this is not a palindrome"))

# filter()

# help() shows the documentation of modules, functions, classes, keywords. You don't need print() to have it shown

import tkinter

help(tkinter)


# input()

name = input("What is your name?: ")

print("Hello " + name)

#If you want the user to input on a new line then: 
print("What is your name?"
answer = input()
print("Your name is " + answer)

# example two input()

# input + int/float

age = int(input("What is your age?: "))

print("You are " +str(age) + " years old")




#int() converts a float into an int by chopping of everything behind the decimal. It doesn't round up

change_to_integer = int(34.7262) # 34


# Len + input

hilde = len(input("what is your name? "))
print(hilde)

# len() + integer gives a type error

len(272)

# list()

snake = "python"

print(list(snake))

# You can do list() on a range as well. 

numbers_range = range(0,10)

list(numbers_range)

#map(function, iterable): define a function first and then run it. Map runs it for you, so no need to write a lot. It doesn't change the list (pure function)

def multiply_by_itself(item):
    return item * item

print(list(map(multiply_by_itself, [2, 4, 6, 8])))

# machine 

machine = input("How many times should the machine repeat this process?")
machine = int(machine)

for mach in range(machine):
    print("Button pushed")


# map() accepts two arguments: a function and an iterable

# min() to find the shortest thing



# open() functions to read files. Parameters: file is mandatory. there are many others

file = open("filename.txt")
file.read()

# round() to round up a number. Behind the comma, you put the amount of decimals

happy = round(8/9, 3)

# set(): to create a set out of something

list = [ 1, 2, 5 ]

set(list)

# slice()

# sorted() works with tuples or lists. It returns a copy, doesn't change the original itself. 
#It sorts it by alphabet and numbers. if reverse=True it will change the order
# when sorting a dictionary, you have to write down the parameter to be sorted: key=len to have he ones with most key-value pairs


# str() to type convert something to a string

# tuple() to create a tuple

# type() to see what data type it is 

print(type(True))




