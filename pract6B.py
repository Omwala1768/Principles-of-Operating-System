from collections import deque

print("Om Wala S119")

processes = [
    ["P1", 0, 5],
    ["P2", 1, 3],
    ["P3", 2, 6]
]

time_quantum = 2

def round_robin(processes, tq):

    processes = sorted(processes, key=lambda x: x[1])

    n = len(processes)
    remaining = {}
    arrival = {}
    burst = {}
    completion = {}

    for p in processes:
        remaining[p[0]] = p[2]
        arrival[p[0]] = p[1]
        burst[p[0]] = p[2]

    queue = deque()
    gantt = []

    time = 0
    i = 0

    
    while i < n and processes[i][1] <= time:
        queue.append(processes[i][0])
        i += 1

    while queue:

        pid = queue.popleft()

        start = time

        
        run_time = min(tq, remaining[pid])

        time += run_time
        remaining[pid] -= run_time

        gantt.append((pid, start, time))

        
        while i < n and processes[i][1] <= time:
            queue.append(processes[i][0])
            i += 1

        
        if remaining[pid] > 0:
            queue.append(pid)
        else:
            completion[pid] = time

    
    turnaround = {}
    waiting = {}

    for p in processes:
        pid = p[0]

        turnaround[pid] = completion[pid] - arrival[pid]
        waiting[pid] = turnaround[pid] - burst[pid]

    avg_tat = sum(turnaround.values()) / n
    avg_wt = sum(waiting.values()) / n

    return gantt, turnaround, waiting, avg_tat, avg_wt


gantt, turnaround, waiting, avg_tat, avg_wt = round_robin(
    processes,
    time_quantum
)


print("\nRound Robin Scheduling")
print("Time Quantum =", time_quantum, "ms")

print("\nGantt Chart:")

for pid, start, end in gantt:
    print(f"| {pid} {start}-{end} ", end="")

print("|")


print("\nTurnaround Time:")

for pid in turnaround:
    print(f"{pid} = {turnaround[pid]} ms")


print("\nWaiting Time:")

for pid in waiting:
    print(f"{pid} = {waiting[pid]} ms")


print("\nAverage Turnaround Time =", round(avg_tat, 2), "ms")
print("Average Waiting Time    =", round(avg_wt, 2), "ms")
