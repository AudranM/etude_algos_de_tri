from numpy import *
from random import *

def random_table (n: int, a: int, b: int)-> [int]:
    """
    pre-cond: a est min et b est max
    post-cond: retourne un tableau de n entiers compris entre a(min) et b(max)
    """
    i= 0
    tab = zeros(n, int)
    while i < n : 
        tab[i]=randint(a, b)
        i+=1
    return tab

