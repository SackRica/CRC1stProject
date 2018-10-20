import os
import platform
import sys
import matplotlib.pyplot as plt
import pylab
import networkx as nx
import matplotlib.pyplot as plt
import operator
import numpy as np

G= nx.read_weighted_edgelist("../../fb_edgeList.txt", nodetype=int)

degrees = [k for (v,k) in G.degree()]

#Transitivity
print('Clustering coefficient', nx.transitivity(G))

#Average Degree
print('Average degree: ', sum(degrees)/G.number_of_nodes())

#Degree distribution
plt.title('Distribuição de grau')
plt.xlabel('k', fontsize=12)
plt.ylabel('Pk', fontsize=12)

plt.hist(degrees, bins=max(degrees)+1,  density=True)
plt.show()

#Degree distribution log
plt.title('Distribuição de grau')
plt.xlabel('k', fontsize=12)
plt.ylabel('Pk', fontsize=12)

plt.loglog(distinct_degrees, y, 'o',markersize=0.75, color = '#00868B')
plt.show()
