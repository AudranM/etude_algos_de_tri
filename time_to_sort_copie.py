from numpy import *
from time import *

import random_table as R
import tab_trie as T
import tab_inversement_trie as IT
import print_time as P
import algo_Z as Z
import algo_Y as Y
import algo_X as X
import NEWalgo_perso as AP

def time_to_sort ():
    i=0
    timetab = []
    min = -1000
    max = 1000
    trie = int(input ("Choisir l'algorithme: \n1 pour X \n2 pour Y \n3 pour Z \n4 pour P \n"))
    tableau = int(input("Choisir le type de tableau: \n1 random \n2 trié \n3 inversement trié \n"))
    taille = int(input("Définir le nombre de tableau i tel que la taille de ceux-ci vaut i*100 \n"))
    while i < taille:
        if tableau == 1:
            tab1 = R.random_table(100*i,min,max)
        elif tableau == 2:
            tab1 = T.table_trie(100*i)
        elif tableau == 3:
            tab1 = IT.table_inverse(100*i)
        else:
            print("Erreur de saisie lors du choix du type de tableau")
            breakpoint()

        if trie == 1:
            start = process_time()
            X.algo_main(tab1)
            timetab.append(process_time() - start)
            i = i+1 

        elif trie == 2:
            start = process_time()
            Y.algo_main(tab1)
            timetab.append(process_time() - start)
            i = i+1 

        elif trie == 3:
            start = process_time()
            Z.algo_main(tab1)
            timetab.append(process_time() - start)
            i = i+1  
        
        elif trie == 4:
            start = process_time()
            AP.algo_main(tab1)
            timetab.append(process_time() - start)
            i = i+1
        else:
            print("Erreur de saisie lors du choix de l'algorithme de tri")
            breakpoint()
    return timetab