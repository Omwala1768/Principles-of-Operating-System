import threading
import time
import random

BUFFER_SIZE = 5
buffer = [None] * BUFFER_SIZE

in_index = 0
out_index = 0

mutex = threading.Lock()
empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)

def producer():
    global in_index

    for i in range(10):
        item = random.randint(1, 100)

        empty.acquire()

        with mutex:
            buffer[in_index] = item
            print(f"Producer produced: {item} | Inserted at position {in_index}")
            in_index = (in_index + 1) % BUFFER_SIZE
            print("Buffer:", buffer)

        full.release()
        time.sleep(random.uniform(0.5, 1.5))

def consumer():
    global out_index

    for i in range(10):
        full.acquire()

        with mutex:
            item = buffer[out_index]
            buffer[out_index] = None
            print(f"Consumer consumed: {item} | Removed from position {out_index}")
            out_index = (out_index + 1) % BUFFER_SIZE
            print("Buffer:", buffer)

        empty.release()
        time.sleep(random.uniform(0.5, 1.5))

print("Om Wala S119")
print("Producer-Consumer Bounded Buffer Problem")
print("Buffer Size:", BUFFER_SIZE)
print()

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("\nAll items produced and consumed successfully.")
