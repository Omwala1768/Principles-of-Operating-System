from collections import deque

print("Om Wala S119")

processes = [
    ["P1", 0, 5],
    ["P2", 4, 2],
    ["P3", 5, 4]
]

time_quantum = 2

def round_robin(processes, tq):

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
    n = len(processes)

    processes = sorted(processes, key=lambda x: x[1])

    
    while i < n and processes[i][1] <= time:
        queue.append(processes[i][0])
        i += 1

    while queue:

        pid = queue.popleft()

        start = time
        run_time = min(tq, remaining[pid])
        time += run_time

        gantt.append((pid, start, time))

        remaining[pid] -= run_time

        
        while i < n and processes[i][1] <= time:
            queue.append(processes[i][0])
            i += 1

        if remaining[pid] > 0:
            queue.append(pid)
        else:
            completion[pid] = time

    turnaround = {}
    waiting = {}

    for pid in arrival:
        turnaround[pid] = completion[pid] - arrival[pid]
        waiting[pid] = turnaround[pid] - burst[pid]

    avg_tat = sum(turnaround.values()) / n
    avg_wt = sum(waiting.values()) / n

    return gantt, turnaround, waiting, avg_tat, avg_wt



def fcfs(processes):

    processes = sorted(processes, key=lambda x: x[1])

    time = 0
    gantt = []
    turnaround = {}
    waiting = {}

    for p in processes:

        pid = p[0]
        arrival = p[1]
        burst = p[2]

        if time < arrival:
            time = arrival

        start = time
        time += burst

        gantt.append((pid, start, time))

        turnaround[pid] = time - arrival
        waiting[pid] = turnaround[pid] - burst

    n = len(processes)

    avg_tat = sum(turnaround.values()) / n
    avg_wt = sum(waiting.values()) / n

    return gantt, turnaround, waiting, avg_tat, avg_wt



def display(title, gantt, turnaround, waiting, avg_tat, avg_wt):

    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

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

    print(f"\nAverage Turnaround Time = {avg_tat:.2f} ms")
    print(f"Average Waiting Time = {avg_wt:.2f} ms")


rr_gantt, rr_tat, rr_wt, rr_avg_tat, rr_avg_wt = round_robin(
    processes, time_quantum
)

display(
    "ROUND ROBIN (Time Quantum = 2 ms)",
    rr_gantt,
    rr_tat,
    rr_wt,
    rr_avg_tat,
    rr_avg_wt
)

fcfs_gantt, fcfs_tat, fcfs_wt, fcfs_avg_tat, fcfs_avg_wt = fcfs(
    processes
)

display(
    "FCFS SCHEDULING",
    fcfs_gantt,
    fcfs_tat,
    fcfs_wt,
    fcfs_avg_tat,
    fcfs_avg_wt
)
