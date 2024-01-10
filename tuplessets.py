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
# no duplicate values. no order. No index because no order. 

set = {"a", "b", "c"}

# sets often used to remove duplicates

favorite_fruits = ["apples", "bananas", "apples", "strawberries", "kiwis", "kiwis"]
print(set(favorite_fruits)) # {'strawberries', 'bananas', 'kiwis', 'apples'}

