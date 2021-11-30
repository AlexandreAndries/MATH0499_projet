"""
Résumé:
    module gérant les fonctions liées aux modifications de graphe du projet

Auteurs:
    Alexandre Andries
    Thomas Rotheudt
"""


import networkx as nx
import matplotlib.pyplot as plt
import random as rand


def init_graphe_aleatoire(nbrSommets):
    """
        Résumé:
            Crée un graphe connexe aléatoire avec "nbrSommets" noeuds et un nombre d'arêtes aléatoires

        Paramètres:
            -nbrSommets le nombre de sommets du graphe

        Retourne:
            -G un graphe aléatoire
    """
    G = nx.Graph()

    for j in range(nbrSommets): #Boucle initialisant les différents noeuds du graphe Gs
        G.add_node(j, weight = 'S')

    for i in range(nbrSommets): #Boucle parcourant les différents noeuds du graphe G

        while len(G.adj[i]) <= 2: #Pour chaque noeuds on crée des liaisons aléatoires entre des noeuds aléatoires tant que le degré de chaque noeuds n'est pas au minimum égale à 2
            nbrAleatoire = (rand.randint(0, nbrSommets-1), rand.randint(0, nbrSommets-1))

            if nbrAleatoire[0] != nbrAleatoire[1]:
                G.add_edge(nbrAleatoire[0], nbrAleatoire[1])

    return G

def afficher_graphe(Graphe):
    """
    Résumé:
        Affiche le graphe "Graphe" dans une fenêtre à part.

    Paramètres:
        -Graphe: le graphe à afficher

    Retourne:
        Ne retourne rien mais affiche une fenêtre avec le graphe "Graphe"
    """
    color = []

    for i in range(len(Graphe)):
        if Graphe.nodes[i]['weight'] == 'S':
            color.append('grey')

        elif Graphe.nodes[i]['weight'] == 'G':
            color.append('green')

        else:
            color.append('red')

    nx.draw(Graphe, node_color = color ,font_weight='bold')
    plt.show()


def verifier_population(Graphe) :
    """
    Résumé:
        Vérifie l'état de contamination de la population.

    Paramètres:
        -Graphe: le graphe à afficher

    Retourne:
        True si l'entiereté de la population a été contaminée.
        False sinon.
    """
    compteur = 0
    for i in range(len(Graphe)):
        if Graphe.nodes[i]['weight'] == 'C':
            compteur += 1

    if compteur == len(Graphe) :
        return True
    else :
        return False
