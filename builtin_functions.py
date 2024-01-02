# all(): returns True if the iterable is empty of all values are True

def all_list_check(values):
    return all(type(list) == list for list in values)

# bool

check_bool = 0

print(bool(check_bool))

#enumerate; to loop over something with an automatic counter. The index number will be printed if you do this: 
games = ["Zelda", "Mario", "Final Fantasy", "Street Fighter"]

for x, element in enumerate(games):
    print(x, element)

# second enumerate() example

def reverse_string(str):
    re = ''
    for leter, char in enumerate(str[::-1]):
        re += char
    return re
print(reverse_string("this is not a palindrome"))


# input

name = input("What is your name?: ")

print("Hello " + name)

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

#map(function, iterable): define a function first and then run it. Map runs it for you, so no need to write a lot. It doesn't change the list (pure function)

def multiply_by_itself(item):
    return item * item

print(list(map(multiply_by_itself, [2, 4, 6, 8])))


# open() functions to read files. Parameters: file is mandatory. there are many others

file = open("filename.txt")
file.read()

# round() to round up a number. Behind the comma, you put the amount of decimals

happy = round(8/9, 3)

# slice()


# str() to type convert something to a string

# type() to see what data type it is 

print(type(True))




