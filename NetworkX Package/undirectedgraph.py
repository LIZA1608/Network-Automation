import networkx

# To create an empty undirected graph
G = networkx.Graph()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(7)
G.add_node(9)
G.add_node(8)

# To add an edge
# Note graph is undirected
# Hence order of nodes in edge doesn't matter
G.add_edge(1,2)
G.add_edge(3,1)
G.add_edge(2,4)
G.add_edge(4,1)
G.add_edge(9,1)
G.add_edge(1,7)
G.add_edge(2,9)

# To get all the nodes of a graph
node_list = G.nodes()
print("#1")
print(node_list)

# To get all the edges of a graph
edge_list = G.edges()
print("#2")
print(edge_list)

# To remove a node of a graph
G.remove_node(2)
node_list = G.nodes()
print("#3")
print(node_list)

# To get all the edges of a graph
edge_list = G.edges()
print("#4")
print(edge_list)


# To remove an edge of a graph
G.remove_edge(1,3)
edge_list = G.edges()
print("#5")
print(edge_list)

# To find number of nodes
n = G.number_of_nodes()
print("#6")
print(n)

# To find number of edges
m = G.number_of_edges()
print("#7")
print(m)

# To find degree of a node
# d will store degree of node 2
d = G.degree(1)
print("#8")
print(d)

# To find all the neighbor of a node
neighbor_list =list( G.neighbors(1))
print("#9")
print(neighbor_list)
