from numpy import *

	
def algo_main(tab : [int]) -> None:
	"""
	pré-condition : 
	post-condition : trie tab par ordre croissant
	"""
	i=1
	while i < len(tab):
		j=i-1
		tmp = tab[i]
		while tmp < tab[j] and j >= 0:
			tab[j+1] = tab[j]
			j -= 1
		tab[j+1] = tmp
		i += 1
