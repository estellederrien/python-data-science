# Author : https://github.com/Zzzly0322

from gurobipy import *
import data_read_RCPSP
# file="./data/j30.sm/j304_7.sm"
def Gurobi_RSPSP_J30(file):
    # Get the initial data from the file as follow
    # number_job
    # job_num_successors
    # job_successors
    # job_predecessors
    # job_duration
    # job_resource
    # resource_capacity
    number_job,job_num_successors, job_successors,job_predecessors,job_duration,job_resource,resource_capacity=data_read_RCPSP.dataRead(file)

    # Set the upper bound Completion Time of the project
    # we set T=100 when you solve the J30 problem
    T=100

    # Initial the gurobi model
    m = Model()
    #add variables xjt note that j activity start at time t
    x = m.addVars(number_job,T,vtype=GRB.BINARY, name='e')

    # Set the obj which means the minmize the Completion Time
    obj=0
    for t in range(T):
        obj+=x[number_job-1,t]*t
    # t_dict={(i,j):j
    #    for i in range(number_job) for j in range(T)
    # }
    m.setObjective(obj,GRB.MINIMIZE)

    # Constraint only can be done once
    m.addConstrs(x.sum(i,'*') == 1 for i in range(number_job))

    # Timing constraint
    for i in range(number_job):
        if len(job_predecessors[i]) !=0:
            for j in job_predecessors[i]:
                sum_ti=0
                sum_tj=0
                for t0 in range(T):
                    sum_ti+=x[i,t0]*t0
                for t1 in range(T):
                    sum_tj+=x[j-1,t1]*(t1+job_duration[j-1])
                m.addConstr(sum_ti>=sum_tj)
    # Resource constraint
    number_resource=4
    for k in range(number_resource):
        for t3 in range(50):
            use_resource=0
            for j in range(number_job):

                use_resource+=sum(x[j,tt] for tt in range(t3,t3+job_duration[j]))*job_resource[j][k]
            m.addConstr(resource_capacity[k]-use_resource>=0)

    m.write('lnear_model.lp')
    m.optimize()


    # Get the solution
    output_dict={}
    for v in m.getVars():
        if v.x!=0:
            print('%s %g' % (v.varName, v.x))
            a=eval(v.varName[1:])
            output_dict[a[0]]=a[1]


    start=list(output_dict.values())
    finish=[]
    count=0
    for start1 in output_dict.values():
        finish.append(start1+job_duration[count])
        count+=1

    # print('Obj: %g' % m.objVal)
    print('start',start)
    print("finish",finish)
    return start,finish