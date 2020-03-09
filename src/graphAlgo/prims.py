
import copy
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from src.config import SAVE_LOCATION
plt.rcParams['figure.max_open_warning'] = 2000
plt.rcParams["figure.figsize"] = (19.5, 10.5)
# plt.rcParams["figure.figsize"] = (6.5, 3.5)
from src.generate_data import generate

generate(kind='matrix', size = 10)

G = nx.DiGraph()
pos = dict()
array = []
nodes_array = []
nodes_array.append([0])


def minm_dist(dist, mstSet, nVertices):
    min = 9999
    for v in range(nVertices):
        if(mstSet[v] == False and dist[v] < min):
            min = dist[v]
            min_index = v
    return min_index


def prims():
    nVertices = len(G.nodes())
    dist = []
    parent = [None] * nVertices
    mstSet = []
    for i in range(nVertices):
        dist.append(9999)
        mstSet.append(False)
    dist[0] = 0
    parent[0] = -1
    for count in range(nVertices - 1):
        u = minm_dist(dist, mstSet, nVertices)
        mstSet[u] = True
        for v in range(nVertices):
            if(u, v) in G.edges():
                if mstSet[v] == False and G[u][v]['length'] < dist[v]:
                    dist[v] = G[u][v]['length']
                    parent[v] = u

    for x in range(nVertices):
        if(parent[x] != -1):
            if (parent[x], x) in G.edges():
                nodes_array.append(nodes_array[-1] + [x])
                if(len(array) == 0):
                    array.append([[parent[x], x]])
                else:
                    array.append(array[-1] + [[parent[x], x]])





    





def CreateGraph():
    global n
    f = open('input.txt')
    n = int(f.readline())
    wtMatrix = []
    for i in range(n):
        list1 = f.readline().split()
        list1 = [x for x in list1 if x!= '']
        try:
            list1.remove('\n')
        except:
            pass
        list1 = list(map(int, list1))
        if(len(list1)!= 0):
            wtMatrix.append(list1)
    source = int(f.readline())  # source vertex from where BFS has to start
    # Adds egdes along with their weights to the graph
    for i in range(n):
        for j in range(n):
            if wtMatrix[i][j] > 0:
                G.add_edge(i, j, length=wtMatrix[i][j])
    # sorted(G, key=lambda x: x[-1])
    return G, source

def DrawGraph():
    pos = nx.spring_layout(G)
    # with_labels=true is to show the node number in the output graph
    nx.draw(G, pos, with_labels=True)
    edge_labels = dict([((u, v,), d['length'])
                        for u, v, d in G.edges(data=True)])
    # prints weight on all the edges
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=11)
    return pos

def animate(i):
    # print(i)
    # print(len(visited_list))
    plt.clf()
    nx.draw(G, pos, with_labels=True)
    edge_labels = dict([((u, v,), d['length'])
                        for u, v, d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=11)
    if(i >= len(nodes_array)):
        visite = nodes_array[-1]
    else:
        visite = nodes_array[i]
    nx.draw_networkx_nodes(G,pos,
                       nodelist=visite,
                       node_color='r',
                       node_size=500,
                   alpha=0.8)

    return nx.draw_networkx_edges(G, pos, array[i], width = 5, alpha = 0.6, edge_color = 'g')
    



def CreateVideo():
        fig = plt.figure()
        ani = animation.FuncAnimation(fig, animate, range(len(array)),interval = 1000,  blit=True, repeat_delay=5000, save_count = 1000)
        FFwriter=animation.FFMpegWriter(fps=1, extra_args=['-vcodec', 'libx264'])
        ani.save('prims.gif', writer='Pillow')

_, source = CreateGraph()
pos = DrawGraph()
prims()
for i in range(5):
    array.append(array[-1])
    nodes_array.append(nodes_array[-1])
CreateVideo()