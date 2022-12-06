from numpy import *
from random import *
def checktab (tab: [int]) -> bool:
    """
    pré-condition:
    post-condition: retourne vrai si le tableau est trié.
    """
    i=0
    longueur = len(tab)
    while i+1<longueur:
        if tab[i]>=tab[i+1]:
            return False
        else:
            i+=1
    return True
