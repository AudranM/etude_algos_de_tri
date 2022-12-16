from numpy import *

	
def algo_main(tab : [int]) -> None:
	"""
	pré-condition : 
	post-condition : trie tab par ordre croissant
	"""
	
	i=1
	#La variable i parcourt le tab en partant de la deuxième valeur
	while i < len(tab):
		j=i-1
		#La valeur contenue dans tab[i] est affecté à tmp
		tmp = tab[i]
		"""
		tant que la valeur de tmp est inferieur à tab[j] et tant que
		j >= à l'indice min du tab:
		"""
		while tmp < tab[j] and j >= 0:
                        #on copie la valeur de tab[j] à l'indice d'après 
			tab[j+1] = tab[j]
			#j est décrémenté de 1
			j -= 1
		#on copie la valeur stockée dans tmp à l'indice ou il doit etre classé
		tab[j+1] = tmp
		i += 1
