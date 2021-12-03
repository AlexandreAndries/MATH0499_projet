

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import time as tm
import random as rand


NBR_SOMMETS = 120
NBR_COMMUNAUTES = 7
CONNEXITE = 0.07
INTERCONNEXITE = 0.0002
MORTAL = False

FRAMES = 12 + NBR_COMMUNAUTES//2
TOUR_GUERISON = 3

etatG = []
ancienConta = []
