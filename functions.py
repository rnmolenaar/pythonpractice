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


