import pulp as pl
import pytups as pt

# Get input data
duration = {1: 8, 2: 12, 3: 6, 4: 13, 5: 2, 6: 12, 7: 15, 8: 20, 9: 16, 10: 16, 11: 10, 12: 14, 13: 17, 14: 3, 15: 20, 16: 19, 17: 13, 18: 6, 19: 18, 20: 11}
priority = {1: 4, 2: 5, 3: 6, 4: 8, 5: 4, 6: 2, 7: 5, 8: 6, 9: 1, 10: 8, 11: 8, 12: 4, 13: 4, 14: 8, 15: 9, 16: 11, 17: 6, 18: 10, 19: 6, 20: 9}
duedate = {1: 52, 2: 80, 3: 133, 4: 150, 5: 53, 6: 133, 7: 113, 8: 107, 9: 75, 10: 133, 11: 77, 12: 126, 13: 117, 14: 72, 15: 111, 16: 111, 17: 117, 18: 69, 19: 115, 20: 68}



# Get intermediate paramters, sets.
C_max = sum(duration.values())
periods = range(C_max)
tasks = duration.keys()

# all legal combinations of task-period assignment
jk_all = pt.TupList((t, p) for t in tasks for p in periods)

# we filter the starts that are too late to be possible:
JK = jk_all.filter_list_f(lambda x: x[1] + duration[x[0]] <= C_max)

# we create a set of tasks that can start at time period k
K_j = JK.to_dict(result_col=1)

# all combinations (t, p, p2) such that I start a task j 
# in time period k and is active in period k2
jkk2 = pt.TupList((j, k, k2) for j, k in JK 
				  for k2 in range(k, k + duration[j]))

# given a period k2, what starts affect make it unavailable:
JK_k2 = jkk2.to_dict(result_col=[0, 1])

# given a start (j, k), what periods k2 are made unavailable:
K2_jk = jkk2.to_dict(result_col=2)

# for each possible start: how late will the task be
t_jk = {(j, k): max(duration[j] + k -1 - duedate[j], 0) * 
				priority[j] for j, k in JK}



# model construction with PuLP
model = pl.LpProblem("Scheduling", pl.LpMinimize)
X = pl.LpVariable.dicts(name='start', indexs=JK,
                            lowBound=0, upBound=1, cat=pl.LpInteger)

# objective function:
model += pl.lpSum(X[j, k] * t_jk[j, k] for j, k in JK)

# one and only one start per task
for j in tasks:
    model += pl.lpSum(X[j, k] for k in K_j[j]) == 1

# only one task is active at any moment:
for k2 in periods:
    model += pl.lpSum(X[j, k] for j, k in JK_k2[k2]) == 1

# solve model:
solver = pl.PULP_CBC_CMD(msg=True)
# solver = pl.CPLEX_CMD(msg=True)
model.solve(solver)



# get tasks starts
starts_out = pt.SuperDict(X).vapply(pl.value).clean().keys_l()

solution = [-1 for p in periods]
for j, k in starts_out:
    for p2 in K2_jk[j, k]:
        solution[p2] = j

print('solution is \n{}'.format(solution))



# verify that all periods are filled:
# counting if there is any with a minus -1
pt.TupList(solution).filter_list_f(lambda v: v == -1)

# verify that each task t appears exactly duration[t] times
task_count = pt.SuperDict().fill_with_default(keys=duration.keys())
for period, task in enumerate(solution):
    task_count[task] += 1
task_count.apply(lambda k, v: duration[k] - v).clean()

