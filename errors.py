## try, except, else, finally. Try = test, except: take care of the error, else=what happens when there is no error, finally=happens regardless of whether there are errors

try: 
  print(something)
except NameError:
  print("Something needs to be defined:)
except:
print("There is a problem. Check your code")


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



# AttributeError: attribute does not exist. iow a method does not exist

[9, 2, 4].singsong()

# IndexError: the index is too high and does not exist


# KeyError when you call a key in a dictionary that does not exist (similar to IndexError)

TRex = dict(name = "Rexie", food = "meat", size = "big")

print(TRex["age"]) # KeyError

# NameError: something hasn't been defined. Also happens when a module has not been imported yet and its methods are not yet available.

# SyntaxError. Something is missing or something is wrong.
101dalmatians = "many dogs" #syntax error because a variable can't start with a number

#TypeError: wrong type is used. Something is used meant for a different type. 

# ValueError: there is nothing wrong about the type but the value added is wrong

float("this is indeed a string, so the correct type, but the value can't be converted to an integer")

#ZeroDivisionError when you try to divive by 0


#######
