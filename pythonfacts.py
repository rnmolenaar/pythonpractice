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
               "list method index: you can specify where in the list you want to look. list,index("word", 2, 5)
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
               "interpolate = like an f string. you make something part of the string",
               "if num % 2 != 0:",
               "naturally false things: 0, false conditional checks, empty objects, empty strings, None",
               "if variable: then it checks if there is something in it and therefore truthy",
               "lexigraphical ordering a > b",
               "Difference between is and == is that == checks if the values are the same. Is checks if it is the same thing in memory",
               "Control 0D to duplicate in Pycharm",
               "random.randint(0, 100) if only random is imported. If randint specifically, no need for random",
               "input(something with quotation marks ).lower()",
               "ranges used with for loops only it seems",
               "list.index("Temenos") specifies what index Temenos has",
               "If you do range(7) it will give you the numbers 0-6",
               "anything you can do with a for look, you can do with a while loop, but not the other way around",
               "While loops run, while a condition is truthy",
               "With a while loop, you need to first declare a valuable",
               "Selenium is used for automated test cases",
               "randint is inclusive. Ranges are exclusive the last number",
               "You can convert a range into a list: list(range(1, 5))",
               "If you want to see if something is in a list, do 'green' in colors. It will give True or False",
               " ' '. join(listname) joins the words of listname into a string with what's before it as what is put between them",
               "Slicing. [] are used for this. There are three elements: list[start:end:step",
               " 'wordddddddds'[::2] = wrddddds] one gets removed constantly",
               "swapping is possible in lists", 
               "You can create a new list from another list: [x*10 for x in nums].",
               "List comprehension: to create a new list based on the values of an existing list",
               "there is a boolean function: bool()",
               " an empty string, empty list and 0 is falsy".
               "You can use conditionals with list comprehension",
              "answer = [flower[0] for flower in ["Rose", "Lily", "Primsose"]] list comprehension",
              "answer = [letter for letter in 'partook' if char not in 'aeiou'] "
              "
              

               
               
              
               
               
               

               ]

print(random.choice(python_info))
