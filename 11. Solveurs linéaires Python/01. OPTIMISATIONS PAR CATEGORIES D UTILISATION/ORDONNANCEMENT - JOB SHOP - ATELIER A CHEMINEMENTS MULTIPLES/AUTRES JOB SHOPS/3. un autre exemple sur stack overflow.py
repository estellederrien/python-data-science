# https://stackoverflow.com/questions/70352814/is-there-a-way-to-ignore-some-machines-set-to-nothing-in-job-shop-scheduling-p

from pulp import *

# define number of machines (m) and jobs (j)
machines = 3
jobs = 2

# for each job, the order the machines will go in
# for job 1, machine 1 is not needed
machine_sequence = [[0, None, 2],
                    [1, 2, 0 ]]

valid_starts = [(j, m) for j in range(jobs) for m in range(machines)  if machine_sequence[j][m] != None]

model = LpProblem("Example", LpMinimize)

# Improved Variable...?  using LpVariable.dicts
s = LpVariable.dicts("start time", indexs=valid_starts, lowBound=0, cat='Continuous')

# starting time x, on job j (from all jobs n) on machine i (from all machines m)
x = [[LpVariable(name='x({} ,{} )'.format(j+1, i+1), lowBound=0) for i in range(machines)] for j in range(jobs)]

print(type(s), s)
print(type(x), x)

# random constraint for j-m pairs that are valid
for j, m in valid_starts:
    model += s[j, m] <= 10
