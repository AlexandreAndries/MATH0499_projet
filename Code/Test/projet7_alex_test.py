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


def init_graphe(nSommets, nArcs):
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

    G = nx.gnm_random_graph(nSommets, nArcs)
    layout = nx.spring_layout(G)

    for i in range(nSommets):
        G.nodes[i]['weight'] = 'S'

    patient_zero(G, nSommets)

    return G, layout


# ---------------------------------------------------------------------------- #
def patient_zero(G, nSommets):
    """
    Résumé:
        Initialise aléatoirement un élément du graphe comme étant contaminé.

    Paramètres:
        - G, le graphe
        - nSommets: le nombre de sommets du graphes

    Retourne:
        Ne retourne rien
    """

    index = rand.randint(0, nSommets-1)
    G.nodes[index]['weight'] = 'C'

# ---------------------------------------------------------------------------- #


# INSERT NEW FUNCTIONS USED FOR PROPAGATION() HERE

def contaminer_voisins(G):
    liste_contacts = []

    for i in range(len(G)):
        if G.nodes[i]['weight'] == 'C':
            liste_contacts.extend(list(G.adj[i]))

    for contact in liste_contacts:
        # il faut ajouter ici une condition sur un nombre alétoire afin de
        # freiner la propagation du virus !
        G.nodes[contact]['weight'] = 'C'


# ---------------------------------------------------------------------------- #
def coloriage(G):
    color = []

    for i in range(len(G)):
        if G.nodes[i]['weight'] == 'S':
            color.append('grey')

        elif G.nodes[i]['weight'] == 'G':
            color.append('green')

        elif G.nodes[i]['weight'] == 'C':
            color.append('red')

    return color


# ---------------------------------------------------------------------------- #
def propagation(num, nSommets, layout, G, ax):
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
    ax.clear()

    # color.append(coloriage(G))

    random_colors = np.random.randint(2, size=NBR_SOMMETS)

    nx.draw(G, pos=layout, node_color=coloriage(G), ax=ax, font_weight='bold')
    ax.set_title("Frame {}".format(num))

    contaminer_voisins(G)

    #règle de changement d'etat du graphe (contamination, guérison ...)
    #modification de weight dans chaque node en fonction de l'adjacence
# ---------------------------------------------------------------------------- #


def animate():
    """
    Résumé:
        Fonction d'animation de la propagation du virus.

    Paramètres:
        Pas de paramètre

    Retourne:
        Rien, mais affiche l'animation du graphe
    """
    global NBR_SOMMETS, NBR_ARCS, FRAMES

    fig, ax = plt.subplots(figsize=(6, 4))
    G, layout = init_graphe(NBR_SOMMETS, NBR_ARCS)

    ani = animation.FuncAnimation(fig,
                                  propagation,
                                  frames=FRAMES,
                                  fargs=(NBR_SOMMETS, layout, G, ax),
                                  interval=500,
                                  blit=False)

    ani.save('animation_1.gif', writer='imagemagick')

    plt.show()


# ---------------------------------------------------------------------------- #
# ------------------------------ MAIN LOOP ----------------------------------- #
# ---------------------------------------------------------------------------- #
animate()
