from queue import PriorityQueue
from tabulate import tabulate


def output(completed_processes, time):
    total_wt = total_tat = total_rt = total_bt = proportionality = 0

    data = []

    for process in completed_processes:
        process.waitingTime = process.completionTime - process.arrivalTime - process.burstTime
        process.turnaroundTime = process.completionTime - process.arrivalTime
        process.responseTime = process.startTime - process.arrivalTime

        total_wt += process.waitingTime
        total_tat += process.turnaroundTime
        total_rt += process.responseTime
        total_bt += process.burstTime

        if process.completionTime > process.deadline:
            process.status = "F"

        proportionality = max(proportionality, process.turnaroundTime / process.burstTime)

        data.append([process.name, process.startTime, process.completionTime, process.burstTime,
                     process.status])

    avg_wt = total_wt / len(completed_processes)
    avg_tat = total_tat / len(completed_processes)
    avg_rt = total_rt / len(completed_processes)
    throughput = len(completed_processes) / time
    utilization = total_bt / time

    headers = ["Process", "Start Time", "End Time", "Duration", "Status"]
    print(tabulate(data, headers, tablefmt="rounded_grid", stralign="center", numalign="center"))

    metrics = [
        ["Average Waiting Time", avg_wt],
        ["Average TAT Time", avg_tat],
        ["Average Response Time", avg_rt],
        ["Throughput", throughput],
        ["CPU Utilization (%)", utilization * 100],
        ["Proportionality", proportionality]
    ]

    print("Metrics:")
    print(tabulate(metrics, tablefmt="rounded_grid", numalign="center", floatfmt=".2f"))


def edf_scheduling(processes_list):
    processes_list.sort(key=lambda p: p.arrivalTime)
    time = 0
    ready_queue = PriorityQueue()
    completed_processes = []
    current_process = None

    while processes_list or not ready_queue.empty() or current_process:
        # check for new arrivals
        while processes_list and processes_list[0].arrivalTime <= time:
            ready_queue.put(processes_list.pop(0))

        # if there is a process or not
        if current_process:
            if not ready_queue.empty():
                top_process = ready_queue.queue[0]
                # Return the current process to the queue if its deadline is greater than the top process in the queue
                # if the same deadline don't do anything
                if top_process.deadline < current_process.deadline:
                    ready_queue.put(current_process)
                    current_process = ready_queue.get()

            if current_process.startTime is None:
                current_process.startTime = time

            current_process.burstTimeRemaining -= 1
            time += 1

            # If the current process is done, move it to completed processes
            if current_process.burstTimeRemaining == 0:
                current_process.completionTime = time
                completed_processes.append(current_process)
                current_process = None
        else:
            if not ready_queue.empty():
                current_process = ready_queue.get()
                if current_process.startTime is None:
                    current_process.startTime = time

            if not current_process:
                time += 1

    output(completed_processes, time)
