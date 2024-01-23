# use 'as' to change the name of the module

# You can only import one method or two, three etc. If you want to import them all, use *

from random import shuffle

#keyword module

import keyword. To check if something is a keyword

def check_keyword(*args):
  for item in args:
    if keyword.iskeyword(): return True
  return False

import keyword

def contains_keyword(*args):
    for item in args:
        if keyword.iskeyword(item): return True
    return False

# import module you made yourself

import selfmade_module

num = selfmade_module.function_defined_in_other_file()

# To assign a random number to a variable, which can then be used in conditional statements

from random import randint
num = randint(1, 1000)

### modules

# keyword: regards the Python keywords

import keyword

def keyword_present(*args):
    for i in args:
        if keyword.iskeyword(i): return True
    return False

# math module

import math

result = math

answer = math.sqrt(16384)
print(answer)

# random

# .choice() method: pick something random from a list


# random number
import random

print (random.randint(0, 60))

### external modules

# pyfiglet

# termcolor

from termcolor import colored

colored_string = colored("Test color", color="yellow", on_color="on_magenta")
print(colored_string)
