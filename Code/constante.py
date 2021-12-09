

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import time as tm
import random as rand


default = input("Lancer avec paramètres par défaut ? (Y/N)\n")
while (default != 'Y') and (default != 'N'):
    default = input("Lancer avec paramètres par défaut ? (Y/N)\n")

if default == 'Y' :
    NBR_SOMMETS = 120
    NBR_COMMUNAUTES = 7
    CONNEXITE = 0.07
    INTERCONNEXITE = 0.00004
    MORTAL = False
    FRAMES = 12 + NBR_COMMUNAUTES//2
else :
    NBR_SOMMETS = int(input("Entrez nb de sommets par communauté (ex: 150) : "))
    NBR_COMMUNAUTES = int(input("Entrez nb de communautés (ex: 3) : "))
    CONNEXITE = float(input("Entrez le facteur de connexité intra-communauté (ex: 0.07) : "))
    INTERCONNEXITE = float(input("Entrez le facteur de connexité inter-communautés (ex: 0.0002) : "))
    MORTAL = bool(input("Le virus est-il mortel (True/False) ? "))
    FRAMES = 20 + NBR_COMMUNAUTES//2

FRAMES = 12 + NBR_COMMUNAUTES//2
TOUR_GUERISON = 3

etatG = []
ancienConta = []
