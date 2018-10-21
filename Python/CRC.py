import os
import platform
import sys
import matplotlib.pyplot as plt
import pylab
import networkx as nx
import operator
import numpy as np
import collections

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

#Assortativity
s = nx.average_neighbor_degree(G, nodes=None, weight=None)
plt.figure()
plt.loglog(degrees, s.values(), 'ko', markersize=0.3, color = '#00868B')
plt.xlabel('Degree', fontsize=12)
plt.ylabel('Average Neighbor Degree', fontsize=12)
plt.show()
