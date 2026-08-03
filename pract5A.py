import threading
from concurrent.futures import ThreadPoolExecutor

print("Om Wala S119")

def fibonacci(n):
    a, b = 0, 1
    sequence = []

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return threading.current_thread().name, sequence

numbers = [5, 8, 10, 12]

with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(fibonacci, numbers))

total_terms = 0

for name, sequence in results:
    print(f"\n{name}")
    print("Fibonacci Sequence:", sequence)
    total_terms += len(sequence)

print("\nTotal Fibonacci terms generated:", total_terms)
