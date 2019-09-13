import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node('A', data={"name": "node A"})
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_node('E')
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('A', 'D')
G.add_edge('D', 'E')

print(G.node['A']['data'])
print(G.edges)
print(nx.average_clustering(G))
print(nx.shortest_path(G, 'A', 'E'))
print(list(nx.neighbors(G,'A')))
# nx.draw_networkx(G)
# plt.show()