import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist('C:\\Users\\hp\\Desktop\\edgelist.txt',create_using = nx.DiGraph() , nodetype = str)
nx.draw(G)
nx.info(G)
plt.show()
