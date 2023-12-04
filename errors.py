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
     

