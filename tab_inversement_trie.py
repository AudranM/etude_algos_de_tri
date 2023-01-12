from numpy import *

def table_inverse (n: int)-> [int]:
    """
    pre-cond: a est min et b est max
    post-cond: retourne un tableau de n entiers compris entre a(min) et b(max) inversement trié
    """
    i = n-1
    tab = zeros(n, int)
    while i >= 0 : 
        tab[i]=i
        i-=1
    return tab

