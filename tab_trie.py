from numpy import *

def table_trie (n: int)-> [int]:
    """
    pre-cond: a est min et b est max
    post-cond: retourne un tableau de n entiers compris entre a(min) et b(max) trié
    """
    i = 0
    tab = zeros(n, int)
    while i < n : 
        tab[i]=i
        i+=1
    return tab