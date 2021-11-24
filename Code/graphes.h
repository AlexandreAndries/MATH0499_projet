#if defined(GRAPHES_H)
#else
#define GRAPHES_H

#define MAX 10000

typedef struct eltadj {
	int dest;
	int info;
	struct eltadj *suivant;
}ELTADJ;

typedef struct sommet {
	int label;
	int info;
	struct sommet *suivant;
	ELTADJ *adj;
}SOMMET;


typedef struct graphe {
	int nbS;
	int nbA;
	int maxS;
	SOMMET *premierSommet;
	SOMMET *dernierSommet;
}GRAPHE;

/**
 * \fn void initialiserGraphe(GRAPHE *)
 * \brief Initilise un graphe vide
 *
 * \param g un graphe
 *
 * \pre
 * \post g != NULL
 *
 * \return
 */
void initialiserGraphe(GRAPHE *g);

/**
 * \fn int ajouterSommet(GRAPHE *g, int info)
 * \brief ajoute un sommet au graphe g
 *
 * \param g un graphe
 * \param info info du sommet
 *
 * \pre g != NULL
 * \post g possède un sommet supplémentaire avec l'info "info"
 *
 * \return
 *      -1 si l'allocation du sommet à échoué
 *			 psommet->label si tout va bien
 */
int ajouterSommet(GRAPHE *g, int info);

/**
 * \fn int ajouterArc(GRAPHE *g, int a, int b, int info)
 * \brief ajoute un arc au graphe g
 *
 * \param g un graphe
 * \param a origine de l'arc à créer
 * \param b destination de l'arc à créer
 * \param info info de l'arc
 *
 * \pre g != NULL
 * \post g possède un nouvel arc d'origine a et de destination b
 *
 * \return
 *      -1 si l'allocation du sommet à échoué
 *			-2 si création d'un arc dont l'extremite n'existe pas
 *			-3 mémoire insuffisante pour creer un sommet
 *			 0 si tout va bien
 */
int ajouterArc(GRAPHE *g, int a, int b, int info);

/**
 * \fn int supprimerSommet(GRAPHE *g, int label)
 * \brief supprime un sommet au graphe g
 *
 * \param g un graphe
 * \param label label du sommet à supprimer
 *
 * \pre g != NULL
 * \post le sommet de label "label" est supprimer du graphe g
 *
 * \return
 *      -1 si graphe vide, suppression impossible
 *			 0 si tout va bien
 */
int supprimerSommet(GRAPHE *g, int label);

/**
 * \fn int supprimerArc(GRAPHE *g, int a, int b)
 * \brief supprime un arc du graphe g
 *
 * \param g un graphe
 * \param a origine de l'arc
 * \param b destination de l'arc
 *
 * \pre g != NULL
 * \post l'arc d'origine a et de destination b est supprimer du graphe g
 *
 * \return
 *      -1 si l'extremite de l'arc a supprimer n'existe pas
 *			 0 si tout va bien
 */
int supprimerArc(GRAPHE *g, int a, int b);

/**
 * \fn void supprimerGraphe(GRAPHE *g)
 * \brief supprime un graphe g
 *
 * \param g un graphe
 *
 * \pre g != NULL
 * \post g = NULL
 *
 * \return
 */
void supprimerGraphe(GRAPHE *g);

/**
 * \fn void afficherGraphe(GRAPHE *g)
 * \brief affiche graphe g
 *
 * \param g un graphe
 *
 * \pre g != NULL
 * \post g est afficher sur terminal
 *
 * \return
 */
void afficherGraphe(GRAPHE *g);

int lireFichier(char *nomf, GRAPHE *g);

#endif
