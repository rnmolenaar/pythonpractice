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

