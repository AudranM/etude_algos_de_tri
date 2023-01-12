from numpy import *
from random import *


def algo_main (tab: [int]) -> [int]:
    """
    pré-condition:
    post-condition : trie tab par ordre croissant
    """
    i = 0
    while i <len(tab):
        min = recherche_min (tab, i)
        indice_min = recherche_indice_min(tab,i, min)
        tmp = tab[i]
        tab[i] = min
        tab[indice_min] = tmp
        i+=1


def recherche_min(tab : [int], x : int) -> int:
    i = x
    min = tab[i]
    while i < len(tab):
        if tab[i] < min:
            min = tab[i]
        i += 1
    return min

def recherche_indice_min(tab: [int],x : int, min : int)-> int:
    i = x
    while i < len(tab):
        if tab[i] == min:
            return i
        i+=1