import networkx as nx
from getting_list import get_list, show
import matplotlib.pyplot as plt
def unique_list(n:list):
    return list(set(n))

def build_graph(srcId_list=None,dstID_list=None):
    if(srcId_list==None and dstID_list==None):
        srcId_list, srcType_list, dstID_list, edgeType_list, timestamp_list=get_list()
        # making unique list
        # show("Making Unique List from src and dst id")
        src_uni = unique_list(srcId_list)
        # dst_uni = unique_list(dstID_list)
        # print(f"length of Unique Src : {len(src_uni)}")
        # print(f"length of Unique Dst : {len(dst_uni)}")
        show("Making Graph Arrangement")
        G = nx.DiGraph()
        for src,dst in zip(srcId_list[:500],dstID_list[:500]):
            G.add_edge(src,dst)
        # G.add_nodes_from(dst_uni[:500])
        # for src,dst in zip(srcId_list[:500],dstID_list[:500]):
        #     G.add_edge(src,dst)                               
        return G, srcId_list[:500],dstID_list[:500]
    else:
        show("Making Graph Arrangement")
        G = nx.DiGraph()
        for src,dst in zip(srcId_list[:500],dstID_list[:500]):
            G.add_edge(src,dst)
        # G.add_nodes_from(dst_uni[:500])
        # for src,dst in zip(srcId_list[:500],dstID_list[:500]):
        #     G.add_edge(src,dst)                               
        return G, srcId_list[:500],dstID_list[:500]


def draw_graph():
    srcId_list, srcType_list, dstID_list, edgeType_list, timestamp_list=get_list()
    # src=srcId_list[5]
    # print(f"SrcID : {src}")
    # making unique list
    # show("Making Unique List from src and dst id")
    # src_uni = unique_list(srcId_list)
    # dst_uni = unique_list(dstID_list)
    # print(f"length of Unique Src : {len(src_uni)}")
    # print(f"length of Unique Dst : {len(dst_uni)}")
    show("Making Graph Arrangement")
    G = nx.DiGraph()
    # G.add_nodes_from(src)
    for src,dst in zip(srcId_list[:500],dstID_list[:500]):
        G.add_edge(src,dst)
    # for src,dst in zip(srcId_list[:500],dstID_list[:500]):
    #     G.add_edge(src,dst)
    # for dst in dstID_list[5:500]:
    #     G.add_edge(src,dst)

    nx.draw(G) 
    plt.show()   


if __name__=="__main__":
    draw_graph()