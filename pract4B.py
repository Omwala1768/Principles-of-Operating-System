print("Om Wala S119")
processes = ["P1", "P2", "P3", "P4"]
arrival = [0, 2, 4, 5]
burst = [7, 4, 1, 4]

n = len(processes)

completed = [False] * n
completion = [0] * n
turnaround = [0] * n
waiting = [0] * n
gantt = []

time = 0
done = 0

while done < n:
    idx = -1
    shortest = 999

    for i in range(n):
        if arrival[i] <= time and not completed[i]:
            if burst[i] < shortest:
                shortest = burst[i]
                idx = i

    if idx == -1:
        time += 1
        continue

    time += burst[idx]
    completion[idx] = time
    turnaround[idx] = completion[idx] - arrival[idx]
    waiting[idx] = turnaround[idx] - burst[idx]

    completed[idx] = True
    done += 1
    gantt.append((processes[idx], completion[idx]))

avg_waiting = sum(waiting) / n
avg_turnaround = sum(turnaround) / n

print("\nNon-Preemptive SJF Scheduling\n")

print("{:<8}{:<10}{:<10}{:<12}{:<12}{:<10}".format(
    "Process", "Arrival", "Burst", "Completion", "Turnaround", "Waiting"))

for i in range(n):
    print("{:<8}{:<10}{:<10}{:<12}{:<12}{:<10}".format(
        processes[i],
        arrival[i],
        burst[i],
        completion[i],
        turnaround[i],
        waiting[i]
    ))

print("\nAverage Waiting Time =", round(avg_waiting, 2), "ms")
print("Average Turnaround Time =", round(avg_turnaround, 2), "ms")

# Gantt Chart
print("\nGantt Chart:")

start = 0
print(start, end="")

for p, end_time in gantt:
    print("------", end="")
print()

for p, end_time in gantt:
    print("| {:^3} ".format(p), end="")
print("|")

print(0, end="")
for p, end_time in gantt:
    print("{:>6}".format(end_time), end="")
print()
