#!/usr/bin/env python3

# Code pour compter les ennemies tués
from gestion_des_dégâts import gestion_des_degats as gd
def compteur(pv_perso, compteur_victoires):
    compteur_victoires = 0
    if pv_perso > 0:
        compteur_victoires += 1
        print(compteur_victoires)
    return(compteur_victoires)
