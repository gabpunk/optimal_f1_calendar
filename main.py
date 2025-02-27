import numpy as np
import pandas as pd
import networkx as nx
from geopy.distance import geodesic


df = pd.read_csv('calendario.csv')

def calculate_distance(point1, point2):
    return geodesic(point1, point2).km


num_circuits = len(df)
distance_matrix = np.zeros((num_circuits, num_circuits))

for i in range(num_circuits):
    for j in range(num_circuits):
        if i != j:
            point1 = (df.iloc[i]['Latitude'], df.iloc[i]['Longitude'])
            point2 = (df.iloc[j]['Latitude'], df.iloc[j]['Longitude'])
            distance_matrix[i][j] = calculate_distance(point1, point2)

G = nx.from_numpy_array(distance_matrix)

tsp_path = nx.approximation.traveling_salesman_problem(G, cycle=True)

total_distance = sum(distance_matrix[tsp_path[i]][tsp_path[i+1]] for i in range(len(tsp_path)-1))

print("Calendário mais eficiente:")
for i, idx in enumerate(tsp_path[:-1]):
    print(f"{i+1}. {df.iloc[idx]['GP Name']} ({df.iloc[idx]['Location']})")

print(f"\nDistância total: {total_distance:.2f} km")