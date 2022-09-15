# https://github.com/timnon/pyschedule
# https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_gestion_de_projet_%C3%A0_contraintes_de_ressources
# Uniquement compatible avec python < 3.6 avant mais il a récemment commité le changement


''' remplacer dans le fichier pulp_scip car c'est plus à jour: 
import os
from time import perf_counter
import re
import subprocess
import pulp
import pulp.apis

class SCIP_CMD(pulp.apis.LpSolver_CMD):
    def __init__(self, path = None, keepFiles = 0, mip = 1,
            msg = 0, options = [], time_limit = None, ratio_gap = None):
        pulp.apis.LpSolver_CMD.__init__(self, path, keepFiles, mip, msg, options)
        self.time_limit = time_limit
        self.ratio_gap = ratio_gap
 '''

from pyschedule import Scenario, solvers, plotters, alt

# the planning horizon has 10 periods
S = Scenario('household',horizon=10)

# two resources: Alice and Bob
Alice, Bob = S.Resource('Alice'), S.Resource('Bob')

# three tasks: cook, wash, and clean
cook = S.Task('cook',length=1,delay_cost=1)
wash = S.Task('wash',length=2,delay_cost=1)
clean = S.Task('clean',length=3,delay_cost=2)

# every task can be done either by Alice or Bob
cook += Alice | Bob
wash += Alice | Bob
clean += Alice | Bob

# compute and print a schedule
solvers.mip.solve(S,msg=1)
print(S.solution())

