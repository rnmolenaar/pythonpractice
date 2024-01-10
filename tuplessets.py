# tuple immutable and ordered. Faster than lists. Safer from bugs. Tuples can be used as keys in dict. 
# can use slices

# some dict methods return tuples in a list, like .items()
earth = { "life": True, "inner planet": True, "moon": 1, "size_ranked": 5}

planet = earth.items()
print(planet)

# tuple methods

# .count() how many times something is in a tuple

tuple_name.count(name)

#.index() what is the index of (something). Only shows the first occassion. 

########### Sets
# no duplicate values. no order. No index because no order. Mutable as you can remove things

set = {"a", "b", "c"}

# sets often used to remove duplicates

favorite_fruits = ["apples", "bananas", "apples", "strawberries", "kiwis", "kiwis"]
print(set(favorite_fruits)) # {'strawberries', 'bananas', 'kiwis', 'apples'}

# set union: when you want to remove duplicates from two sets

favorite_fruits_peter = {"apples", "bananas", "strawberries", "kiwis"}
favorite_fruits_petra = {"apples", "mango", "kiwis", "peaches"}
total = favorite_fruits_petra | favorite_fruits_peter
print(total) # {'peaches', 'kiwis', 'bananas', 'apples', 'strawberries', 'mango'}

# set intersection: check which exist in both sets

favorite_fruits_peter = {"apples", "bananas", "strawberries", "kiwis"}
favorite_fruits_petra = {"apples", "mango", "kiwis", "peaches"}
total = favorite_fruits_petra & favorite_fruits_peter
print(total)



## set methods

# .add() can only be added once because duplicates don't work

# .clear() removes everything

# .copy() makes a duplicate. Not at the same location, just like with methods for lists and disctionary

# .discard() removes somethingbut doesn't give an error if the thing isn't there in the first place

# .remove() KeyError if the ("value") isn't there

set.remove("value")

