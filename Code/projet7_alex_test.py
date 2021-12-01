## @package projet7
#
#  Main Projet 7 - MATH0499 Theorie des Graphes

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import graphe as gr
import time as tm
import random as rand


# ---------------------------------------------------------------------------- #
# -------------------------------- INIT -------------------------------------- #
# ---------------------------------------------------------------------------- #
NBR_SOMMETS = 30
NBR_ARCS = 70
FRAMES = 50

rand.seed()
# ---------------------------------------------------------------------------- #
# ------------------------------ FUNCTIONS ----------------------------------- #
# ---------------------------------------------------------------------------- #
"""
Résumé:
    Initialise un graphe aléatoire sur base d'un nombre de sommets et d'arcs
    donnés. Les sommets du graphes correspondent aux "personnes" appartenant à
    une "population" (i.e. l'ensemble du graphe) et les arcs représentent les
    liens entre ces personnes (i.e. si elles se fréquentent).
    Les sommets sont tous initialisés comme étant sain (S), à l'exception d'un
    sommet initialisé comme contaminé (C), c'est le patient zéro.

Paramètres:
    - nSommets: le nombre de sommets du graphes
    - nArcs: le nombre d'arcs du graphes

Retourne:
    - G, le graphe
    - layout, la disposition du graphe
"""


def init_graphe(nSommets, nArcs):
    G = nx.gnm_random_graph(nSommets, nArcs)
    layout = nx.spring_layout(G)

    for i in range(nSommets):
        G.nodes[i]['weight'] = 'S'

    patient_zero(G, nSommets)

    return G, layout


# ---------------------------------------------------------------------------- #
"""
Résumé:
    Initialise aléatoirement un élément du graphe comme étant contaminé.

Paramètres:
    - G, le graphe
    - nSommets: le nombre de sommets du graphes

Retourne:
    Ne retourne rien
"""


def patient_zero(G, nSommets):
    index = rand.randint(0, nSommets-1)
    G.nodes[index]['weight'] = 'C'

# ---------------------------------------------------------------------------- #


# INSERT NEW FUNCTIONS USED FOR PROPAGATION() HERE


# ---------------------------------------------------------------------------- #
"""
Résumé:
    Fonction de mise à jour de l'animation. Cette fonction gère la propagation
    du virus depuis le patient zéro jusqu'à la contamination de la population
    entière du graphe. Le virus se propage d'une personne à l'autre si celles-ci
    sont en contact.

Paramètres:
    - num, nombre d'image de l'animation
    - nSommets: le nombre de sommets du graphes
    - layout, la disposition du graphe
    - ax, ????? what the fuck is ax

Retourne:
    Ne retourne rien, permet l'évolution des contaminations
"""


def propagation(num, nSommets, layout, G, ax):
    ax.clear()

    color = []

    for i in range(len(G)):
        if G.nodes[i]['weight'] == 'S':
            color.append('grey')

        elif G.nodes[i]['weight'] == 'G':
            color.append('green')

        else:
            color.append('red')

    nx.draw(G, pos=layout, node_color=color, ax=ax, font_weight='bold')
    ax.set_title("Frame {}".format(num))

    # for j in range(len(G)):
    #     if G.nodes[j]['weight'] == 'C':
    #         liste_voisins = list(G.adj[j])
    #         print(liste_voisins)
    #         for i in liste_voisins:
    #             G.nodes[i]['weigth'] = 'C'

    #règle de changement d'etat du graphe (contamination, guérison ...)
    #modification de weight dans chaque node en fonction de l'adjacence
# ---------------------------------------------------------------------------- #
"""
Résumé:
    Fonction d'animation de la propagation du virus.

Paramètres:
    Pas de paramètre

Retourne:
    Rien, mais affiche l'animation du graphe
"""


def animate():
    global NBR_SOMMETS, NBR_ARCS, FRAMES

    fig, ax = plt.subplots(figsize=(6, 4))
    G, layout = init_graphe(NBR_SOMMETS, NBR_ARCS)

    ani = animation.FuncAnimation(fig,
                                  propagation,
                                  frames=FRAMES,
                                  fargs=(NBR_SOMMETS, layout, G, ax))

    ani.save('animation_1.gif', writer='imagemagick')

    plt.show()


# ---------------------------------------------------------------------------- #
# ------------------------------ MAIN LOOP ----------------------------------- #
# ---------------------------------------------------------------------------- #
animate()
