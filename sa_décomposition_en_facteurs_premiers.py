#!/usr/bin/python3
# coding: utf-8


def décomposition (nb_à_dec, indice, produits):
    indice = 2
    produits = “1”
    if (est_premier (nb_à_dec)):
        print (“Ce nombre n’a pas de diviseur autre que lui-même et un.”)
        return False
    else:
        while (indice < nb_à_dec):
            if (nb_à_dec % indice == 0):
                produits = produits + “*” + str(indice)
                nb_à_dec = int(nb_à_dec / indice)
                indice = indice - 1
                if (est_premier (nb_à_dec)):
                    produits = produits + “*” + str(nb_à_dec)
            indice = indice + 1
    return produits
##################################################
def est_premier (nb):
    nb_premier = True
    for i in range (2, nb):
        if (nb % i):
            nb_premier = False
       #   break
       # else:
            # Instruction(s) exécutée(s) seulement si la boucle n’est pas interrompue par l’instruction break
         #   nb_premier = True
    return nb_premier        
##################################################
nb = int(input(“Entrez un nombre à décomposer.”))


if (décomposition(nb)):
    print (“Une de ses décompositions en facteur(s) est : “, décomposition(nb)) 
