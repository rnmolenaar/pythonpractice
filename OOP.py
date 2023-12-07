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
 
    
