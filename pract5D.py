import threading

print("Om Wala S119")
lock = threading.Lock()

def print_even():
    with lock:
        print("Even Numbers:")
        for i in range(2, 21, 2):
            print(i, end=" ")
        print("\n")


def print_odd():
    with lock:
        print("Odd Numbers:")
        for i in range(1, 21, 2):
            print(i, end=" ")
        print("\n")

def reverse_string(text):
    with lock:
        print("Original String :", text)
        print("Reversed String :", text[::-1])
        print()

if __name__ == "__main__":

    text = "Multithreading"

    t1 = threading.Thread(target=print_even)
    t2 = threading.Thread(target=print_odd)
    t3 = threading.Thread(target=reverse_string, args=(text,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("All threads completed.")
