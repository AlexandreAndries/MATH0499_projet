/**
 * \file main.c
 * \brief Ce fichier contient la fonction main du programme
 * \author: Rotheudt Thomas S191895 Alexandre Andries S196948
 * @projet: MATH0499
 */
 #include <stdio.h>
 #include <stdlib.h>
 #include "graphes.h"


 int main(){
   GRAPHE *g = malloc(sizeof(GRAPHE *));
   initialiserGraphe(g);

   ajouterSommet(g, 1);


   //afficherGraphe(g);

   return 0;
 }
