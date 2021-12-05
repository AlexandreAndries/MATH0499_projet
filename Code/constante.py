

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import time as tm
import random as rand


NBR_SOMMETS = 170
NBR_COMMUNAUTES = 5
CONNEXITE = 0.055
INTERCONNEXITE = 0.00005
MORTAL = False

FRAMES = 12 + NBR_COMMUNAUTES//2
TOUR_GUERISON = 3

etatG = []
ancienConta = []
