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
answer = [[l for l in range(0,30)] for num in range(0,30)]
