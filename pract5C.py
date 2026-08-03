import threading

print("Om Wala S119")

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"\nFactorial of {n} = {fact}")

if __name__ == "__main__":

    numbers = [5, 7, 10]
    threads = []
    for num in numbers:
        t = threading.Thread(target=factorial, args=(num,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nAll threads completed.")
