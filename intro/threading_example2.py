import threading
from time import sleep
import math


def append_values(lst, values=[], delay=1):
    for value in values:
        lst.append(value)
        sleep(math.ceil(abs(delay)))


def append_integer(lst, integer):
    lst.append(integer)


lst = []

# Write your code here.

thread1 = threading.Thread(target=append_values, args=(lst, [1, 3, 5], 1))
thread2 = threading.Thread(target=append_integer, args=(lst, 4))
thread3 = threading.Thread(target=append_integer, args=(lst, 3))
thread1.start()
thread2.start()
thread1.join()
thread3.start()