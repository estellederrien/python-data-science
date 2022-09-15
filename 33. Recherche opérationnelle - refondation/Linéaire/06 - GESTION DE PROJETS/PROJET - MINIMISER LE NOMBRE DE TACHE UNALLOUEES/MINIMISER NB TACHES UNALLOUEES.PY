# https://stackoverflow.com/questions/70571072/minimize-number-of-unallocated-tasks-in-pulp

from pulp import *
from random import choice, sample

### CREATING DATA

# Setting parameters

num_tasks = 10
num_volunteers = 7

# Creating list of 100 tasks numbered T1 to T100
tasks = [f"T{i}" for i in range(1,num_tasks + 1)]

# Each task is labelled with a number 1 - 3 that indicates estimated time taken to complete
task_load = dict(zip(tasks, [choice([1,2,3]) for i in range(num_tasks)]))

# Creating list of 50 volunteers numbered V1 to V50
volunteers = [f"V{i}" for i in range(1,num_volunteers+1)]

# Each volunteer is asked to choose 7 tasks to be assigned
volunteer_choices = dict(zip(volunteers, [list(sample(tasks, k=7)) for i in range(num_volunteers)]))

# Each volunteer can choose to take between 1 - 3 tasks
volunteer_max_tasks = dict(zip(volunteers, [choice([1, 2, 3]) for i in range(num_volunteers)]))

### DEFINING MODEL

# Define model
model = LpProblem(name = "resource-allocation", sense = LpMaximize)

# Define decision pair
pair = LpVariable.dicts("Pair", (volunteers, tasks), cat=LpBinary)  # no need for upper/lower bound for binary. :)
task_covered = LpVariable.dicts("Covered", tasks, cat=LpBinary)

# Set list of all possible pairs
pairs = [(v, t) for t in tasks for v in volunteers]

# Set objective
model += lpSum(task_covered[t] for t in tasks) + \
         0.05 * lpSum(pair[v][t] for v in volunteers for t in tasks)   # a little "sugar" to maximize assignments

# model += (lpSum([pair[v][t] for (v, t) in pairs]))  # not needed


### SETTING CONSTRAINTS

#  NEW:  Link the coverage of task to having at least one volunteer paired with it.
#        The model wants to "increase" the covered task variable, so we need to clamp it
#        down unless there is at least one pair assigned.  Make sense?
for t in tasks:
    model += task_covered[t] <= lpSum(pair[v][t] for v in volunteers)

# All volunteers must be assigned at least one task  <-- superfluous constraint.  Model is "trying" to do this
# for v in volunteers:
#     model += lpSum(pair[v][t] for t in tasks) >= 1

# Volunteers cannot be assigned to more tasks than they are willing to take on
for v in volunteers:
    model += lpSum(pair[v][t] for t in tasks) <= volunteer_max_tasks[v]

# Volunteers cannot be assigned too high a work load
for v in volunteers:
    model += lpSum(pair[v][t] * task_load[t] for t in tasks) <= 6
    
# Volunteers cannot be assigned a task they didn't choose
for v in volunteers:
    for t in tasks:
        if not (t in volunteer_choices[v]):
            model += pair[v][t] == 0
    
# All tasks must get a volunteer (CAN I LOOSEN THIS?)  # This is where your infeasibility problem was
# for t in tasks:
#     model += (lpSum([pair[v][t] for v in volunteers]) >= 1)

model.solve()

for v in sorted(volunteers):
    for task in sorted(pair[v]):
        if pair[v][task].varValue:
            print(f'pair: {v} to task {task}')