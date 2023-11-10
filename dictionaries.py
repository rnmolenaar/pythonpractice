
#Make a dictionary
character = {"name": "Smiley", "fan of": "River music", "Speaks": "A language"}

# How to add values of different keys together in a dictionary

person = {
    "first": "Janie",
    "last": "Grey",
}

full_name = person["first"] + " " + person["last"]


# running a for loop on the values in a dictionary. You only get the values with this

for value in dictionary.values():
    print(value) 
# You can also do .keys() is the same as above

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

    
