from numpy import *
from random import *
from time import *

import numpy as np
import matplotlib.pyplot as plt
import random_table as R
import algo_Z as Z
import algo_Y as Y
import algo_X as X

i=0
taille = 100
timetab = []
while i < 100:
    tab1 = R.random_table(100*i,1,50)
    start = process_time()
    Y.algo_main(tab1)
    timetab.append(process_time() - start)
    print(tab1)
    print(timetab)
    i = i+1 
plt.title("Rapport de Vitesse")
plt.plot(timetab)
plt.xlabel('Nombre')
plt.ylabel('Temps')
plt.show()