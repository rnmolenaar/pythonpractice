
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

# running a for loop on items. You get both key and value in a tuple.

    
for k, v in dictionary.items():
    print(f:"key is {k} and value is {v}")
    
