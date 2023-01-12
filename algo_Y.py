from numpy import *


def algo_a(tab: [int], i: int, j: int) -> None:
	"""
	pré-condition: 0 <= i, j < len(tab)
	post-condition: ?
	"""
	m = (i+j)//2 
	x=m+1
	while x <= j:
		tmp = tab[x]
		k = x-1
		while tmp <= tab[k] and k >= i:
			tab[k+1]=tab[k]
			k -= 1
		tab[k+1] = tmp
		x += 1
		
def algo_b(tab: [int], i: int, j: int) -> None:
	"""
	pré-condition: 0 <= i, j < len(tab)
	post-condition: ?
	"""
	if i==j:
		return
	if j-i == 1:
		if tab[i] > tab[j]:
			tmp = tab[i]
			tab[i] = tab[j]
			tab[j] = tmp
	elif j - i > 1 :
		m = (i+j)//2 #milieu = division entière indice min + indice max /2 
		algo_b(tab, i, m) #appel récursif avec indice min et milieu
		algo_b(tab, m+1,j) #appel récursif avec milieu +1 et indice max
		algo_a(tab, i, j)
	
def algo_main(tab : [int]) -> None:
	"""
	pré-condition : 
	post-condition : trie tab par ordre croissant
	"""
	algo_b(tab, 0, len(tab)-1)
