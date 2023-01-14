from numpy import *
from random import *


import random_table as R
import checktab as C
import algo_Z as Z
import algo_Y as Y
import algo_X as X
import algo_perso as P

tab1 = R.random_table(50,1,100)
if C.checktab(tab1):
    print("Le tableau était déjà trié avant intervention de l'algorithme")
else:
    print("Le tableau n'était pas trié avant intervention de l'algorithme :")
    print(tab1)

X.algo_main(tab1)

if C.checktab(tab1):
    print("Le tableau a bien été trié : ")
    print(tab1)
else:
    print ("Le tableau n'a pas été trié : ")
    print(tab1)
