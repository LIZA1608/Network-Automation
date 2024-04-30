import networkx as nx
import matplotlib.pyplot as plt
 
G = nx.watts_strogatz_graph(n = 10, k = 4, p = 0.5)
pos = nx.circular_layout(G)
 
plt.figure(figsize = (12, 12))
nx.draw_networkx(G, pos)
plt.title("Watts-Strogatz Graph")
plt.show()
