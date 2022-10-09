# Source https://linuxtut.com/en/338f5a4883551b7c057f/

from ortools.sat.python import cp_model
from collections import defaultdict
from dataclasses import dataclass
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import random

num_machines = 3
num_lots = 5
num_jobs_per_lot = 3
num_jobs = num_lots * num_jobs_per_lot

@dataclass
class job_type:
    id: int
    lot_id: int
    size: int

random.seed(1)
jobs_list = [job_type(j, j//num_jobs_per_lot, random.randint(1, 10)) for j in range(num_jobs)]
horizon = sum([job.size for job in jobs_list])

model = cp_model.CpModel()
machine_to_intervals = defaultdict(list)
for job in jobs_list:
    start_var = model.NewIntVar(0, horizon, 'start_' + str(job.id))
    end_var = model.NewIntVar(0, horizon, 'end_' + str(job.id))
    job.start_var = start_var
    job.end_var = end_var
    bool_var_list = []
    for m in range(num_machines):
        suffix = str(m) + '_' + str(job.id)
        bool_var = model.NewBoolVar('bool_' + suffix)
        bool_var_list.append(bool_var)
        interval_var = model.NewOptionalIntervalVar(start_var, job.size, end_var, bool_var, 'interval_' + suffix)
        interval_var.job = job
        interval_var.bool_var = bool_var
        machine_to_intervals[m].append(interval_var)
    model.Add(sum(bool_var_list) == 1)

for m in machine_to_intervals:
    model.AddNoOverlap(machine_to_intervals[m])

for j in range(num_jobs-1):
    if jobs_list[j].lot_id != jobs_list[j+1].lot_id: continue

span_var = model.NewIntVar(0, horizon, 'span_var')
model.AddMaxEquality(span_var, [j.end_var for j in jobs_list])
model.Minimize(span_var)

solver = cp_model.CpSolver()
solver.Solve(model)
print(solver.StatusName(), solver.ObjectiveValue())


span_max = solver.Value(span_var)
cmap = plt.cm.get_cmap('hsv', num_lots+1)
fig = plt.figure(figsize=(12, 8))
for m in machine_to_intervals:
    ax = fig.add_subplot(num_machines, 1, m+1, yticks=[], ylabel=m)
    ax.set_xlim(-1, span_max+1)
    ax.set_ylim(-0.1, 1.1)
    for i in machine_to_intervals[m]:
        if solver.Value(i.bool_var) == 0: continue
        start = solver.Value(i.job.start_var)
        rectangle = matplotlib.patches.Rectangle((start, 0), i.job.size, 1, fill=False, color=cmap(i.job.lot_id), hatch='/')
        ax.add_patch(rectangle)
        rx, ry = rectangle.get_xy()
        cx = rx + rectangle.get_width()/2
        cy = ry + rectangle.get_height()/2
        lab = str(i.job.lot_id) + '-' + str(i.job.id)
        ax.annotate(lab, (cx, cy), ha='center', va='center')
plt.show()
