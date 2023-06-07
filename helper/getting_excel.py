import pandas as pd
import os
from graph_draw import build_graph
import networkx as nx
import matplotlib.pyplot as plt
def data_from_excel(path):
    # print(path)
    data = pd.read_excel(path)
    src_list = list(data['SrcID'][:2900])
    dst_list = list(data['DstID'][:2900])
    # print(src_list)
    # print(dst_list)
    print("----------Loading Build Graph-----------")
    graph,source,dst = build_graph(srcId_list=src_list,dstID_list=dst_list)
    print("----------Finish Building Graph-----------")
    return graph,source,dst
    



if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    data_folder_path = os.path.join(current_dir, '..', 'data')
    path_list = os.path.join(data_folder_path, 'ta1-theia-e3-official-3_d.xlsx')
    data_from_excel(path_list)
