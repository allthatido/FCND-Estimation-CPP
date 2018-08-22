import numpy as np             
import os
import sys

#change system directory to directory of the executing file
os.chdir(os.path.dirname(sys.argv[0]))

graph1 = np.genfromtxt('Graph1.txt', delimiter=',', dtype=None, encoding='utf8')
graph2 = np.genfromtxt('Graph2.txt', delimiter=',', dtype=None, encoding='utf8')

graph1_std = np.std(graph1[1:,1].astype('float32'), ddof=1)
graph2_std = np.std(graph2[1:,1].astype('float32'), ddof=1)

print(graph1[0,1].astype('str'), graph1_std, graph2[0,1].astype('str'), graph2_std)
