## @package graphe.py
#  
#  -Résumé:
#    Cette librairie contient les différentes fonctions utilisées pour la gestion/création de graphe
#
#  -Auteurs:
#    Alexandre Andries S19   Thomas Rotheudt S191896    


import networkx as nx
import matplotlib as plt
import random as rand

def init_graphe_aleatoire(nbrSommets):
    G = nx.Graph()
    
    for j in range(nbrSommets):
        G.add_node(j, weight = 'S')
    
    for i in range(nbrSommets):
        while len(G.adj[i]) <= 1:
            nbrAleatoire = (rand.randint(0, nbrSommets), rand.randint(0, nbrSommets))
            if nbrAleatoire[0] != nbrAleatoire[1]:
                G.add_edge(nbrAleatoire[0], nbrAleatoire[1])
            
    print(G)
    return G