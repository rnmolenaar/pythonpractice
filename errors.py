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
