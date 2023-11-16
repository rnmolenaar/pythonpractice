#make a function where the inserted will be returned in capitalized letters

def big_letters(insert):
    return f"{insert.upper()}!"

#return breaks you out of the function. So make sure everything is done that needs to be done. Watch indentation
def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total


print(sum_odd_numbers([0, 12, 13, 17, 19, 20, 345, 3738392]))

# to count how often something is present in a given argument

def count_m(word):
    count = 0
    for char in word:
        if char == 'm':
            count += 1
    return count

# function with two parameters

    def multiply(a,b):
        return a*b

# 

    def weekday(num):
        days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
      
        if num > 0 and num <= len(days):
             return days[num-1]
        return None

# check if a list is empty

def last_element(lst):
    if lst:
        return lst[-1]
    return None

# check how often one appears in the other. See it as string.count(letter)

def letter_count(string, letter):
    return string.lower().count(letter.lower())
    
# functions and slicing from backwards

def palindrome_check(string):
    return string == string[::-1]

# Create a function to see how often something comes up in a list
def frequency(lst, searchTerm):
   return lst.count(searchTerm)

# args You need the star to do it. Args is a tuple

def AnyFunction(*args):
    total = 0
    for num in args:
        total += num
    return total
    
# if you want to make a function to capitalize the first letter of a string. The right part is to add the rest of the string
def capitalize_first(string):
    return string[:1].upper() + string[1:]

# if you want to only print the truthy values in a list

def truthyList(lst):
    return [val for val in lst if val]

print(truthyList([1, 0, True, False]))

#lambda and tkinter. Lambda saves you from having to define functions for each buttons that are not used anywhere else

command=lambda: print("clicked")

# lambda and cube

cube = lambda num: num ** 3




