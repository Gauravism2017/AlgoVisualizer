import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from src.config import SAVE_LOCATION
plt.rcParams['figure.max_open_warning'] = 2000
# plt.rcParams["figure.figsize"] = (19.5, 10.5)
plt.rcParams["figure.figsize"] = (6.5, 3.5)

from src.generate_data import generate

generate(kind='matrix', size = 20)


G = nx.DiGraph()
# BFS traversal
n = 0
array = []
visited_list = []
def BFS(G, source, pos):
    # visited = [False]*(len(G.nodes()))
    visited = [False] * n

    queue = []
    # print(len(G.nodes()))
    queue.append(source)
    visited_list.append([source])
    visited[source] = True
    while queue:
        curr_node = queue.pop(0)
        if(len(G[curr_node]) != 0):
            for i in G[curr_node]: 

                # iterates through all the possible vertices adjacent to the curr_node
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    visited_list.append(visited_list[-1] + [i])
                    if(len(array) > 0):
                        array.append([pos, array[-1][1] + [(curr_node,i)]])
                    else:
                        array.append([pos, [[curr_node, i]]])
                    # nx.draw_networkx_edges(G, pos, edgelist = [(curr_node,i)], width = 2.5, alpha = 0.6, edge_color = 'r')
                    # plt.show()
    return


# takes input from the file and creates a weighted graph
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
        # print(list1)
        list1 = list(map(int, list1))
        if(len(list1)!= 0):
            wtMatrix.append(list1)
    source = int(f.readline())  # source vertex from where BFS has to start
    # Adds egdes along with their weights to the graph
    for i in range(n):
        for j in range(n):
            if wtMatrix[i][j] > 0:
                G.add_edge(i, j, length=wtMatrix[i][j])
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
        G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=11, width = 0.5)
    return pos

def animate(i):
    # print(i)
    # print(len(visited_list))
    plt.clf()
    nx.draw(G, array[i][0], with_labels=True)
    edge_labels = dict([((u, v,), d['length'])
                        for u, v, d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(
        G, array[i][0], edge_labels=edge_labels, label_pos=0.3, font_size=11)
    if(i >= len(visited_list)):
        visite = visited_list[-1]
    else:
        visite = visited_list[i]
    nx.draw_networkx_nodes(G,array[i][0],
                       nodelist=visite,
                       node_color='r',
                       node_size=500,
                   alpha=0.8)
    return nx.draw_networkx_edges(G, array[i][0], array[i][1], width = 2.5, alpha = 0.6, edge_color = 'r')
    


def CreateVideo():
        fig = plt.figure()
        ani = animation.FuncAnimation(fig, animate, range(len(array)),interval = 1000,  blit=True, repeat_delay=5000, save_count = 1000)
        FFwriter=animation.FFMpegWriter(fps=1, extra_args=['-vcodec', 'libx264'])
        ani.save('saves/gif/' + 'BFS.gif', writer='Pillow')

# main function
# if __name__ == "src.graphAlgo.BFS":
#     _, source = CreateGraph()
#     pos = DrawGraph()
#     BFS(G, source, pos)
#     CreateVideo()

_, source = CreateGraph()
pos = DrawGraph()
BFS(G, source, pos)
for i in range(5):
    array.append(array[-1])

CreateVideo()