import threading
import time

print("=== Om Wala S119 ===")


def task(task_no):
    print(f"Task {task_no} started")
    time.sleep(2)
    print(f"Task {task_no} ended")

print("\nSequential Execution\n")

start = time.time()

for i in range(1, 5):
    task(i)

end = time.time()

print(f"\nSequential Execution Time: {end - start:.2f} seconds")

print("\nThreaded Execution\n")

threads = []

start = time.time()

for i in range(1, 5):
    t = threading.Thread(target=task, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end = time.time()

print(f"\nThreaded Execution Time: {end - start:.2f} seconds")
