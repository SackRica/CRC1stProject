import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
import pylab
import sys
from scipy.optimize import curve_fit


def fit_func(x, a):
    return (x ** a)


def getY(G):

	kv = [k for (v,k) in G.degree()]
	x = np.array([float(i) for i in range(1,max(kv)+1)])
	y = np.array([float(kv.count(i))/float(len(G)) for i in range(1,max(kv)+1)])
	params = curve_fit(fit_func, x, y, maxfev=10000)
	return params[0]


if __name__ == '__main__':

	file_name = sys.argv[1]

	print('Opening file ' + file_name)
	G = nx.read_edgelist(file_name, nodetype=int, data=(('_',int),('timestamp',int)))

	# Get the degree of each vertex
	kv = [k for (v,k) in G.degree()]

	data = np.array(kv)
	[a] = getY(G)
	print(a)

	# Change window title
	fig = pylab.gcf()
	fig.canvas.set_window_title('Degree Distribution')

	kmax = 100
	plt.hist(kv, bins=kmax+1, range=[0,kmax],  density=True)
	plt.plot([i for i in range(kmax+1)], [fit_func(x,a) for x in range(kmax+1)])

	# Show
	plt.show()



