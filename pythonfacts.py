import random

python_info = ["With random.choice(listname), you can pick a random item from a list",
               "With shuffle, you can shuffle a list",
               "if you want to know what version of Python you are using, use print('sys.version')",
               "print(time.time()) to get local time in seconds after 1-1 1970. This is called the Epoch",
               "time.sleep()to put a pause for x in range(0, max): print(x)time.sleep(0.012)",
               "TensorFlow is a module related to machine learning",
               "SciPy is a module related to algoritms for scientific computing",
               "PyTorch is a library for irregular input data.",
               "class Skyscrapers(Buildings): here Skyscrapes is a child class of Buildings",
               "ntfy can be used to send SMS by phone",
               "MicroPython is being used to write Python code to control hardware. There is no C necessary",
               "NumPy is a library to work with numbers in Python",
               "Add root.mainloop() at the end to make tkinter work",
               "Pip helps install new libraries.",
               "BeautifulSoup is a library for scraping the web",
               "Pandas is the most used library in Python. Data analysis",
               " __init__ method is used in object oriented programming. Called whenever an object is created from a class.",
               "Flask is a web framework. It handles the backend of a website that can communicate with the frontend",
               "There is a Python packages index",
               "Post to send to the server. Can be added in html file (form tag)",
               "Tensorflow for algorithms",
               "pythonanywhere.com to load up files on machine. Can use github for that",
               " list methods. append: to add to the end of a list, copy: returns a copy of the list, clear: removes all items from the list",
               " list methods. count: counts how many times an element is in the list, extend: you can add more than one to a list",
               " list methods. index: returns the lowest index where the element appears, insert: adds element to the index number provided",
               " list methods. pop: removes and returns the last value or a given one",
               "list method index: you can specify where in the list you want to look. list,index('word', 2, 5)",
             "list method: remove: you name the actual name of what is in the list and the first one of that is removed",
               "list method pop: if no index is specified, the last is removed",
               "list methods: reverse: changes the order from start to finish, sort: sorts the list.",
               "list methods: min: calculates the minimum of all elements in the list, calculates the max",
               "string method: join is for strings but used to convert lists to strings",
               "dunder methods allow instances of a class to interact with the built-in functions and operators.",
               "Event driven architectures: EDA. Split applications",
               "function touch {New-Item -ItemType File -Name ($args[0])}",
               "command slash to comment or remove comment",
               "square root 2 ** 0.5",
               "// is integer division",
               "assign multiple variables at once: all, at, once = 2, 3, 4",
               "== operator to compare the values of two objects. The is operator compares the identity of two objects.",
               "Dynamic typing= types can change easily in Python",
               " 2 ** 3 ** 2 is hetzelfde als 2 ** (3 ** 2)",
               " \n new line",
               "interpolate = with an f string. you make something part of the string",
               "if num % 2 != 0:",
               "naturally false things: 0, false conditional checks, empty objects, empty strings, None",
               "if variable: then it checks if there is something in it and therefore truthy",
               "lexigraphical ordering a > b",
               "Difference between is and == is that == checks if the values are the same. Is checks if it is the same thing in memory",
               "Control 0D to duplicate in Pycharm",
               "random.randint(0, 100) if only random is imported. If randint specifically, no need for random",
               "input(something with quotation marks ).lower()",
               "ranges used with for loops only it seems",
               "list.index('Temenos') specifies what index Temenos has",
               "If you do range(7) it will give you the numbers 0-6",
               "anything you can do with a for look, you can do with a while loop, but not the other way around",
               "While loops run, while a condition is truthy",
               "With a while loop, you need to first declare a valuable",
               "Selenium is used for automated test cases",
               "randint is inclusive. Ranges are exclusive the last number",
               "You can convert a range into a list: list(range(1, 5))",
               "If you want to see if something is in a list, do 'green' in colors. It will give True or False",
               " ' '. join(listname) joins the words of listname into a string with what's before it as what is put between them",
               "Slicing. [] are used for this. There are three elements: list[start:end:step]",
               " 'wordddddddds'[::2] = wrddddds] one gets removed constantly",
               "swapping is possible in lists",
               "You can create a new list from another list: [x*10 for x in nums].",
               "List comprehension: to create a new list based on the values of an existing list",
               "there is a boolean function: bool()",
               " an empty string, empty list and 0 is falsy",
               "You can use conditionals with list comprehension",
               "answer = [flower[0] for flower in ['Rose', 'Lily', 'Primsose']] list comprehension",
               "answer = [letter for letter in 'partook' if letter not in 'aeiou'] to make a list with the consonants of that word ",
               "If you want to access a specific item in a nested list, do [9][1]",
               "lists = [[l for l in range(0,30)] for num in range(0,30)] outcome [[0, 1, 2], [0, 1, 2], [0, 1, 2]] note the ]",
               " .values() for dictionary. You can run a for loop on that to get all the info out",
               "if you want to add the total of values in a dictionary: total_gifts = sum(gifts.values())",
               "dict: if you want to test for the existence of keys, use in. Values is in dictionary.values()",
               "dict methods: clear empties the dict. copy makes a copy of the dict.",
               "dict method: fromkeys {}.fromkeys() if you want to set every property to whatever you want it to. You can set a range",
               "dict method: gets a key from a dict, but retrieves none instead of an error if it isn't there",
               "dict method: pop: you have to provide the key to remove key-value pair. popitem randomly removes something. No key needed",
               "dict method: update will add to another dictionary which can already have key-value pairs. Doesn't remove anything",
               "to add a key value pair to a dictionary: dict['key_name'] = 'Value'",
               "For dictionary comprehension syntax: {   : for .. in...}   ",
               "parity refers to whether a number is odd or even",
               "zip function is used to zip two dictionaries together into one",
               "A list of pairs can be turned into a dictionary using dict() dictionary1 = dict(listname)",
               "chr() function returns a string when entering ASCII code",
               "tuple is immutable. tuple is faster",
               "dynamically typed language is when the type of a variable is checked during run time",
               "Tuples can be a key in dictionary. Like with coordinates of a location {(coord,coord)Amsterdam Zoo} Can't use a list as a key",
               "Tuple method: count. the number of times a value is in a tuple. tuple.count('happy')",
               "). Index: where a value is found inside the tuple",
               "tuples can be nested and you can also slice them",
               "sets don't have order and no duplicate values. No index because no order {} are used. there is also a set function like dict function",
               "set methods: add t.add(4) only works if the value isn't there yet. Remove. t.remove(2) 2 is removed.",
               "set method: discard is you don't want to worry about errors if something isn't there. It removes something",
               "set method: copy. copies. Clear: removes everything.",
               "set math: | group two sets together. & look at those who are in both sets",
               "Tuples are ordered but sets are not",
               "DRY: dont' repeat yourself. functions help with that",
               "return exists the function. it outputs what come after return",
               "Call stack is a list of all you have to do with your code",
               "a parameter is in the declaration of the function. The argument is what's passed in when calling the function",
               "You can add a default in the parameter if no argument is given: function(parameter1, parameter2= 3)"
               "The default parameter needs to be at the end (or all parameters need one)",
               "Keyword arguments in a function allow you to call the different parameters up in another order. You need to know the keyword name",
               "Scope: variables are not always available everywhere",
               "put global in the function: global variable_name to give the function access to it", 
               "Docstrings: triple quotes used inside a function to explain what it does",
               "replace function let's you replace a string with something else. stripped = string.replace(' ', '').lower()",
               "the 4 primitive data structures: integers, float, string, and boolean",
               " If you want to count how often something appears in a list: return lst.count(searchTerm)",
               "args used to pass in multiple arguments. You don't have to specify them when defining the function",
               
               
               
               
               
               

               ]

print(random.choice(python_info))
