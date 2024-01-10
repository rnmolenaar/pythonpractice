# tuple immutable and ordered. Faster than lists. Safer from bugs. Tuples can be used as keys in dict. 
# some dict methods return tuples in a list, like .items()
earth = { "life": True, "inner planet": True, "moon": 1, "size_ranked": 5}

planet = earth.items()
print(planet)
