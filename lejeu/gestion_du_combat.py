#!/usr/bin/env/python3

from creation_du_personnage import creation_du_personnage as personnage
from creation_du_monstre import creation_du_monstre as monstre
from gestion_des_dégâts import gestion_des_degats as degats
from compteur_ennemis_tues import compteur_ennemis_tues as compteur_ennemis
def gestion_du_combat():
    perso_count=personnage[1]
    #tant que les points de vie du joueur est positif continuer.
    # 1) afficher les stats du personnage
    # 2) générer un nouveau monstre
    #lorsque les points de vis du joueur sont a 0 alors afficher game over et sortir de la boucle.
    monstre_count=monstre[1]
    while perso_count > 0:
        perso_count-= degats[0]
        monstre=[]
        print("vous continuer le combat voici vos point de vie restant : ")
        print(perso_count)
        print("voici votre nouveau monstre :")
        print(monstre)

print("vous avez perdu la partie veuillez créer un nouveau personnage.")
        #monstre_count-=degats[1]
        #print(perso_count, monstre_count)
        #compteur_ennemis 

        