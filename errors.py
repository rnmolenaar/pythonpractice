# error types: syntax error because a variable can't start with a number
101dalmatians = "many dogs"

## common errors

# NameError: something hasn't been defined

# SyntaxError. Something is missing

#TypeError: wrong type is used. Something is used meant for a different type. 


#######
# when raising error messages

if type(arg) is not str:
  raise TypeError("this must be an instance of str")

def get dictionary, key):
  try:
    return dictionary[key]
  except: KeyError:
    return None

dictionary = {"Country": "Netherlands"]

print(get(dictionary, "name"))

# several except

def divide(a, b):
  try:
    result = a/b
  except TypeError:
    print("Use ints or floats")
  except ZeroDivisionError as err:
    print("You cannot divide by 0")
    print(err)
  else:
    print(f"{a} divided by {b} is {result}")

divide(2,0)

# example try/except block

def divide(num1, num2):
    try: 
        total = num1 / num2
    except TypeError: 
        return "Please enter integers or floats"
    except ZeroDivisionError:
        return "Do not divide by zero"
    return total
     
# using assert

def function(a, b):
  assert x = 0, "Whatever is here, will show up when x is not 0"
 return x

## Error types

# KeyError when you call a key in a dictionary that does not exist

TRex = dict(name = "Rexie", food = "meat", size = "big")

print(TRex["age"]) # KeyError
