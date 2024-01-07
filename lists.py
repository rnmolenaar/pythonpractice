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

