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
    print("Use ints of floats"
  except ZeroDivisionError:
    print("You cannot divide by 0")
  else:
    print(f{a} divided by {b} is {result"})
    
