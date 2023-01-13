from numpy import *
from time import *

import random_table as R
import tab_trie as T
import tab_inversement_trie as IT
import print_time as P
import algo_Z as Z
import algo_Y as Y
import algo_X as X
import algo_perso as AP

def time_to_sort (n : int, numero : int):
    i=0
    timetab = []
    min = -1000
    max = 1000
    if numero == 1:
        while i < n:
            tab1 = R.random_table(100*i,min,max)
            start = process_time()
            AP.algo_main(tab1)
            timetab.append(process_time() - start)
            i = i+1 
        return timetab

    elif numero == 2:
        while i < n:
            tab1 = T.table_trie(100*i)
            start = process_time()
            AP.algo_main(tab1)
            timetab.append(process_time() - start)
            i = i+1 
        return timetab

    elif numero == 3:
        while i < n:
            tab1 = IT.table_inverse(100*i)
            start = process_time()
            AP.algo_main(tab1)
            timetab.append(process_time() - start)
            i = i+1 
        return timetab
    
    else:
        return "erreur algo"