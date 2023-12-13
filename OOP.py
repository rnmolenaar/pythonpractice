#creating a Class and a few objecs:

class Animal:
    pass

cat = Animal()
dog = Animal()
rat = Animal()
print(type(dog))

# make a class of comments online

class Comment():
    def __init__(self, user, text, likes=0):
        self.user = user
        self.text = text
        self.likes = likes

# Bank class

class Bank:
 
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0
 
    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
 
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
 
# Raise errors. the last two will have errors raised.

class Pet:
    allowed = ['rat', 'rabbit', 'parcot', 'cat']
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} as a pet")
        self.name = name
        self.species = species
    def set_species(self,species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} as a pet")
        self.species = species

cat = Pet("Felix", "cat")
dog = Pet("Snuffles", "bear")
tiger = Pet("Happy", "Tiger"t

# if you want to use a parent class. Super refers to Plant as the parent class

 class Rose(Plant):
     def __init__(self, color, sort, country):
     super().__init__(color, sort="Rose")
     self.country = country


     
            
