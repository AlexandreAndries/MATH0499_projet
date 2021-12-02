from matplotlib.animation import FuncAnimation
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')


def animate_nodes(G, node_colors, pos=None, *args, **kwargs):

    # define graph layout if None given
    if pos is None:
        pos = nx.spring_layout(G)

    # draw graph
    nodes = nx.draw_networkx_nodes(G, pos, *args, **kwargs)
    edges = nx.draw_networkx_edges(G, pos, *args, **kwargs)
    plt.axis('off')

    def update(ii):
        # nodes are just markers returned by plt.scatter;
        # node color can hence be changed in the same way like marker colors
        nodes.set_array(node_colors[ii])
        return nodes,

    fig = plt.gcf()
    animation = FuncAnimation(fig, update, interval=50,
                              frames=len(node_colors), blit=True)
    return animation


total_nodes = 10
graph = nx.complete_graph(total_nodes)
time_steps = 20
node_colors = np.random.randint(0, 100, size=(time_steps, total_nodes))

animation = animate_nodes(graph, node_colors)
animation.save('test.gif', writer='imagemagick',
               savefig_kwargs={'facecolor': 'white'}, fps=0.5)
