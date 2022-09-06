#!/usr/bin/env/python3

# Ici que le jeu se passe.


# import os pour nettoyer l'écran et les modules du jeu
import os
from creation_du_presonnage import creation_du_personnage as cp
from compteur_ennemis_tues import compteur
from gestion_des_dégâts import gestion_des_degats as gd

os.system('cls')

# D'abord créons notre personnage
personnage = cp()
print(f""" 
Salut {personnage[0]}, vous avez {personnage[1]} PV, {personnage[2]} de force et {personnage[3]} d'armure
""")

# commencer les combats, un compteur pour les victoires
liste_monstres_tues=[]
compteur_victoires=0
while True:
    # resultat du combat importe le resultat du module gestion des dégats
    resultat_combat = gd(personnage)
    # compteur_vistoire importe le résultat du moducle compteur d'énemis tués
    compteur_victoires+=compteur(resultat_combat[0])    
    if resultat_combat[0] <= 0:
        break
    else:
        liste_monstres_tues.append(resultat_combat[2])

print("Tu est mort! Mais tu as amené avec toi {} monstres: {} ".format(compteur_victoires, liste_monstres_tues))