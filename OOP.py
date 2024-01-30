# When you create a class, you also ceate the functions it can use as methods, when you create an object
#creating a Class and a few objects:

class Superhero:
    def __init__(self, superpower, name, real_name):
        self.superpower =  superpower
        self.name = name
        self.real_name

ratgirl = Superhero("own the sewers", "Ratgirl", "Atty")

#second example

Class Planet:
     def __init__(self, star, sort, size_ranking):
        self.star = star
        self.sort = sort
        self.size_ranking = size_ranking

Saturn = Planet("Sun", "gas giant", 2) 
Trappist1e = Planet("Trappist1e", "rocky, earth-sized". 4)
TrES4b = Planet("GSC 02620-00648", "hot Jupiter", 1)

#Third example. 

Class King:
def __init__(self, country, era, warlike):
    self.country = country
    self.era =era 
    self. warlike = warlike

EdwardI = King("England", "medieval", True)
LouisXIV = King("France", "Enlightenment", False)
FerdinandofAragon = King("Aragon", "late medieval", True)

#Fourth Example

Class Country:   
    def__init__(self, continent, language, capital)
    self.continent = continent
    self.language = language
    self.capital = capital

Nigeria = Country(

Class Fairytale:
    def __init__(self, villain, object):
        self.villain = villain
        self.object = object

Cinderella = Fairytale("evil stepmom", "shoe")
Snow White = Fairytale("evil queen and stepmom", "apple")
  


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

# if you want to indicate that something is private, you put _ in front of it. Should only be used in the class (can still be accessed, but it is a convention
 
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


     
            
