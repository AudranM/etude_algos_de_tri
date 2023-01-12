#SAE ALGO

# Notes et notices
Si jamais on a des trucs à se dire sur les projets ça peut être pratique de passer pour le README? 

Test Algo d'origine:

X : Fonctionne: OUI

Complexité: 
    - Temporelle: O(n²) car une première boucle parcourre le tableau n fois, et dans cette boucle, une autre boucle parcourre le tableau n fois. 
    - Spatiale:
        En place: OUI puisqu'on ne crée pas de nouveau tableau.

        Stable: NON car on vérifie que la valeur à classer (stockée dans tmp) est strctement inferieure à
        la valeur comparée. Au moment ou tmp sera comparé à une valeur identique à elle même, la boucle 
        continuera de tourner.


Y : Fonctionne
Complexité: 
    - Temporelle: O(n*log(n)) ca
    - Spatiale:
        En place: OUI

        Stable: NON puisque l'algorithme déplace les éléments vers la bonne position, donc il peut modifier l'ordre des éléments à valeurs égales.


Z : Ne Fonctionne Pas

Complexité: 
    - Temporelle:
    - Spatiale:
        En place: OUI

        Stable: NON, car en échangeant deux valeurs, on peut inverser l'ordre dans lequel ils apparaissaient. 