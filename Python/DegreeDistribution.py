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

plt.title('Distribuição de grau')
plt.xlabel('k', fontsize=12)
plt.ylabel('Pk', fontsize=12)

plt.hist(degrees, bins=max(degrees)+1,  density=True)
plt.show()
