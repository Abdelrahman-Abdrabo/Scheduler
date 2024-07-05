from tabulate import tabulate


def check_for_new_arrivals(processes, n, current_time, ready_queue):
    for i in range(n):
        p = processes[i]
        if p.arrivalTime <= current_time[0] and not p.inQueue and not p.isComplete:
            processes[i].inQueue = True
            ready_queue.append(i)


def update_queue(processes, num_of_processes, quantum, ready_queue, current_time, programs_executed):
    i = ready_queue[0]
    ready_queue.pop(0)

    # calculate response time
    if processes[i].startTime is None:
        processes[i].startTime = current_time[0]

    if processes[i].burstTimeRemaining <= quantum:
        programs_executed[0] += 1
        processes[i].isComplete = True
        current_time[0] += processes[i].burstTimeRemaining
        processes[i].completionTime = current_time[0]
        processes[i].burstTimeRemaining = 0

        if programs_executed[0] != num_of_processes:
            check_for_new_arrivals(processes, num_of_processes, current_time, ready_queue)
    else:
        processes[i].burstTimeRemaining -= quantum
        current_time[0] += quantum

        if programs_executed[0] != num_of_processes:
            check_for_new_arrivals(processes, num_of_processes, current_time, ready_queue)

        ready_queue.append(i)


def output(processes, end_time, num_of_processes):
    avg_waiting_time = avg_turnaround_time = avg_response_time = proportionality = total_bt_time = 0

    table = []
    for process in processes:
        # for printing
        table.append([process.name, process.startTime, process.completionTime, process.burstTime, process.status])
        # calculate the parameters
        process.waitingTime = process.completionTime - process.arrivalTime - process.burstTime
        process.turnaroundTime = process.waitingTime + process.burstTime
        process.responseTime = process.startTime - process.arrivalTime

    print(tabulate(table, headers=["Process", "Start Time", "End Time", "Duration", "Status"],
                   tablefmt="rounded_grid", stralign="center", numalign="center"))

    for i in range(num_of_processes):
        total_bt_time += processes[i].burstTime
        avg_waiting_time += processes[i].waitingTime
        avg_turnaround_time += processes[i].turnaroundTime
        avg_response_time += processes[i].responseTime
        proportionality = max(proportionality, (processes[i].turnaroundTime / processes[i].burstTime))

    throughput = len(processes) / end_time[0]
    utilization = (total_bt_time / end_time[0]) * 100

    metrics = [
        ["Average Waiting Time", avg_waiting_time / num_of_processes],
        ["Average Turnaround Time", avg_turnaround_time / num_of_processes],
        ["Average Response Time", avg_response_time / num_of_processes],
        ["CPU Utilization Ratio (%)", utilization],
        ["Throughput", throughput],
        ["Proportionality", proportionality]
    ]

    print("Metrics:")
    print(tabulate(metrics, tablefmt="rounded_grid", numalign="center", floatfmt=".2f"))


def round_robin(processes, n, quantum):
    processes.sort(key=lambda p: p.arrivalTime)
    current_time = [0]
    programs_executed = [0]
    ready_queue = []
    check_for_new_arrivals(processes, n, current_time, ready_queue)

    while programs_executed[0] != n:
        while len(ready_queue) == 0:
            current_time[0] += 1
            check_for_new_arrivals(processes, n, current_time, ready_queue)

        while len(ready_queue) != 0:
            update_queue(processes, n, quantum, ready_queue, current_time, programs_executed)
    output(processes, current_time, n)
