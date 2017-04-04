#When threshold is changed to 0.6
import numpy as np
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
#This dictionary stores the gene-expression data
everything  = defaultdict(list)
#This list holds all the genes of the network
all_keys = [ ]
#Initialize graph
G = nx.Graph()
file = ('C:\\Users\\hp\\Desktop\\breastcancer.txt')
with open(file) as f :
    first_line = f.readline()
    for line in f:
        m = line.strip("\n").split("\t")
        everything[ m[0] ] = m[ 1: ]
        all_keys.append( m[0] )
               

threshold = 0.7512
for key, value in everything.items():
    for key1, value1 in everything.items():
        if( key != key1 ):
            #Firstly, check if both genes don't match then find the correlation coefficient between two
            first_value = np.array(value).astype(np.float)
            second_value = np.array(value1).astype(np.float)
            values = round( np.corrcoef(first_value, second_value)[1,0] , 4 )
            print(values)
            #If pcc is greater than some threshold then both genes share an edge hence, draw an edge
            if values > threshold :
                G.add_edge(key , key1)
                #Now write to the edgelist
                nx.write_edgelist(G, 'C:\\Users\\hp\\Desktop\\edgelist060.txt' ,data=False) 






#clustering coefficient of all nodes
f = nx.average_clustering(G)
print(f)
#Shortest path length
sh = nx.shortest_path_length(G)
print(sh)
#Calculate number of nodes
print(nx.number_of_nodes(G))
#Calculate number of edges
print(nx.number_of_edges(G))
#Calculate average degree
cam = nx.read_edgelist('C:\\Users\\hp\\Desktop\\edgelist075.txt' , create_using = nx.DiGraph())
N, K = cam.order(), cam.size()
avg_deg = float(K)/N
print(avg_deg)
#Get clustering coefficient of each node
cc = nx.clustering(G)
print(cc)
#Get betweenness centrality of each node
bet = nx.betweenness_centrality(G)
print(bet)
#Average clustering coefficient 
avg_clust = sum(cc.values())/ len(cc)
print(avg_clust)
#Closeness centrality
close = nx.closeness_centrality(G)
print(close)
#Degree distribution
plt.hist(list(nx.degree(G).values()))
plt.ylabel('Number of nodes')
plt.xlabel('Degree')
plt.savefig('network_degree.png')
plt.show()






    
    
    
                
