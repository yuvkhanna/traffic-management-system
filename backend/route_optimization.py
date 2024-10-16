import networkx as nx

# Predefined road network graph
road_network = nx.Graph()

# Sample graph creation
road_network.add_edge('A', 'B', weight=5)  # Congestion weight
road_network.add_edge('B', 'C', weight=2)
road_network.add_edge('A', 'C', weight=10)

def get_optimized_route(start, destination):
    return nx.dijkstra_path(road_network, start, destination, weight='weight')
