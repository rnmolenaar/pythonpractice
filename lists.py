#Lists start counting at 0, just like ranges

# return index of a list

def index_list(arr, idx):
    if idx >= 0:
        return arr[idx]
    return arr[idx + len(arr)]

print(index_list([1,2,3,4,5], -2))

# check if something is in a list (you will get True or False

my_list = [0.5, "what", "nono", ["blabla", "yay"]]

print("yelp" in my_list)

######### build in functions
#len()

#list() to create a list out of a range

pet = list(range(1,200))

print(pet)

##################built in methods for lists

## general list methods

# .index() shows you where an item is 

languages = ["English", "Japanese", "Chinese", "French", "Romanian"]
print(languages.index("English")) # 0




## adding to a list

# .append() will add something to the end of a list. Takes only one argument

rodents = ["rats", "capybaras","rabbits"]
rodents.append("mice")

print(rodents)

# .extend() will take in another list and add the values to the end of the first list

rodents = ["rats", "capybaras","rabbits"]
rodents.extend(["mice", "guinea pigs"])

print(rodents)  #['rats', 'capybaras', 'rabbits', 'mice', 'guinea pigs']

# .insert: adds a value at a specific position in the list

rodents = ["rats", "capybaras","rabbits"]
rodents.insert(2, "hamsters")

print(rodents)

## removing from a list

# .clear() removes everything

planets = ["Mercury", "Venus", "Mars", "Jupiter"]
planets.clear()

print(planets) # []

# .pop() removes something from list at a specific place. If no index is given, the last item will be removed from the list. This last item is then returned
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter"]
planets.pop(2)

print(planets) # earth is returned

# .remove() you need to give a value. It only removes the first one if there are more than one. Does not return the item. 

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter"]
planets.remove("Mercury")

print(planets)










