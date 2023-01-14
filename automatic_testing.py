from numpy import *
from random import *

import algo_perso as P
import random_table as R
import checktab as C
import algo_Z as Z
import algo_Z_modified as ZM
import algo_Y as Y
import algo_X as X

def automatic_testing()->None:
    """
    pre-cond: /
    post-cond: /
    """
    type_tri = int(input ("Bonjour.\nTapez 1 si vous souhaitez tester le tri d'un tableau en détail.\nTapez 2 si vous souhaitez tester le tri de plusieurs tableaux de taille exponentielle.\n"))

    if type_tri == 1:
       taille_tab = int( input ("Entrez la taille du tableau à tester\n"))
       min_valeur = int( input ("Entrez la valeur minimum du tableau à tester\n"))
       max_valeur = int( input ("Entrez la valeur maximum du tableau à tester\n"))
       numero_algo = int(input ("Choisissez l'algorithme: \n1 pour X \n2 pour Y \n3 pour Z \n4 pour P \n5 pour Z modifié. \n"))
       if min_valeur > max_valeur:
            print("Erreur de saisie: minimum supérieur au maximum.\nLes valeurs ont été échangées.\nLe programme va s'executer normalement.\n\n")
            tmp = max_valeur
            max_valeur = min_valeur
            min_valeur = tmp
       test_tri_detail(taille_tab, min_valeur, max_valeur, numero_algo)
       
    elif type_tri == 2:
        nombre_tableaux = int( input ("Entrez le nombre de tableaux à tester\n"))
        numero_algo = int(input ("Choisissez l'algorithme: \n1 pour X \n2 pour Y \n3 pour Z \n4 pour P \n5 pour Z modifié. \n"))
        print("Merci de patienter pendant le traitement de votre demande\n")
        test_tri_boucle (nombre_tableaux, numero_algo)
    else:
        print("Erreur de saisie. Merci de recommencer.")
        automatic_testing ()
        
def test_tri_boucle( nombre_tableaux : int, numero_algo: int) -> None:
    """
    pre-cond: nombre_tableaux >= 1
    post-cond: /
    """
    i=0
    fonctionne = True
    while i<nombre_tableaux:
        tab1 = R.random_table(100*i,1,100)
        if C.checktab(tab1):
            print("Le tableau", i, " était déjà trié avant intervention de l'algorithme\n")
            
        if numero_algo == 1:
            X.algo_main(tab1)
        elif numero_algo == 2:
            Y.algo_main(tab1)
        elif numero_algo == 3:
            Z.algo_main(tab1)
        elif numero_algo == 4:
            P.algo_main(tab1)
        elif numero_algo == 5:
            ZM.algo_main(tab1)
            
        if C.checktab(tab1) == False :
            print ("Le tableau numéro ", i+1, " n'a pas été trié\n")
            fonctionne = False
        else :
            print ("Le tableau numéro ", i+1, " a été trié\n")
        i+=1
        
    if fonctionne:
        print("\n\nChacun des ", nombre_tableaux, " tableaux testés étaient trié à la fin de l'exécution de l'algorithme.\n")
    else:
        print("\n\nDes problèmes sont survenus lors du tri des tableaux.\n")

    
def test_tri_detail(taille_tab: int, min_valeur: int, max_valeur: int, numero_algo: int)-> None:
    """
    pre-cond: min_valeur < max_valeur, numero_algo = 1 ou 2 ou 3 ou 4 ou 5
    post-cond: 
    """
    deja_trie = False
    tab1 = R.random_table(taille_tab,min_valeur,max_valeur)
    if C.checktab(tab1):
        print("Le tableau était déjà trié avant intervention de l'algorithme")
        deja_trie = True
    else:
        print("Le tableau n'était pas trié avant intervention de l'algorithme :")
        print(tab1)
        
    if deja_trie == False:
            
        if numero_algo == 1:
            X.algo_main(tab1)
        elif numero_algo == 2:
            Y.algo_main(tab1)
        elif numero_algo == 3:
            Z.algo_main(tab1)
        elif numero_algo == 4:
            P.algo_main(tab1)
        elif numero_algo == 5:
            ZM.algo_main(tab1)
            
        if C.checktab(tab1):
            print("Le tableau a bien été trié : ")
            print(tab1)
        else:
            print ("Le tableau n'a pas été trié : ")
            print(tab1)

        
automatic_testing ()
continuer = True
while continuer:
    reponse = int(input("\nVoulez-vous continuer de trier des tableaux?\n Tapez 1 si oui, tapez 2 si non.\n"))
    if reponse == 1:
        automatic_testing ()
    elif reponse ==2:
        print("Au revoir!")
        continuer = False
    else:
        print("Saisie invalide. Au revoir.")
        continuer = False

