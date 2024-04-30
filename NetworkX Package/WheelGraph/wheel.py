

# import required module
import networkx
 
# importing matplotlib.pyplot
import matplotlib.pyplot as plt

# number of nodes
n = 5
 
# create object
G = networkx.wheel_graph(n)
 
# illustrate graph
networkx.draw(G)
plt.savefig("Wheel.png")
