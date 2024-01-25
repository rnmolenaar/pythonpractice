import random

python_info = ["With random.choice(listname), you can pick a random item from a list",
   "The Zen of Python",
   "Subscripting: If you want the specific character from a string: "Hello"[0]",
   "To uncomment in pycharm: control / 0", 
   "Variables can be reassigned at any time",
   "If you do range(number), it will count from 0 until that number",
   "assigning several variables at once: at, the, same, time = 1, 2, 3, 4",
   " Range goes up until last number -1. Lists start counting from 0",
   " 273_733_378 is the same as using , in between, to make it clearer to read",
   "if statements are also called conditional statements",
   "Randint has a range, but it includes both endpoints", 
   "A variable can start with a letter or an underscore",
   "If you do several "if" and multiple apply, then you get all those things happen",
   "None can be assigned to a variable when something doesn't apply, like some people with dogs have their dogs age there, but people without dogs have None",
   "If you want to use input(), make sure you wrap it in int() if you want to use the number as an integer", 
   "print(string_name.upper()",
   'Primitive Data types: integer, float, Boolean, string", 
   "a function tied to an object is called a method: object.method()",
   "With shuffle, you can shuffle a list",
    "math.sqrt() to find the square root of a number,           
   "if you want to know what version of Python you are using, use print('sys.version')",
   "Iterable: lists, strings, dictionaries, sets, tuples: something that can be iterated over",
   "print(time.time()) to get local time in seconds after 1-1 1970. This is called the Epoch",
   "time.sleep()to put a pause for x in range(0, max): print(x)time.sleep(0.012)",
   "Slicing a string with index [start:stop:step]",
   "TensorFlow is a module related to machine learning",
   "SciPy is a module related to algoritms for scientific computing",
   "PyTorch is a library for irregular input data.",
   "class Skyscrapers(Buildings): here Skyscrapes is a child class of Buildings",
   "ntfy can be used to send SMS by phone",
   "MicroPython is being used to write Python code to control hardware. There is no C necessary",
   "NumPy is a library to work with numbers in Python",
   "Add root.mainloop() at the end to make Tkinter work",
   "Pip helps install new libraries.",
   "BeautifulSoup is a library for scraping the web",
   "Pandas is the most used library in Python. It's used for data analysis",
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
   "Dynamic Typing= types of variables can change easily in Python by assigning something else to them C++ is statically types, in contrast",
   " 2 ** 3 ** 2 is hetzelfde als 2 ** (3 ** 2)",
   " \n new line",
   "interpolate = with an f string. you convert data types into a string",
   " f string: anything happening between {} is regular python, so you can put round() there for instance",
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
   "Functional programming: a paradym, just like OOP",
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
   "tuple is immutable. tuple is faster. there is always a komma (3) is not a tuple. (3,) is a tuple",
   "dynamically typed language is when the type of a variable is checked during run time",
   "Tuples can be a key in dictionary. Like with coordinates of a location {(coord,coord)Amsterdam Zoo} Can't use a list as a key",
   "Tuple method: count. the number of times a value is in a tuple. tuple.count('happy')",
   "Index: where a value is found inside the tuple",
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
   "Put global in the function: global variable_name to give the function access to it", 
   "Docstrings: triple quotes used inside a function to explain what it does",
   "Replace function let's you replace a string with something else. stripped = string.replace(' ', '').lower()",
   "The 4 primitive data structures: integers, float, string, and boolean",
   "If you want to count how often something appears in a list: return lst.count(searchTerm)",
   "args used to pass in multiple arguments. You don't have to specify them when defining the function",
   "if you use a return in a conditional at the end, you don't need an else for that last possibility",
   "kwargs ** stores them in a dictionary",
   "Parameter ordering: parameters, *args, default paramters, **kwargs",
   "If you want to insert a list in args and use the individual numbers, put in *list when calling the function",
   "If you want to make a function with caps for first letter: return string[:1].upper() + string[1:]",
   "lambda is like a function that has no name. Can only be one line. aka Anonymous functions. Automatically returned.",
   "lambda a, b: a + b.(the first a and b are parameters)",
   "lambda is used when you want to pass a function into a function", 
   "map is a build-in function that can be used with lambdas. Two arguments: iterable and a function",
   "map runs the lambda over the iterable and returns a map object. This can be converted into another data structure",
   " double_it = map(lambda x: x*2, nums). Turn into a list by list(double_it)",
   "build in function all(): returns True if everything in the iterable is truthy or empty.",
   "Generator expressions (less memory) or list comprehensions. GE when you iterate once. LC when you want to store the result",
   "sorted is built in function. makes a copy and doesn't change the original like the .sort() method for lists",
   "You can change the direction fort- sorted() by setting reverse=True. It's alphabetical.",
   "To use emojis, you can install the emoji module",
   "There is a Wikipedia module. There is a Wikipedia API that helps get information from Wikipedia ",
   "sorted() reverse= True to do it backwards, key=lambda to sort by a certain keyword then add another word to sort by key username:  ",
   "build in reversed function takes in an iterable. Different from reverse method in list. This can be used with strings",
   "len can also be used with a dictionary based on the amount of key value pairs",
   "Len and OOP: you can tell it what you want the length of REVIEW",
   "abs: returns the absolute value of a number. Negative numbers turn into positive ones", 
   "dir function returns all properties and methods of an object, without values", 
  "fabs treats everything as a float. Need the math module", 
  "Sum: the sum of all plus the start. Start by default is 0: sum([1, 4, 5], 12) 12 is the start here", 
   " ''.join(sequence) is a fast way to concotenate a series of iterables",
   " round() to round up. If you want it to a certain decimal, specify that: round(6.7262, 2)",
   "Zip function: pairs up the first two numbers from two lists, then the second ones etc with a ",
   "The opposite of zip is when you do (zip(*zipped_list)). It will unzip them because of the *)",
   "SyntaxError: something that isn't valid Python. Like you forget () when defining a function", 
   "NameError: When something is not defined yet.",
   "KeyError: when a specific key does not exist in the dict",
   "ValueError: int('Letters') is a ValueError. you cannot convert this to an integer",
   "TypeError: when the wrong type is used. Like you to addition and one of them is a string", 
   "AttributeError: some method does not exist, like [1, 2, 3].happy().",
   "ZeroDivisionError: When you try to divide something by 0",
   "IndexError: when an index is asked for that doesn't exist", 
   "raise TypeOfError ('message you want displayed')",
   " try/except blocks: You try something and if these is an exception, whatever is under except: will happen", 
   "Don't try to catch every error with one try/except block. It will make it difficult to understand what the problem is", 
   "Else and finally don't have to be there in the try/except blocks", 
   "Else will run when except does not. So if there is not a problem else will run", 
   "Finally will run no matter what. Is not that commonly used",
   "try/except/else/finally works well with a loop", 
   "You can define several except in a function, for each error you want to antipate",
   "You can do one except for multiple types of errors if you usea tuple", 
   "PDB is Python debugger. It's a module that you don't have to install",
   "A silent bug: code doesn't break, but gives you a different result than expected",
   "pdb.set_trace() can be put in a line. Everything about it runs, but then it stops. Anything below doesn't exist yet", 
   "You don't keep pdb.set_trace() in your code", 
   "pdb.set_trace() has several commands. c is to quit",
   "random.choice method picks something random from a list", 
   "import module_name as whatever_name_you_want_to_give_it. This is usually done to make something shorter rand.choice",
   "from is used to precisely specify what you want", 
   " * to import everything",
   " from random import randint, choice, shuffle to only import the methods you need. Then you don't need to do random.choice, but just choice",
   "If you create functions on a seperate file, you can just call the specific functions when importing from file import function",
   "Make a module if you want to use code in more than one place. If your file is very" 
   "if you want to import a function from another file in the same directory, filename.functioname()",
   "Import random vs from random import * : 1st imports everything as an attribute on random", 
   "Custom module; one you made yourself. External module: made by others.",
   "PyPI: Python package index. You can find more modules there.",
   "You can download external modules with pip. Comes with Python by default",
   "print(dir(module_name)): to see what's in a module", 
   "help with module, explains a lot more about what you can do with a module", 
   "Module Pyfiglet package for ASCII", 
   "autopep8 package helps clean up code", 
   " dunder double underscore __. You're not supposed to touch them ", 
   "__init__(self, ...) is used when an object is created from a class",
   " __name__ variable: if it's the file being run it's __main__",
   "OOP: is used to create things that actually exist in Python, like a car or a robot", 
   "Class is a blueprint for every instance/object", 
   "There can be methods etc in classes", 
   "Lists are also a class that you can do certain things with. A specific list is an instance of the class lists",
   "Inheritance: an object can be part of a class that sits in another class. Just like classifying animals", 
   "Encapsulate: is done to encapsulate code in hierarchical classes", 
   "_private: to make it clear this should be only used in a given class", 
   "Abstraction: hiding unnecessary information from a user. Related to OOP", 
   "use CamelCase when defining classes. And singular", 
   "Classes can have a __init__ method. This gets called every time you make an object of the class", 
    "self refers to the objects, whatever comes after that can be put in: self.name =", 
   "Private methods, attributes do not exist in Python", 
    "Class: attributes: what it has. Methods: what it does",            
   "Use f strings + self.attribute to make the attribute (like age or first name) come back",
   "Class attributes are not static. You can change them. It is something that belongs to an object, like its speed or name", 
   "Self needs to be there for every defined instance method",          
   "Class attribute is defined only once. They are shared by all instances. Do it at the top under Class   :",
   "Class attributes: you don't refer to the instances any more. You don't use self.",           
   "id() shows you the exact memory location of something in Python. To check if two variables/objects refer to the same location in memory",
   "@classmethod (this is a decorator). then def and classmethod_name(cls)", 
   " __repr__ method (dunder method) used to have a class’s object as a string", 
   "encapsulating: binding methods and variables together and stopping them from being accessed by other classes. A class is an example of encapsulation", 
   "Abstraction:  hide the inner working from other users. Only show relevant data in a class interface",
   "Class method implicit first argument = cls, instance method = self", 
   "Class method is @classmethod. Used when a method doesn't need to know about a specific instance",
   "If you put an argument in when creating a class, it means that this class inherits from that other class",             
   "isinstance() is a Boolean method that shows if something is an instance of a certain class", 
   "_age: makes age private for a specific class", 
   " @property whatever you define underneath it, can be called underneath", 
   "Getters: methods used in OOP to access the private attributes of a class", 
   "Setters: methods used in OOP to set the value to private attributes in a class", 
    "super() isn't of the class refers to the parent class. Don't have to specify self in this way", 
   "Multiple inheritance: when a class inherits from multiple classes", 
   "MRO: Method Resolution Order: this is the order that Python looks for methods on instances of a class",        
   "To find out MRO: __mro__ attribute, mro() method, help(cls)", 
   "print(CLASSNAME.__mro__)" help(CLASSNAME)",
   "Polymorphism: OOP: An object can take on many forms. One method works in similar way for different classes. The same operation works for different types of objects",
   "Method overriding: similar method in parent and child class, so the parent method is overridden", 
   "NotImplementedError: you can raise this if every child class needs a specific method to be set. So if it's not set, the error will show up",
   "magic methods: dunder methods", 
  "iterators: objects that can be iterated upon. Something you run a for loop on. next() can be run upon it", 
  "iterable: objects that will return an iterator when iter() is used on it (next doesn't work on iterables)", 
  "A string or list is not an iterator. It's iterable", 
  "when next() is put on an iterator, the iterator returns the next item.", 
  "StopIteration error: raised when there is nothing to be called upon any more", 
  "iter= returns the iterator on an iterable object. It needs to return an iterator", 
  "the iterator returns the next item", 
  "Generators are a subset of iterators: a short way of creating iterators", 
   "Generators can be made by generator expressions and generator functions (they used the yield keywords)", 
   "Generator functions: instead of using 'return', 'yield' is used. Can yield more than once. It returns a generator",
  "If you put 'yield somewhere in a function, it will give you a generator object", 
   "A generator is returned from a generator function", 
   "You don't always have to put in a list of date. You can also use a generator expression", 
   "generator functions are not declared with the def keyword, unlike normal functions", 
   "generator expressions look and act like list comprehension",
   "higher function returns another function from inside or accepts a function as an argument", for
    "Decorator is a function that wraps other functions and changing its behavior",
    "Decorators are an form of higher order functions and a @ should be used", 
    "Decorators with different signatures: when one function has a different amount of arguments than the other. We use args and kwargs for that",
    "A module named 'functools' is there for higher order functions", 
    "wraps are used to preserve the name and docstrings of a function that is decorated", 
    "Test Driven Development: you first write tests and then write the codes", 
    "TDD: write a test that fails, green: write the least amount of code to make the test pass, refactor: clean up code", 
    "Assert tests if a condition is True. If not an AssertionError will be raised".
    "Assertions: assert accepts an expression. Returns None if expression is truthy. If falsy: AssertionError", 
    "assert is a statement. Not a function", 
    " -o assertions won't be evaluated", 
    "doctests: tests for functions inside the docstring. Write like it's in a REPL. >>>", 
    "REPL: Read, Evaluate, Print, and Loop", 
    "File I/O: input output. Important for data science and webdevelopment", 
    "Python uses a cursor when reading a file. So after doing a read method on them, they are at the end of the line", 
    "You can move the cursor with the seek method. file.seek(0) to get to the beginning",
    "file.readline() can be used to read a file line by line. The cursor moves along", 
    "file.readlines() creates a list with each line", 
    "file.close() necessary to save space. You will need to open it again afterwards",
    " with open("filename.txt") as file:    file.read(). You don't have to close it anymore",
    " f.__exit__()"
    "If you want to write to a file, add a w like so: ("filename.txt", "w") as file:", 
    "The original contents are overwritten with w",
    "Data types, text type
    "A tuple is ordered and unchangeable. Set is unordered and unchangeable",
    "To use SQL with Python, Python needs an SQL driver",
    "No Boolean in SQL", 
    "SQL COMMANDS IN CAPITALS", 
    
    
    
    
    
    
               
               
               
               

               ]

print(random.choice(python_info))
