# """From Bradley, Hax, and Magnanti, 'Applied Mathematical Programming', figure 8.1."""
# https://developers.google.com/optimization/flow/mincostflow

""" Le problème du flux de coût minimum

Le problème de flux de coût minimum (coût min) est étroitement lié au problème de flux maximal, 

dans lequel chaque arc du graphique a un coût unitaire pour le transport de matière à travers celui-ci. 

Le problème est de trouver un flux avec le moindre coût total.

Le problème de flux de coût min a également des nœuds spéciaux, appelés nœuds d'approvisionnement ou nœuds de demande,

 qui sont similaires à la source et au puits du problème de flux max.
 
  Le matériel est transporté des nœuds d'approvisionnement aux nœuds de demande.

    À un nœud d'approvisionnement, un montant positif - l'approvisionnement - est ajouté au flux. 
    
    Une offre pourrait représenter la production à ce nœud, par exemple.
    
    Au niveau d'un nœud de demande, un montant négatif (la demande) est retiré du flux. 
    
    Une demande pourrait représenter la consommation à ce nœud, par exemple.

Pour plus de commodité, nous supposerons que tous les nœuds, autres que les nœuds d'offre ou de demande, 

ont une offre (et une demande) nulle.

Pour le problème de flux de coût minimum, nous avons la règle de conservation de flux suivante, 

qui prend en compte les approvisionnements et les demandes :

À chaque nœud, le flux total sortant du nœud moins le flux total menant au nœud 

est égal à l'offre (ou la demande) à ce nœud.

Le problème du débit max est de trouver un débit pour lequel la somme des montants de débit pour l'ensemble du réseau est aussi grande que possible.

Les sections suivantes présentent les programmes Python et C# pour trouver le flux maximum de la source (0) au récepteur (4).

 """

from __future__ import print_function
from ortools.graph import pywrapgraph

def main():
  """MinCostFlow simple interface example."""

  # Define four parallel arrays: start_nodes, end_nodes, capacities, and unit costs
  # between each pair. For instance, the arc from node 0 to node 1 has a
  # capacity of 15 and a unit cost of 4.

  start_nodes = [ 0, 0,  1, 1,  1,  2, 2,  3, 4]
  end_nodes   = [ 1, 2,  2, 3,  4,  3, 4,  4, 2]
  capacities  = [15, 8, 20, 4, 10, 15, 4, 20, 5]
  unit_costs  = [ 4, 4,  2, 2,  6,  1, 3,  2, 3]

  # Define an array of supplies at each node.

  supplies = [20, 0, 0, -5, -15]


  # Instantiate a SimpleMinCostFlow solver.
  min_cost_flow = pywrapgraph.SimpleMinCostFlow()

  # Add each arc.
  for i in range(0, len(start_nodes)):
    min_cost_flow.AddArcWithCapacityAndUnitCost(start_nodes[i], end_nodes[i],
                                                capacities[i], unit_costs[i])

  # Add node supplies.

  for i in range(0, len(supplies)):
    min_cost_flow.SetNodeSupply(i, supplies[i])


  # Find the minimum cost flow between node 0 and node 4.
  if min_cost_flow.Solve() == min_cost_flow.OPTIMAL:
    print('Minimum cost:', min_cost_flow.OptimalCost())
    print('')
    print('  Arc    Flow / Capacity  Cost')
    for i in range(min_cost_flow.NumArcs()):
      cost = min_cost_flow.Flow(i) * min_cost_flow.UnitCost(i)
      print('%1s -> %1s   %3s  / %3s       %3s' % (
          min_cost_flow.Tail(i),
          min_cost_flow.Head(i),
          min_cost_flow.Flow(i),
          min_cost_flow.Capacity(i),
          cost))
  else:
    print('There was an issue with the min cost flow input.')

if __name__ == '__main__':
  main()