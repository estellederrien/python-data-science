#https://towardsdatascience.com/how-i-saved-christmas-with-the-travelling-salesman-problem-3d85c190ed9d

#   Import Pandas - List of cities can be found here https://simplemaps.com/data/world-cities
import pandas as pd
#   Import PuLP modeler functions
from pulp import *
#   Math functions for distance calculation
import math
#   Networkx to get connected components and subtours
import networkx as nx
#   Matplotlib for debugging
import matplotlib.pyplot as plt
#   Visually see loops progression
from tqdm import tqdm
#   To measure the optimizataion time
import time


class TSP():
    cities = None
    santa = None
    variables_dict = None
    x = None
    path = None
    sec_constraints = 0
    execution_time = 0

    def __init__(self, population_lower_bound=10e5 * 3):
        cities = pd.read_csv("worldcities.csv")
        self.cities = cities.loc[cities["population"] >= population_lower_bound][
            ["lat", "city", "lng", "population"]].reset_index()

        #   Add Santa's house
        santa_df = pd.DataFrame([["Santa's House", 66.550331132, 25.886996452, 10000]],
                                columns=["city", "lat", "lng", "population"])

        #   Add other cities with smaller population to improve the World coverage
        reykjavik = cities.loc[(cities["city_ascii"] == "Reykjavik") & (cities["country"] == "Iceland")]
        algiers = cities.loc[(cities["city_ascii"] == "Algiers") & (cities["country"] == "Algeria")]
        brazzaville = cities.loc[(cities["city_ascii"] == "Brazzaville")]
        dublin = cities.loc[(cities["city"] == "Dublin") & (cities["country"] == "Ireland")]
        guatemala_city = cities.loc[(cities["city_ascii"] == "Guatemala City")]
        ulaanbaatar = cities.loc[(cities["city_ascii"] == "Ulaanbaatar")]
        wellington = cities.loc[(cities["city"] == "Wellington") & (cities["country"] == "New Zealand")]
        port_moresby = cities.loc[(cities["city_ascii"] == "Port Moresby")]
        juneau = cities.loc[(cities["city_ascii"] == "Juneau")]
        edmonton = cities.loc[(cities["city_ascii"] == "Edmonton")]
        juba = cities.loc[(cities["city_ascii"] == "Juba")]
        stockholm = cities.loc[(cities["city_ascii"] == "Stockholm")]
        copenhagen = cities.loc[(cities["city_ascii"] == "Copenhagen")]
        oslo = cities.loc[(cities["city_ascii"] == "Oslo")]
        abeche = cities.loc[(cities["city_ascii"] == "Abeche")]
        kuala_lumpur = cities.loc[(cities["city_ascii"] == "Kuala Lumpur")]
        kuching = cities.loc[(cities["city_ascii"] == "Kuching")]
        tirana = cities.loc[(cities["city_ascii"] == "Tirana")]
        volgograd = cities.loc[(cities["city_ascii"] == "Volgograd")]
        belgrade = cities.loc[(cities["city_ascii"] == "Belgrade") & (cities["country"] == "Serbia")]
        fairbanks = cities.loc[(cities["city_ascii"] == "Fairbanks")]
        vilnius = cities.loc[(cities["city_ascii"] == "Vilnius")]
        tartu = cities.loc[(cities["city_ascii"] == "Tartu")]
        riga = cities.loc[(cities["city_ascii"] == "Riga") & (cities["country"] == "Latvia")]
        nur_sultan = cities.loc[(cities["city_ascii"] == "Nur-Sultan")]
        bamako = cities.loc[(cities["city_ascii"] == "Bamako")]
        ouagadougou = cities.loc[(cities["city_ascii"] == "Ouagadougou")]
        nouakchott = cities.loc[(cities["city_ascii"] == "Nouakchott")]
        n_djamena = cities.loc[(cities["city_ascii"] == "N'Djamena")]
        bangui = cities.loc[(cities["city_ascii"] == "Bangui")]
        niamey = cities.loc[(cities["city_ascii"] == "Niamey")]
        ljubljana = cities.loc[(cities["city_ascii"] == "Ljubljana")]
        sofia = cities.loc[(cities["city_ascii"] == "Sofia")]
        zagreb = cities.loc[(cities["city_ascii"] == "Zagreb")]

        self.cities = pd.concat(
            [self.cities, santa_df, dublin, reykjavik, algiers,
             brazzaville, guatemala_city, ulaanbaatar, wellington,
             port_moresby, juneau, edmonton, juba,
             stockholm, copenhagen, oslo, abeche, kuala_lumpur,
             kuching, tirana, volgograd, belgrade, fairbanks, vilnius,
             tartu, riga, nur_sultan, bamako, ouagadougou, nouakchott,
             n_djamena, bangui, niamey, ljubljana, sofia, zagreb]).reset_index()

        self.cities = pd.concat(
            [self.cities, santa_df]).reset_index()

        return

    def build_model(self):
        #   Initialize the problem
        santa = LpProblem("santa", LpMinimize)

        #   Generate distances
        w = h = self.cities.shape[0]
        distances = [[0 for x in range(w)] for y in range(h)]
        for index_a, row_a in tqdm(self.cities.iterrows(), total=self.cities.shape[0]):
            lat_a = row_a["lat"]
            lng_a = row_a["lng"]
            for index_b, row_b in self.cities.iterrows():
                lat_b = row_b["lat"]
                lng_b = row_b["lng"]
                distances[index_a][index_b] = self.calculate_distance(lat_a, lng_a, lat_b, lng_b)

        #   Generate dictionary to create the Linear program decision variables
        distances_dict = dict(((a, b), distances[a][b]) for a in self.cities.index for b in self.cities.index if a != b)
        #   The objective function
        x = LpVariable.dicts('x', distances_dict, 0, 1, LpBinary)
        self.x = x
        self.variables_dict = dict([(str(value), key) for key, value in x.items()])
        cost = lpSum([x[(i, j)] * distances_dict[(i, j)] for (i, j) in distances_dict])

        #   Add cost function to the model
        santa += cost

        #   Add other constraints, after this we will only need to add the subtour elimination constraints!
        for k in self.cities.index:
            # every site has exactly one inbound connection
            santa += lpSum([x[(i, k)] for i in self.cities.index if (i, k) in x]) == 1
            # every site has exactly one outbound connection
            santa += lpSum([x[(k, i)] for i in self.cities.index if (k, i) in x]) == 1

        self.distances_dict = distances_dict
        self.santa = santa

    def add_subtour_constraints(self):
        #   Generate the graph from the current solution
        varsdict = {}
        for v in self.santa.variables():
            if v.varValue == 1:
                varsdict[v.name] = v.varValue

        G = nx.Graph()
        #   Add nodes to the Graph
        for index_a, row_a in self.cities.iterrows():
            lat_a = row_a["lat"]
            lng_a = row_a["lng"]
            G.add_node(index_a, pos=(lat_a, lng_a))

        #   Add edges according to solution
        for k in varsdict:
            tmp_node = self.variables_dict[k]
            G.add_edge(tmp_node[0], tmp_node[1])

        #   If the number of connected components is 1, we found the optimal path
        nr_connected_components = nx.number_connected_components(G)
        if nr_connected_components == 1:
            return True
        #   Otherwise we need to add the SEC equations

        #   Get all the connected components. If there are more than 1, then there are subtours
        components = nx.connected_components(G)
        for c in tqdm(components, total=nr_connected_components):
            self.santa += lpSum([self.x[(a, b)] for a in c for b in c if a != b]) <= len(c) - 1
            self.sec_constraints += 1

        print("ok")

    def build_graph_from_current_solution(self):
        varsdict = {}
        for v in self.santa.variables():
            if v.varValue == 1:
                varsdict[v.name] = v.varValue

        G = nx.Graph()
        #   Add nodes to the Graph
        for index_a, row_a in self.cities.iterrows():
            lat_a = row_a["lat"]
            lng_a = row_a["lng"]
            G.add_node(index_a, pos=(lat_a, lng_a))

        #   Add edges according to solution
        for k in varsdict:
            tmp_node = self.variables_dict[k]
            G.add_edge(tmp_node[0], tmp_node[1])

        return G

    def solve(self):
        #   Now, the model is missing of the subtour elimination constraints.
        #   The number of these constraints is 2^N-2 where N is the number of cities selected. Too many.
        #   What we can do is:
        #       1. Solve the problem without the Subtour elimination constraints
        #       2. Get the solution and see if there are subtours of length lower than N
        #       3. Add the constraints that exclude those subtours
        #       4. Goto 1 and repeat until there are no more subtours
        start_time = time.time()
        while True:
            self.santa.solve(solvers.PULP_CBC_CMD(msg=True))

            G = self.build_graph_from_current_solution()
            pos = nx.get_node_attributes(G, 'pos')
            nx.draw(G, pos, node_size=200)
            plt.show()
            if self.add_subtour_constraints():
                break
        self.execution_time = time.time() - start_time

    def extract_solution(self):
        G = self.build_graph_from_current_solution()

        santas_idx = self.cities[self.cities["city"] == "Santa's House"].index

        cycle = nx.find_cycle(G, santas_idx)
        solution = []
        for e in G.edges:
            edge = []
            edge.append(e[0])
            edge.append(self.cities.iloc[e[0]]["city"])
            edge.append(self.cities.iloc[e[0]]["lat"])
            edge.append(self.cities.iloc[e[0]]["lng"])
            edge.append(self.cities.iloc[e[0]]["population"])

            edge.append(e[1])
            edge.append(self.cities.iloc[e[1]]["city"])
            edge.append(self.cities.iloc[e[1]]["lat"])
            edge.append(self.cities.iloc[e[1]]["lng"])
            edge.append(self.cities.iloc[e[1]]["population"])

            edge.append(self.distances_dict[(e[0], e[1])])

        path = []
        for s, e in cycle:
            path.append(s)

            solution.append(edge)
        columns = ["node_a_id", "node_a_city", "node_a_lat", "node_a_lng", "node_a_population", "node_b_id",
                   "node_b_city", "node_b_lat", "node_b_lng", "node_b_population", "distance_km"]

        path.append(path[0])
        self.path = path
        self.solution = pd.DataFrame(solution, columns=columns)

    def calculate_distance(self, lat_a, lng_a, lat_b, lng_b):
        #   Convert lat lng in radians
        lng_a, lat_a, lng_b, lat_b = map(math.radians, [lng_a, lat_a, lng_b, lat_b])

        d_lat = lat_b - lat_a
        d_lng = lng_a - lng_b

        temp = (
                math.sin(d_lat / 2) ** 2
                + math.cos(lat_a)
                * math.cos(lat_b)
                * math.sin(d_lng / 2) ** 2
        )

        return 6373.0 * (2 * math.atan2(math.sqrt(temp), math.sqrt(1 - temp)))


tsp = TSP(10e5 * 1.5)
tsp.build_model()
tsp.solve()
tsp.extract_solution()

print(tsp.solution)
print("SEC constraints added: {}".format(tsp.sec_constraints))
print("Solution Found in {} seconds".format(tsp.execution_time))
tsp.cities.to_json("selected_cities.json", orient="index")
print(tsp.path)