# dunder methods start and end with __. Also called magic methods. They are used with specific classes. Using dir() will show you which ones can be used with a class


# __name__ Every python file has a  __name__ variable. The main file being run has the value __main__

def show_name():
  print(f"the name is {__name__}")

show_name()

# __init__(self, ...) is used when an object is made from a class. Self is the object here. 


# __new__ create a new object 

# __str__: no parameters. It makes it reader friendly

class HappyDays:
  def __str__(self)
