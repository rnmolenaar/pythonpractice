nums = [1, 2, 3, 4]
print([num*5 for num in nums])

#List comprehension is more concise than doing a for loop


nums = [1, 2, 3, 4]

string_nums = [str(num) for num in nums]
print(string_nums)


#other example

Dividableby12 = [num for num in range(1,101) if val % 12 == 0]

# no vowels
answer = [letter for letter in 'partook' if letter not in 'aeiou'] 

for list2 in nested_list:
  for val in list2:
    print(val)

#
lists = [[l for l in range(0,30)] for num in range(0,30)]

# if you want to use it with a function
def even_numbers():
    return [x for x in range(1,40) if x%2==0]

#check if something is in both lists


# flesh out intersection pleaseeeee
def check_two_lists(list1, list2):
    return[val for val in list 1 if val in list2]

# To check if all are strings in a list

def all_strings():
    
    return all([type(l) == str for l in lst])
  
   
   
