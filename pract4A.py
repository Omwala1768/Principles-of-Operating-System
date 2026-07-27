print("Om Wala S119")
processes = ["P1", "P2", "P3", "P4"]
arrival = [0, 1, 2, 3]
burst = [5, 3, 8, 6]

n = len(processes)

completion = [0] * n
turnaround = [0] * n
waiting = [0] * n

current_time = 0

for i in range(n):
    if current_time < arrival[i]:
        current_time = arrival[i]

    current_time += burst[i]
    completion[i] = current_time
    turnaround[i] = completion[i] - arrival[i]
    waiting[i] = turnaround[i] - burst[i]

avg_waiting = sum(waiting) / n
avg_turnaround = sum(turnaround) / n

print("\nFCFS Scheduling\n")

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

print("\nGantt Chart:")
print("0", end="")

time = 0
for b in burst:
    time += b
    print("------", end="")

print()

for p in processes:
    print("| {:^3} ".format(p), end="")
print("|")

print("0", end="")
time = 0
for b in burst:
    time += b
    print("{:>6}".format(time), end="")
print()
