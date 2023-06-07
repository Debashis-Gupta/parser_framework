from graph_draw import build_graph
import matplotlib.pyplot as plt
import networkx as nx
import os
from getting_excel import data_from_excel
def build_subgraph(path,node_num):
    graph,source,dist = data_from_excel(path)
    nodes = nx.shortest_path(graph,str(source[node_num]))
    s = graph.subgraph(nodes)
    nx.draw(s, node_color='yellow')
    plt.savefig("subgraph.png",dpi=300)
    plt.show()
    print(f"Sourced node : {str(source[node_num])}")
    print(f"Connected Nodes : {nodes}")
    print(f"Number of node in subgraph : {len(nodes)}")
    # print(unique_source[0])
    # print(f"Named node : {str(source[4])}")
    # nodes = nx.shortest_path(graph,str(source[4]))
    # print(f"Connected Nodes : {nodes}")
    # s = graph.subgraph(nx.shortest_path(graph,nodes))
    # nx.draw(s, node_color='yellow')
    # plt.show()


if __name__=="__main__":
    current_dir = os.path.dirname(__file__)
    data_folder_path = os.path.join(current_dir, '..', 'data')
    path_list = os.path.join(data_folder_path, 'ta1-theia-e3-official-3_d.xlsx')
    build_subgraph(path=path_list,node_num=2)