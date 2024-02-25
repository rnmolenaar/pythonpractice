### strings are immutable


# string escape sequences
# \n creates a new line
#  \\ to create a backslash
# \" to keep the double quotes if you have double quotes surrounding the string

## String concatenation: you can use += for words as well
string_name = "hello" 
string_name += " friend".

#string index starts with 0

# multiply strings
print("Happy birthday" * 20)

#slicing a string (syntax same as for slicing a list)

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

### string methods. 

# .capitalize() will capitalize only the first letter of a string

# .endswith() shows if a string ends with a certain something

print("Oostenrijk".endswith("k"))

# lstrip(removes all white space on the left side of the string


# .replace() When you want to replace parts of a string

 string.replace(" ", "").lower()

# .rstrip() removes all the white space on the right side of a string



# .lower()
# .replace()

tale ="onck upon a timk"

print(tale.replace("k", "e"))"

# .startswith() shows if something starts with something and gives back a Boolean

"happy".startswith("h")

# .strip() strips white space on both sides

# .swapcase() lower case letters become upper case and the other way around

song= "i LIKE DANCING IN THE SUN".swapcase()
print(song)


# .title() will capitalize the first letter of every word

# .upper() to make everything uppercase

city = "amsterdam".upper()




 
