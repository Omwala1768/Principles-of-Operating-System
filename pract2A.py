from queue import Queue
from threading import Thread
import time

print("Om Wala S119")
q = Queue(maxsize=3)

def producer():
    for i in range(1, 7):
        print("Producing:", i)
        q.put(i)
        time.sleep(1)

def consumer():
    for i in range(1, 7):
        item = q.get()
        print("Consumed:", item)
        time.sleep(2)

t1 = Thread(target=producer)
t2 = Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()

print("Program Finished")
