from numpy import *
from random import *


def algo_main (tab: [int]) -> [int]:
    """
    pré-condition:
    post-condition : trie tab par ordre croissant
    """
    i = 0
    while i <len(tab):
        min_et_indice = recherche_min (tab, i)
        min = min_et_indice[0]
        indice_min = min_et_indice[1]
        tmp = tab[i]
        tab[i] = min
        tab[indice_min] = tmp
        i+=1


def recherche_min(tab : [int], x : int) -> numpy.ndarray:
    i = x
    min = tab[i]
    indice_min = i
    while i < len(tab):
        if tab[i] < min:
            min = tab[i]
            indice_min = i
        i += 1
    return array([min, indice_min])

