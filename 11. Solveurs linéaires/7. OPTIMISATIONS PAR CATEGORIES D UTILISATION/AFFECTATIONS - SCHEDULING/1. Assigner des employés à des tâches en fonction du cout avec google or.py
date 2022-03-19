# Source : https://developers.google.com/optimization/assignment/overview

""" L'un des problèmes d'optimisation combinatoire les plus connus est le problème d'affectation . 

Voici un exemple : supposons qu'un groupe de travailleurs doit effectuer un ensemble de tâches, 

et pour chaque travailleur et tâche, il y a un coût pour l'affectation du travailleur à la tâche. 

Le problème est d'affecter à chaque travailleur au plus une tâche, sans que deux travailleurs 

effectuent la même tâche, tout en minimisant le coût total.

Vous pouvez visualiser ce problème par le graphique ci-dessous, dans lequel il y a quatre travailleurs 

et quatre tâches. Les arêtes représentent toutes les manières possibles d'affecter des travailleurs aux tâches. 

Les étiquettes sur les bords indiquent les coûts d'affectation des travailleurs aux tâches. """


""" Une affectation correspond à un sous-ensemble d'arêtes, 
dans lequel chaque travailleur a au plus une arête menant vers la sortie, 
et deux travailleurs n'ont pas d'arête menant à la même tâche. 
Une affectation possible est illustrée ci-dessous.

Workers

Le coût total de la mission est de 70 + 55 + 95 + 45 = 265.

La section suivante montre comment résoudre un problème d'affectation, en utilisant à la fois le solveur MIP
et le solveur CP-SAT.

Autres outils pour résoudre les problèmes d'affectation
OR-Tools fournit également quelques autres outils pour résoudre les problèmes d'affectation, qui peuvent
 être plus rapides que les solveurs MIP ou CP :

Solveur d'affectation linéaire
Solveur de flux à coût minimum
Cependant, ces outils ne peuvent résoudre que des types simples de problèmes d'affectation. Ainsi, 
pour les solveurs généraux capables de gérer une grande variété de problèmes 
(et suffisamment rapides pour la plupart des applications), nous recommandons les solveurs MIP et CP-SAT. """



# Avec le solveur MIP  :

from ortools.linear_solver import pywraplp


def main():
    # Data
    costs = [
        [90, 80, 75, 70],
        [35, 85, 55, 65],
        [125, 95, 90, 95],
        [45, 110, 95, 115],
        [50, 100, 90, 100],
    ]
    num_workers = len(costs)
    num_tasks = len(costs[0])

    # Solver
    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')


    # Variables
    # x[i, j] is an array of 0-1 variables, which will be 1
    # if worker i is assigned to task j.
    x = {}
    for i in range(num_workers):
        for j in range(num_tasks):
            x[i, j] = solver.IntVar(0, 1, '')

    # Constraints
    # Each worker is assigned to at most 1 task.
    for i in range(num_workers):
        solver.Add(solver.Sum([x[i, j] for j in range(num_tasks)]) <= 1)

    # Each task is assigned to exactly one worker.
    for j in range(num_tasks):
        solver.Add(solver.Sum([x[i, j] for i in range(num_workers)]) == 1)

    # Objective
    objective_terms = []
    for i in range(num_workers):
        for j in range(num_tasks):
            objective_terms.append(costs[i][j] * x[i, j])
    solver.Minimize(solver.Sum(objective_terms))

    # Solve
    status = solver.Solve()

    # Print solution.
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        print('Total cost = ', solver.Objective().Value(), '\n')
        for i in range(num_workers):
            for j in range(num_tasks):
                # Test if x[i,j] is 1 (with tolerance for floating point arithmetic).
                if x[i, j].solution_value() > 0.5:
                    print('Worker %d assigned to task %d.  Cost = %d' %
                          (i, j, costs[i][j]))


if __name__ == '__main__':
    main()