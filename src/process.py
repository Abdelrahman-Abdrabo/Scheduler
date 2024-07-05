class Process:
    def __init__(self, name, arrival, burst, deadline):
        self.name = name
        self.arrivalTime = arrival
        self.burstTime = burst
        self.burstTimeRemaining = burst
        self.waitingTime = 0
        self.responseTime = 0
        self.turnaroundTime = 0
        self.deadline = deadline
        self.startTime = None
        self.completionTime = 0
        self.status = "S"
        self.isComplete = False
        self.inQueue = False

    # allow comparison of processes based on their deadlines, necessary for the (priority queue).
    def __lt__(self, other):
        return self.deadline < other.deadline
