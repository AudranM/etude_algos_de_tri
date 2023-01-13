from numpy import *
from random import *

import algo_perso as P
import random_table as R
import checktab as C
import algo_Z as Z
import algo_Y as Y
import algo_X as X
i=0
fonctionne = True
while i<100:
    tab1 = R.random_table(1000,1,100)
    if C.checktab(tab1):
        print("Le tableau", i, " était déjà trié avant intervention de l'algorithme")
    Z.algo_main(tab1)
    if C.checktab(tab1) == False :
        print ("Le tableau n'a pas été trié. Le problème est survenu lors de la vérification du tableau numéro", i+1)
        fonctionne = False
    i+=1
if fonctionne:
    print("L'algoritme fonctionne sur les 100 tableaux testés")
