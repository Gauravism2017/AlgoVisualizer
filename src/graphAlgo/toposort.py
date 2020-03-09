from src.generate_data import generate
import networkx as nx
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from src.config import SAVE_LOCATION
plt.rcParams['figure.max_open_warning'] = 2000
# plt.rcParams["figure.figsize"] = (19.5, 10.5)
plt.rcParams["figure.figsize"] = (6.5, 3.5)
import copy

generate(kind='matrix', size=20)

nodes = 20
edges = 20
G = nx.DiGraph()
G1 = nx.DiGraph()
# BFS traversal
n = 0
_sorted = []
array = []
pos = dict()
_li = []
# visited_list = []

# _sorted = []


# def topologicalSort(pos):
# 	zero_indeg_list = []
# 	sorted_list = []
# 	visited = [False]*len(G.nodes())
# 	while len(G.nodes()) != 0:
# 		for node in G.nodes():
# 			if visited[node-1] == False:
# 				if G.in_degree(node) == 0:
# 					visited[node-1] = True
# 					zero_indeg_list.append(node)
# 		for node in zero_indeg_list:
# 			sorted_list.append(node)
# 			G.remove_node(node)
# 			zero_indeg_list.remove(node)
#           temp = copy.deepcopy(sorted_list)
#           array.append(temp)
# 	return sorted_list

def topologicalSort(pos):
    zero_indeg_list = []
    sorted_list = []
    visited = [False] * len(G.nodes())
    print(len(G.nodes()))
    while(len(G.nodes()) != 0):
        for node in G.nodes():
            # print('b')
            if(visited[node - 1] == False):
                # print('b')
                # print(G.in_degree(node))
                if(G.in_degree(node) == 0):
                    visited[node - 1] = True
                    
                    zero_indeg_list.append(node)
        for node in zero_indeg_list:
            sorted_list.append(node)
            G.remove_node(node)
            zero_indeg_list.remove(node)
            # temp = copy.deepcopy(sorted_list)
            array.append(copy.deepcopy(sorted_list))
    
    return sorted_list


# def CreateGraph():
#     global n
#     f = open('input.txt')
#     n = int(f.readline())
#     wtMatrix = []
#     for i in range(n):
#         list1 = f.readline().split()
#         list1 = [x for x in list1 if x!= '']
#         try:
#             list1.remove('\n')
#         except:
#             pass
#         # print(list1)
#         list1 = list(map(int, list1))
#         if(len(list1)!= 0):
#             wtMatrix.append(list1)
#     source = int(f.readline())  # source vertex from where BFS has to start
#     # Adds egdes along with their weights to the graph
#     for i in range(n):
#         for j in range(n):
#             if wtMatrix[i][j] > 0:
#                 G.add_edge(i, j, length=wtMatrix[i][j])
#     return G, source


def CreateGraph(nodes, edges):
    for i in range(nodes):
        G.add_node(i)
    while edges > 0:
        a = random.randint(0,nodes-1)
        b=a
        while b==a:
            b = random.randint(0,nodes-1)
        G.add_edge(a,b)
        if nx.is_directed_acyclic_graph(G):
            edges -= 1
        else:
            # we closed a loop!
            G.remove_edge(a,b)
    source = 0
    return G, source


# draws the graph and displays the weights on the edges
def DrawGraph():
    pos = nx.spring_layout(G)
    # with_labels=true is to show the node number in the output graph
    nx.draw(G, pos, with_labels=True)
    edge_labels = dict([((u, v,), random.randint(0, 5))
                        for u, v, d in G.edges(data=True)])
    # prints weight on all the edges
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=11)
    # plt.show()
    return pos

def animate(i):
    # print(1)
    plt.clf()
    nx.draw(G1, pos, with_labels=False)
    # plt.show()
    edge_labels = dict([((u, v,), 1)
                        for u, v, d in G1.edges(data=True)])
    
    nx.draw_networkx_edge_labels(
        G1, pos, edge_labels=edge_labels, label_pos=0.3, font_size=11)

    if i > 0 :
        if(i >= len(array)):
            visite = array[-1]
        else:
            visite = array[i]
        # if(i == 0):
            # nx.draw_networkx_edges(G, pos, array[i], width = 2.5, alpha = 0.6, edge_color = 'r')
        
        nx.draw_networkx_nodes(G,pos,
                        nodelist=visite,
                        node_color='r',
                        node_size=500,
                    alpha=0.8)
    # print(array[i])
    return nx.draw_networkx_edges(G, pos, _li[i], width = 2.5, alpha = 0.6, edge_color = 'r')
    # print('k')
    


def CreateVideo():
        fig = plt.figure()
        print(2)
        ani = animation.FuncAnimation(fig, animate, range(len(_li)),interval = 1000,  blit=True, repeat_delay=5000, save_count = 1000)
        FFwriter=animation.FFMpegWriter(fps=1, extra_args=['-vcodec', 'libx264'])
        ani.save('saves/gif/' + 'Topo.gif', writer='Pillow')



G, source = CreateGraph(nodes, edges)
G1 = copy.deepcopy(G)

pos= DrawGraph()
li = topologicalSort(pos)
_li.append([[li[0], li[1]]])
for i in range(1, len(li) - 1):
    _li.append(_li[-1] + [[li[i], li[i + 1]]])
    
# _li.insert(0, [])

for i in range(5):
    _li.append(_li[-1])
    array.append(array[-1])
print(_li)
CreateVideo()

