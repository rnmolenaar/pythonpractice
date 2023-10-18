import time

def counting_time(max):
    t1 = time.time()
    for x in range(0, max):
       print(x)
    t2 =  time.time()

    print("it took %s seconds" % (t2 - t1))

counting_time(1718)

# to put a pause in

import time


def counting_time(max):
    t1 = time.time()
    for x in range(0, max):
        print(x)
        time.sleep(0.012)
    t2 = time.time()

    print("it took %s seconds" % (t2 - t1))

counting_time(171)
