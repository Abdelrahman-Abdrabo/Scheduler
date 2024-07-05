
# Scheduler Simulator

Scheduler Simulator is a Python project that simulates the Round Robin and Earliest Deadline First (EDF) scheduling algorithms. It calculates various performance metrics for each algorithm and provides some statistics for each process.

## Features

- **Algorithms**:
  - **Round Robin (RR)**
  - **Earliest Deadline First (EDF)**
- **Metrics Calculated**:
  - Average Waiting Time (AWT)
  - Average Response Time (ART)
  - Average Turnaround Time (ATT)
  - Throughput
  - CPU Utilization
  - Proportionality
- **Process Statistics**:
  - Start Time
  - End Time
  - Duration
  - Status (Failed 'F' or Success 'S')

## Usage

1. Open a terminal in the folder containing the `scheduler.exe` file.
2. Run the following command:

```sh
.\scheduler.exe <path to list.csv> <quantum as number>
```

- `<path to list.csv>`: Path to the CSV file containing the list of processes and their arrival times, burst time, and deadline.
- `<quantum as number>`: Time quantum for the Round Robin algorithm.

>If you do not provide the required parameters (or you double click on it), the program will prompt you to enter the path to the list and the quantum.

## Example

Here is an example of how to run the scheduler:

```sh
.\scheduler.exe C:\path\to\list.csv 5
```

## Contributors

- **Abdulrahman Ahmed** (عبدالرحمن أحمد)
- **Abdulrahman Mohamed** (عبدالرحمن محمد)
- **Doha Ragab** (ضحى رجب)
- **Fatma Mostafa** (فاطمة مصطفى)
- **Fatma Mohamed** (فاطمة محمد)

