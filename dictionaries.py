
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

# fromkeys method
start = dict.fromkeys(dictionary_name, 0)

#dictionary comprehension
{num:("even" if num % 2 ==0 else "odd") for num in range(0, 20)
    
# dict comprehension: zipping two dictionaries together

 list1 = ["city", "country", "continent"]
list2 = ["Amsterdam", "Netherlands", "Europe"]

answer = { list1[i]: list2[i] for i in range(0,3)}

#dict comprehension 2

animal = [["name", "Len"], ["sort", "cat"], ["age", "2"]]

answer = {i[0]: i[1] for i in animal}

#Difference between dictionary comprehension and set comprehension
{x:**2 for x in range(10}
{x**2 for x in ranger(10)
