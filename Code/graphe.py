from constante import *

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
    ancienConta.append((index, 0))
# ---------------------------------------------------------------------------- #