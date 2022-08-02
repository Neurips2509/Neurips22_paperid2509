from generate_xu_instances import get_random_instance
import networkx as nx
import pandas as pd
from torch_geometric.utils import from_networkx
import pickle
cliquelist = []
graphlist = []
hardnessdict = {'Easy': 0.2, 'Medium': 0.5,'Hard':0.8}
datasets = ["Easy","Medium","Hard"]
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--dataset_name', type=str, default='Hard',
                    help='dataset name')
parser.add_argument('--hardnesspara', type=float, default='0.8',
                    help='hardnesspara')
args = parser.parse_args()
dataset_name = args.dataset_name
hardnesspara = args.hardnesspara
from graph2dimacs import *
print('Harness Dataset :%s'%dataset_name)
print('Hardness parameter: %.2f'%hardnesspara)
i = 0
while i < 1000:
#while i < 400:
    graph,Ncli = get_random_instance(hardness = hardnesspara) # hard 0.8, easy: 0.2, medium: 0.5
    graph = graph.to_undirected()
    graph.remove_edges_from(nx.selfloop_edges(graph))
    if nx.is_connected(graph):
#    if True:
        data = graph
        nnodes = graph.number_of_nodes()
        if (nnodes>=10)and(nnodes<=300):
            graph2dimacs('Datasets/'+dataset_name+'/graphid%d'%i,data)
            print("Index: %d, Number of Nodes:%d"%(i,nnodes))
            print("The MC is:%d"%Ncli)
            i = i + 1
        else:
            pass
    else:
        print('Node not connect!')
    print("---------%d============"%i)
#with open("Datasets/Large_medium_Cliques_%s.p"%dataset_name, 'wb') as f:
#    pickle.dump(graphlist, f)
#with open("Datasets/Large_medium_Cliques_%s_sol.p"%dataset_name, 'wb') as f:
#    pickle.dump(cliquelist, f)
