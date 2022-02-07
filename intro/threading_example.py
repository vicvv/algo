import random
import time
import threading


def loop(thread_name, n):
    for i in range(n):
        # Sleep for up to 20 milliseconds.
        time.sleep(random.randint(1, 20) / 1000)
        print(f"Thread {thread_name}: {i}")


# TODO: As an exercise, try to change this code to let
# t1 finish first before t2 starts running. (Hint: A
# mutex lock should do the trick)
t1 = threading.Thread(target=loop, args=("t1", 10))
t2 = threading.Thread(target=loop, args=("t2", 10))

t1.start()
t2.start()

t1.join()
t2.join()