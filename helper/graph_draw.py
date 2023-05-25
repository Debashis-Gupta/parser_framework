import networkx as nx
from getting_list import get_list, show
import matplotlib.pyplot as plt
def unique_list(n:list):
    return list(set(n))

def draw_graph():
    srcId_list, srcType_list, dstID_list, edgeType_list, timestamp_list=get_list()
    # making unique list
    show("Making Unique List from src and dst id")
    src_uni = unique_list(srcId_list)
    dst_uni = unique_list(dstID_list)
    print(f"length of Unique Src : {len(src_uni)}")
    print(f"length of Unique Dst : {len(dst_uni)}")
    show("Making Graph Arrangement")
    G = nx.DiGraph()
    G.add_nodes_from(dst_uni[:50])
    for src,dst in zip(srcId_list[:500],dstID_list[:500]):
        G.add_edge(src,dst)

    nx.draw(G) 
    plt.show()   


if __name__=="__main__":
    draw_graph()