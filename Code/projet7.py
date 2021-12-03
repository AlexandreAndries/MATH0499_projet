## @package projet7
#
#  Main Projet 7 - MATH0499 Theorie des Graphes
import graphe as gr
import contamination as cont
from constante import *

# ---------------------------------------------------------------------------- #
# ------------------------------ FUNCTIONS ----------------------------------- #
# ---------------------------------------------------------------------------- #

def update_anim(num, layout, G, ax):
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
    global etatG

    ax.clear()


    nx.draw(G,
            pos=layout,
            node_color=etatG[num],
            ax=ax,
            font_weight='bold',
            node_size=50)

    ax.set_title("Frame {}".format(num))

# ----------------------------------------------------------------------------
def animate():
    """
    Résumé:
        Fonction d'animation de la propagation du virus.

    Paramètres:
        Pas de paramètre

    Retourne:
        Rien, mais affiche l'animation du graphe
    """
    global NBR_SOMMETS, NBR_COMMUNAUTES, CONNEXITE, INTERCONNEXITE, FRAMES, etatG

    fig, ax = plt.subplots(figsize = (14, 8))
    G, layout = gr.init_graphe( NBR_SOMMETS,
                                NBR_COMMUNAUTES,
                                CONNEXITE,
                                INTERCONNEXITE)
    cont.etape_contamination(G)

    ani = animation.FuncAnimation(fig,
                                  update_anim,
                                  frames=FRAMES,
                                  fargs=(layout, G, ax),
                                  interval = 800,
                                  blit=False)

    ani.save('animation_1.gif', writer='imagemagick')

    plt.show()

# ---------------------------------------------------------------------------- #
# ------------------------------ MAIN LOOP ----------------------------------- #
# ---------------------------------------------------------------------------- #
animate()
