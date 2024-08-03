#Dynamic programming,Greedy approach used
# TC-O(nlog(n))
# Taking input from the user
n = int(input("Enter the number of jobs: "))
jobs = []
# Input each job's start time, end time, and profit
for i in range(n):
    start = int(input(f"Enter the start time of job {i+1}: "))
    end = int(input(f"Enter the end time of job {i+1}: "))
    profit = int(input(f"Enter the profit of job {i+1}: "))
    jobs.append((start, end, profit))
# Sort jobs based on their end times
jobs = sorted(jobs, key=lambda x: x[1])
print("Sorted jobs based on end times:", jobs)
# Initialize the arrays for storing profit sums and tracking jobs
x = len(jobs)
p = [0] * x
t = [0] * x
select = []

# Calculate the p[] array, which stores the index of the last non-conflicting job
for i in range(len(jobs)-1, 0, -1):  
    for j in range(i-1, -1, -1):
        if jobs[i][0] >= jobs[j][1]:
            p[i] = j + 1
            break

# Function to calculate the maximum profit and determine the jobs to select
def weighted(x):        
    if x == 0:
        return 0
    elif t[x-1]:
        return t[x-1]
    else:
        t[x-1] = max(weighted(x-1), jobs[x-1][2] + weighted(p[x-1]))
        return t[x-1]

# Function to retrieve the selected jobs
def nodes(k):                  
    if k < 1:
        return
    i = k
    while i > 1 and t[i-1] == t[i-2]:
        i -= 1
    select.append((jobs[i-1][0], jobs[i-1][1]))
    nodes(p[i-1])

# Compute the maximum profit
print("Maximum Profit:", weighted(x))

# Retrieve the selected jobs
nodes(x)
print("Selected jobs: ", select)
