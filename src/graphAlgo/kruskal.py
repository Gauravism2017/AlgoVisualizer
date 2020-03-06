import copy
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from src.config import SAVE_LOCATION
plt.rcParams['figure.max_open_warning'] = 2000
plt.rcParams["figure.figsize"] = (19.5, 10.5)
from src.generate_data import generate

generate(kind='matrix', size = 10, density = 0.4)

G = nx.DiGraph()
n = 0
array = []
pos = dict()
nodes_array = []
def minEdge(checked):
    min = 99999
    for i in [(u, v, edata['length']) for u, v, edata in G.edges(data=True) if 'length' in edata]:
        # print(i)
        if(checked[i] == False and i[2] < min):
            min = i[2]
            min_edge = i
    return min_edge



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


# draws the graph and displays the weights on the edges
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


def root(a, id):
    while(id[a] != a):
        a = id[id[a]]
    return a

def union(a, b, id, level):
    _a = root(a, id)
    _b = root(b, id)
    if(level[_a] < level[_b]):
        id[_a] = _b
    elif(level[_a] > level[_b]):
        id[_b] = _a
    else:
        id[_a] = id[_b]
        level[_b] += 1

def krus(pos):
    elen = len(G.edges())
    vlen = len(G.nodes())
    mst = []
    checked = dict()
    for i in [(u, v, edata['length']) for u, v, edata in G.edges(data=True) if 'length' in edata]:
        checked[i] = 0
    id = [None] * vlen
    level = [None] * vlen
    nodes = set()
    for i in range(vlen):
        id[i] = i
        level[i] = 0
    while(len(mst) < vlen - 1):
        curr_edge = minEdge(checked)
        if(curr_edge is not None):
            checked[curr_edge] = 1
            y = root(curr_edge[1], id)
            x = root(curr_edge[0], id)
            if(x != y):
                nodes.add(x)
                nodes.add(y)
                temp = copy.deepcopy(nodes)
                # temp = list(temp)
                # _temp = copy.deepcopy(temp)
                nodes_array.append(temp)
                mst.append(curr_edge)
                temp = copy.deepcopy(mst)
                array.append(temp)
                union(x, y, id, level)

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
                       node_color='g',
                       node_size=500,
                   alpha=0.8)

    return nx.draw_networkx_edges(G, pos, array[i], width = 2.5, alpha = 0.6, edge_color = 'r')
    



def CreateVideo():
        fig = plt.figure()
        ani = animation.FuncAnimation(fig, animate, range(len(array)),interval = 1000,  blit=True, repeat_delay=5000, save_count = 1000)
        FFwriter=animation.FFMpegWriter(fps=1, extra_args=['-vcodec', 'libx264'])
        ani.save('Kruskal.mp4')
# main function
# if __name__ == "src.graphAlgo.BFS":
#     _, source = CreateGraph()
#     pos = DrawGraph()
#     BFS(G, source, pos)
#     CreateVideo()

_, source = CreateGraph()
pos = DrawGraph()
krus( pos)
for i in range(5):
    array.append(array[-1])
for i in range(5):
    array.insert(0, array[0])
for i in range(5):
    nodes_array.insert(0, nodes_array[0])
CreateVideo()







