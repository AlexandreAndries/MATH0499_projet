## @package projet7
#
#   Cette librairie gère la boucle principale du projet

import networkx as nx
import matplotlib.pyplot as plt
import graphe as gr

NBR_SOMMETS = 30

color = []
i = 0

G = gr.init_graphe_aleatoire(NBR_SOMMETS)


nx.draw(G, font_weight='bold')
plt.show()  