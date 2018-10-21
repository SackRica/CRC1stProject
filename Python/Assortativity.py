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

s = nx.average_neighbor_degree(G, nodes=None, weight=None)
plt.figure()
plt.loglog(degrees, s.values(), 'ko', markersize=0.3, color = '#00868B')
plt.xlabel('Degree', fontsize=12)
plt.ylabel('Average Neighbor Degree', fontsize=12)
plt.show()
