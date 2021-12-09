from constante import *


def coloriage(G):
    '''
    Résumé:
        Récupère les couleurs des noeuds du graphe

    Paramètres:
        - G, le graphe

    Retourne:
        -color, une liste des couleurs des noeuds (dans l'ordre des indices des noeuds)

    '''
    color = []

    for i in range(len(G)):
        if G.nodes[i]['weight'] == 'S':
            color.append('grey')

        elif G.nodes[i]['weight'] == 'G':
            color.append('green')

        elif G.nodes[i]['weight'] == 'C':
            color.append('red')

        elif G.nodes[i]['weight'] == 'D':
            color.append('purple')

    return color
# ---------------------------------------------------------------------------- #
def nettoyage_anciens_conta(listeConta, tourInfection):
    global ancienConta
    listeContaFormat = []

    listeConta = list(set(listeConta))

    for i in ancienConta:
        if i[0] in listeConta:
            listeConta.remove(i[0])

    for n in listeConta:
        listeContaFormat.append((n,tourInfection))

    ancienConta.extend(listeContaFormat)
    ancienConta = list(set(ancienConta))


    return listeConta
# ---------------------------------------------------------------------------- #
def etape_contamination(G):
    '''
    Résumé:
        Récupère les différentes étapes de contamination du graphe G
    Paramètres:
        - G, le graphe
    Retourne:
        Ne retourne rien
    '''
    global etatG, ancienConta, MORTAL

    etatG.append(coloriage(G))

    for i in range(1, FRAMES):
        listeContacts = []

        for j in range(len(G)):
            if G.nodes[j]['weight'] == 'C':
                listeContacts.extend(list(G.adj[j]))

        listeContacts = nettoyage_anciens_conta(listeContacts, i)

        for k in listeContacts:
            G.nodes[k]['weight'] = 'C'

        for n in ancienConta:
            if MORTAL == False and i == n[1]+TOUR_GUERISON:
                    G.nodes[n[0]]['weight'] = 'G'
            elif MORTAL == True and i == n[1]+TOUR_GUERISON :
                if rand.randint(0,4) < 3 :
                    G.nodes[n[0]]['weight'] = 'G'
                else :
                    G.nodes[n[0]]['weight'] = 'D'

        etatG.append(coloriage(G))
# ----------------------------------------------------------------------------#
