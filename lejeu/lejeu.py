#!/usr/bin/env/python3
# Ici que le jeu se passe.
# import os pour nettoyer l'écran et les modules du jeu
from .creation_du_personnage import creation_du_personnage as cp
from .compteur_ennemis_tues import compteur
from .gestion_des_dégâts import gestion_des_degats as gd

def jeu(pseudo):
    # D'abord créons notre personnage
    personnage = cp(pseudo)

    # commencer les combats, un compteur pour les victoires
    liste_monstres_tues=[]
    compteur_victoires=0
    resultat_combat=[1]
    while resultat_combat[0] > 0:
        # resultat du combat importe le resultat du module gestion des dégats
        resultat_combat = gd(personnage)
        # compteur_vistoire importe le résultat du moducle compteur d'énemis tués
        compteur_victoires+=compteur(resultat_combat[0])
        if resultat_combat[0] > 0:
            liste_monstres_tues.append(resultat_combat[2])
    return liste_monstres_tues

if __name__ == "__main__":
    print(jeu("michel"))