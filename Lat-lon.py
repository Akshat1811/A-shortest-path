

import osmnx as ox
import networkx as nx
import pandas as pd
import numpy as np
G = ox.graph.graph_from_address('Hyderabad', dist=100000, dist_type='network', network_type='all_private', simplify=True, retain_all=False, truncate_by_edge=False, return_coords=False, clean_periphery=True, custom_filter=None)
node_list = list(G.nodes(data = True))
edge_list = list(G.edges(data = True))
#print(edge_list[2])
#le = len(edge_list)
#len = len(node_list)

#print(le)
f = open('nodes.csv','w')
k = 0
f.write('id,lat,lon\n')
for i in node_list:

    f.write(str(node_list[k][0]))
    f.write(',')
    f.write(str(node_list[k][1]['y']))
    f.write(',')
    f.write(str(node_list[k][1]['x']))
    f.write('\n')
    k = k+1
#df = pd.DataFrame(node_list)
#df.to_csv('node.csv', index=False, header=True)
j = 0
f =open('edges.csv','w')
f.write('source,target,length\n')
for i in edge_list:

    #f.write(str(edge_list[j][2]['osmid'])+',')
    f.write(str(edge_list[j][0])+',')
    f.write(str(edge_list[j][1])+',')
    f.write(str(edge_list[j][2]['length']))
    f.write('\n')
    j = j + 1

