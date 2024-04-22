
import networkx as nx

import matplotlib.pyplot  as plt

G=nx.Graph()

G.add_edge(1,2)
G.add_edge(2,3,weight=4)
G.add_edge(1,4)
G.add_edge(2,4)


# draw the graph using Matplotlib
nx.draw(G, with_labels=True, font_weight='bold')

# display the plot
plt.show()
