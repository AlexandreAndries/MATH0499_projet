## @package projet7
#
#   Cette librairie gère la boucle principale du projet et contient l'algorithme du projet

import networkx as nx
import matplotlib.pyplot as plt
import graphe as gr
import time as tm

NBR_SOMMETS = 20
temps = tm.time()

G = gr.init_graphe_aleatoire(NBR_SOMMETS)
gr.afficher_graphe(G)
