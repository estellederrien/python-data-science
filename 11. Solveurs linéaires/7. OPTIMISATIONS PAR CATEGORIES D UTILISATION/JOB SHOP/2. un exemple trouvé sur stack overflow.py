#https://stackoverflow.com/questions/70352814/is-there-a-way-to-ignore-some-machines-set-to-nothing-in-job-shop-scheduling-p

from pulp import *

# define model
schedule = LpProblem(name="Minimize_Schedule", sense=LpMinimize)

# define number of machines (m) and jobs (j)
machines = 3
jobs = 2

# for each job, the order the machines will go in
# for job 1, machine 1 is not needed
machine_sequence = [[0, 2],
                    [1, 2,    0 ]]

# for each job, the processing time of each
times = [[2, None, 3],
         [1, 4,    5]]

valid_starts = [(j, m) for j in range(jobs) for m in machine_sequence[j]]

# x[j, m] = start time for job j on machine m
x = LpVariable.dicts("start time", indexs=valid_starts, lowBound=0, cat='Continuous')

# machine sequence constraint 
# for each machine in the job sequence (except the 0th), the start time of the
# machine must be greater than the previous start + duration
for j in range(jobs):                  # for each job
    for m_idx in range(1, len(machine_sequence[j])):     # for each machine in job's seq, except 0
        # convenience for bookkeeping...  
        curr_machine = machine_sequence[j][m_idx]
        prior_machine = machine_sequence[j][m_idx - 1]

        # so,
        schedule += x[j, curr_machine] >= x[j, prior_machine] + times[j][prior_machine]

print(schedule)