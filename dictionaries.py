# Dictionary is mutable and unordered
#Make a dictionary
character = {"name": "Smiley", "fan of": "River music", "Speaks": "A language"}

# How to add values of different keys together in a dictionary

person = {
    "first": "Janie",
    "last": "Grey",
}

full_name = person["first"] + " " + person["last"]

# Accessing a specific value in a dictionary
TRex = dict(name = "Rexie", food = "meat", size = "big")

print(TRex["name"]) # Rexie

# adding a value to a dictionary

kings = {"France": "Louis", "England": "Edward"}

kings["Spain"] = "Carlos"

# running a for loop on the values in a dictionary. You only get the values with this

for value in dictionary.values():
    print(value) 
# You can also do .keys() is the same as above

# for items()

TRex = {"name" : "Rexie", "food" : "meat", "size" : "big"}

for keytje, valuetje in TRex.items():
    print(f"the key is {keytje} and the value is {valuetje}")

# running a for loop on items. You get both key and value in a tuple.
    
for k, v in dictionary.items():
    print(f:"key is {k} and value is {v}")
    
# How to add all values in a dictionary

gifts = dict(Lily=2.0, Mina=8.9, Pat=12.0, Lionel=9.5, Sile=15.0)

total_gifts = 0

for gift in gifts.values():
    total_gifts += gift

#or

    total_gifts = sum(gift for gift in gifts.values())

# or

total_gifts = sum(gifts.values())

# other addition example

moons = dict(mercury = 0, venus = 0, earth = 1, mars =2)

total_moons = 0

for moon in moons.values():
    total_moons += moon

print(total_moons)

# fromkeys method
start = dict.fromkeys(dictionary_name, 0)

# Check if something is in a dictionary with in and not

numbers = {1, 2, 7{

6 in dictionary_name # False

### Dictionary comprehension { :  for    in    }

#dictionary comprehension
{num:("even" if num % 2 ==0 else "odd") for num in range(0, 20)
    
# dict comprehension: zipping two dictionaries together

list1 = ["city", "country", "continent"]
list2 = ["Amsterdam", "Netherlands", "Europe"]

answer = { list1[i]: list2[i] for i in range(0,3)}

numbers = [5, 6, 7, 8]
planets = ["Jupiter", "Saturn", "Uranus", "Neptune"]

zipped_planets = {numbers[i]: planets[i] for i in range(0,3)}
print(zipped_planets)


legs = [2, 4, 6, 8]
animals = ["humans", "cats", "bees", "spiders"]
combined_legs = { legs[l]: animals[l] for l in range(0,3)}
print(combined_legs)

#dict comprehension 2

animal = [["name", "Len"], ["sort", "cat"], ["age", "2"]]

answer = {i[0]: i[1] for i in animal}

#Difference between dictionary comprehension and set comprehension
{x:**2 for x in range(10}
{x**2 for x in ranger(10)


 # dictionary comprehension within function. Make a dict with how many times a letter is found in a string

def letter_count(string):
    return {letter: string.count(letter) for letter in string}

print(letter_count("I love Python"))

# Enter a string and see how many times the letters from a certain word or group of letters appear in that string
def happy_count(string):
    lower = string.lower()
    return {letter: lower.count(letter) for letter in lower if letter in "happy"}

print(happy_count("There are many people in Versailles"))

# Create a dictionary in which you add values to keys

def create_dictionaries(keys, values):
    collection = {}

    for idx, val in enumerate(keys):
        if idx < len(values):
            collection[keys[idx]] = values[idx]
        else:
            collection[keys[idx]] = None
    return collection

print(create_dictionaries("happy","day"))

# Dict methods----------

# .clear() clears the whole dictionary

# .copy() creates a new dictionary that is identical to the first one 

collections = {'stickers': 2, 'postcards': 9, 'fridge magnets': 40} 

my_collections = collections.copy()

# .fromkeys() used on an empty dictionary. You can set all the values to None or unknown, or something like that

stars = ["moons", "planets", "asteroids"]

start_solar_system = dict.fromkeys(stars, None)

print(start_solar_system)

# get() if a requested key does not exist, it returns None, instead of an error

# pop() use the key of what you want to remove. You have to put something in because dictionaries have no order
collections = {'stickers': 2, 'postcards': 9, 'fridge magnets': 40}
collections.pop("stickers")


# popitem() removes a random key from a dictionary

#keys() returns the keys of the dictionary as a list 

# update() adds everything from the dictionary between () and adds it. You can overwrite what is there too

# values() returns the values of the dictionary as a list

# items() returns both keys and values 




