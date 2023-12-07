# math module

import math

result = math

answer = math.sqrt(16384)
print(answer)

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

# random number
import random

print (random.randint(0, 60))
