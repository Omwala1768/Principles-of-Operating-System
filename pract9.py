from collections import deque

print("Om Wala S119")
print("MEMORY MANAGEMENT TECHNIQUES")
print("-" * 50)

def fifo_page_replacement(pages, frames):
    memory = []
    queue = deque()
    hits = 0
    misses = 0

    for page in pages:
        if page in memory:
            hits += 1
        else:
            misses += 1

            if len(memory) < frames:
                memory.append(page)
                queue.append(page)
            else:
                old_page = queue.popleft()
                memory.remove(old_page)
                memory.append(page)
                queue.append(page)

    hit_ratio = hits / len(pages)
    miss_ratio = misses / len(pages)

    return hits, misses, hit_ratio, miss_ratio


def lru_page_replacement(pages, frames):
    memory = []
    hits = 0
    misses = 0

    for page in pages:
        if page in memory:
            hits += 1
            memory.remove(page)
            memory.append(page)
        else:
            misses += 1

            if len(memory) >= frames:
                memory.pop(0)

            memory.append(page)

    hit_ratio = hits / len(pages)
    miss_ratio = misses / len(pages)

    return hits, misses, hit_ratio, miss_ratio


def display_results(pages, frames):
    fifo_hits, fifo_misses, fifo_hit_ratio, fifo_miss_ratio = \
        fifo_page_replacement(pages, frames)

    lru_hits, lru_misses, lru_hit_ratio, lru_miss_ratio = \
        lru_page_replacement(pages, frames)

    print("\nPage Reference String:")
    print(pages)

    print("\nNumber of Frames:", frames)

    print("\nFIFO Page Replacement")
    print("Hits       :", fifo_hits)
    print("Misses     :", fifo_misses)
    print("Hit Ratio  :", round(fifo_hit_ratio, 2))
    print("Miss Ratio :", round(fifo_miss_ratio, 2))

    print("\nLRU Page Replacement")
    print("Hits       :", lru_hits)
    print("Misses     :", lru_misses)
    print("Hit Ratio  :", round(lru_hit_ratio, 2))
    print("Miss Ratio :", round(lru_miss_ratio, 2))


pages = list(map(int, input(
    "\nEnter page reference string (space separated): "
).split()))

frames = int(input("Enter number of memory frames: "))

if frames <= 0:
    print("Number of frames must be greater than 0.")
else:
    display_results(pages, frames)

    print("\n" + "-" * 50)
    print("COMPARISON FOR DIFFERENT MEMORY FRAME SIZES")
    print("-" * 50)

    print("\nFrames | FIFO Hits | FIFO Misses | LRU Hits | LRU Misses")
    print("-" * 55)

    for f in range(1, frames + 1):
        fh, fm, _, _ = fifo_page_replacement(pages, f)
        lh, lm, _, _ = lru_page_replacement(pages, f)

        print(f"{f:^6} | {fh:^9} | {fm:^11} | {lh:^8} | {lm:^10}")
