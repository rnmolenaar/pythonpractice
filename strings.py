# string escape sequences
# \n creates a new line
#  \\ to create a backslash
# \" to keep the double quotes if you have double quotes surrounding the string

## String concatenation: you can use += for words as well
string_name = "hello" 
string_name += " friend".

#string index starts with 0



#slicing a string

name = "Napoleon Bonaparte"
slicing_names = name[0:12:4]
print(slicing_names)

#slicing if you only want the letters up until a certain index

name = "Napoleon Bonaparte"
slicing_names = name[:11]
print(slicing_names)

# slicing going backwards
name = "Napoleon Bonaparte"
slicing_names = name[::-2]
print(slicing_names)
