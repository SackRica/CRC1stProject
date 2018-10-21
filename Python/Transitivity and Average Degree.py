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
