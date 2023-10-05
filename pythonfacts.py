import random

python_info = ["With random.choice(listname), you can pick a random item from a list",
               "With shuffle, you can shuffle a list",
              "if you want to know what version of Python you are using, use print("sys.version"),
              "print(time.time()) to get local time in seconds after 1-1 1970. This is called the Epoch",
              "time.sleep()to put a pause in  for x in range(0, max): print(x)time.sleep(0.012)"
              "TensorFlow is a module related to machine learning" 
              "SciPy is a module related to algoritms for scientific computing"
              "PyTorch is a library for irregular input data."
              "class Skyscrapers(Buildings): here Skyscrapes is a child class of Buildings",
              "ntfy can be used to send SMS by phone", 
              "MicroPython is being used to write Python code to control hardware. There is no C necessary"
              }
  print(random.choice(python_info))
