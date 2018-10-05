import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
import pylab
import sys

# Input 1 -> GML file

if __name__ == '__main__':

	# Load graph using gml format
	file_name = sys.argv[1]
	G = nx.read_gml(file_name,True)

	# Get the degree of each vertex
	kv = [k for (v,k) in G.degree()]

	# Change window title
	fig = pylab.gcf()
	fig.canvas.set_window_title('Degree Distribution')

	# Set graph labels
	file_path_splitted = file_name.split("/")
	number_of_directories = len(file_path_splitted)

	# Set histogram
	kmax = max(kv)
        plt.subplot(1, 2, 1)
        plt.hist(kv, bins=kmax+1, range=(0,kmax+1), normed=True)
	plt.title('Network Graph: ' + file_path_splitted[number_of_directories-1].split('.')[0].upper())
	plt.xlabel('Degree of vertexes')
	plt.ylabel('Number of vertexes')

	# Draw graph
        plt.subplot(1, 2, 2)
        color_map = [(0,1.-float(v)/float(kmax),0) for v in kv] # Set color for each vertex
        pos = nx.spring_layout(G,k=0.15,iterations=20)
        nx.draw(G,node_color=color_map, pos=pos)
        
	# Show
        plt.show()
        
