# data types in Python

text_type = ["str"]
### Strings
# strings are any unicode character


numeric_type = ["int", "float", "complex"]

mapping_type = ["dict"]

sequence_type = ["list", "tuple", "range"]

set_type = ["set", "frozenset"]

###
boolean_type = ["bool"]
# Games often start in this way
 game_over = False

# Methods in Python

#string methods
#strip(). You can also use .lstrip() or rstrip() to only strip on one side 

goodmorning = "      goodmorning       "
stripped_goodmorning = goodmorning.strip()

print(goodmorning)
print(stripped_goodmorning)

# upper and lower. Result is SHOUT
shout = "shout"

shout_loud = shout.upper()
print(shout_loud)

# replace. Result is "I prefer books"

original = "I prefer video games"

new_text = original.replace("video games", "books")

print(new_text)








