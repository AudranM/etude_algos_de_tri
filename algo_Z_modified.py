from numpy import *

	
def algo_main(tab : [int]) -> None:
	"""
	pré-condition : 
	post-condition : trie tab par ordre croissant
	"""
	i=0
	while i < len(tab)-1:
		j=0
		while j < len(tab)-i-1:
			if tab[j] >= tab[j+1]:
				tmp = tab[j]
				tab[j]=tab[j+1]
				tab[j+1] = tmp
			j += 1
		i += 1


		

		
		
		
		
		
		
		
		
	
	
