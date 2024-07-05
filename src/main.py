import csv
import sys
import time
from process import Process
from round_robin import round_robin
from EDF import edf_scheduling

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("--> ERROR: you should provide an input file and quantum from terminal")
        print("The command is: > (python main.py <input file.csv path or name> quantum)")
        file = csv.reader(open(input("file path: "), 'r'))
        quantum = int(input("Quantum: "))
    else:
        file = csv.reader(open(sys.argv[1], 'r'))
        quantum = int(sys.argv[2])

    if quantum <= 0:
        print("--> ERROR: quantum must be greater than zero")
        time.sleep(30)
        exit(1)

    processes_EDF = []
    processes_RoundRobin = []
    number_of_processes = 0

    for line in file:
        number_of_processes += 1
        # Round_robin processes
        processes_RoundRobin.append(Process(line[0], int(line[1]), int(line[2]), int(line[3])))
        # EDF processes
        processes_EDF.append(Process(line[0], int(line[1]), int(line[2]), int(line[3])))

    print("____________________________________________________________")
    print("Round Robin Algorithm:")
    round_robin(processes_RoundRobin, number_of_processes, quantum)
    print("____________________________________________________________")
    print("\nEarliest Deadline First Algorithm (EDF):")
    edf_scheduling(processes_EDF)
    # to make the program not exit after complete
    if len(sys.argv) < 3:
        print("\nTo exit press ctrl+c")
        while True:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                print("Bye Bye")
                break
