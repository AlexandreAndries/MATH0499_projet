import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import time as tm
import random as rand

def user_input() :
    global NBR_SOMMETS, NBR_COMMUNAUTES, CONNEXITE, INTERCONNEXITE, MORTALITE, FRAMES

    default = input("Lancer avec paramètres par défaut ? (Y/N)")

    if default == Y :
        NBR_SOMMETS = 120
        NBR_COMMUNAUTES = 7
        CONNEXITE = 0.07
        INTERCONNEXITE = 0.0002
        MORTAL = False
        FRAMES = 12 + NBR_COMMUNAUTES//2
    else :
        NBR_SOMMETS = int(input("Entrez nb de sommets par communauté (ex: 150) : "))
        NBR_COMMUNAUTES = int(input("Entrez nb de communautés (ex: 3) : "))
        CONNEXITE = int(input("Entrez le facteur de connexité intra-communauté (ex: 0.07) : "))
        INTERCONNEXITE = int(input("Entrez le facteur de connexité inter-communautés (ex: 0.0002) : "))
        MORTAL = bool(input("Le virus est-il mortel (True/False) ? "))
        FRAMES = 12 + NBR_COMMUNAUTES//2
