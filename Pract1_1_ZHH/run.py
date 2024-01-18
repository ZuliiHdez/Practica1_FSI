# Search methods

import search

print("Bienvenido al programa de búsqueda en el mapa de Rumania.")

start_city = input("Ingrese la ciudad de inicio: ").upper()
goal_city = input("Ingrese la ciudad de destino: ").upper()


problem = search.GPSProblem(start_city, goal_city, search.romania)

print("\n-----------------------------------------------------\nAmplitud:")
search.breadth_first_graph_search(problem)

print("\n-----------------------------------------------------\nProfundidad:")
search.depth_first_graph_search(problem)

print("\n-----------------------------------------------------\nRamificación y acotación:")
search.branch_and_bound(problem)

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
