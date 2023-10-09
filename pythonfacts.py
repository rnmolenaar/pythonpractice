import random

python_info = ["With random.choice(listname), you can pick a random item from a list",
               "With shuffle, you can shuffle a list",
              "if you want to know what version of Python you are using, use print("sys.version"),
              "print(time.time()) to get local time in seconds after 1-1 1970. This is called the Epoch",
              "time.sleep()to put a pause for x in range(0, max): print(x)time.sleep(0.012)"
              "TensorFlow is a module related to machine learning" 
              "SciPy is a module related to algoritms for scientific computing,
              "PyTorch is a library for irregular input data."
              "class Skyscrapers(Buildings): here Skyscrapes is a child class of Buildings",
              "ntfy can be used to send SMS by phone", 
              "MicroPython is being used to write Python code to control hardware. There is no C necessary",
              "NumPy is a library to work with numbers in Python",
              "Add root.mainloop() at the end to make tkinter work",
              "Pip helps install new libraries.",
              "BeautifulSoup is a library for scraping the web",
              "Pandas is the most used library in Python. Data analysis",
              " __init__ method is used in object oriented programming. Called whenever an object is created from a class.",
              
              }
  print(random.choice(python_info))
