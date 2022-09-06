#!/usr/bin/env/python3

from creation_du_monstre import creation_du_monstre as monstre

def gestion_des_degats(personnage):
    pers_count=personnage
    monstre_count=monstre()
    i=0
    print("Le combat commence !")
    while pers_count[1] > 0 and monstre_count[1] > 0:
        if pers_count[2] > monstre_count[3]:
            print(pers_count[0]+' attaque.')
            monstre_count[1]+=monstre_count[3] - pers_count[2]
        if monstre_count[2] > pers_count[3]:   
            print(monstre_count[0]+" attaque ! préparez vous !")
            pers_count[1]+=pers_count[3] - monstre_count[2]
        i+=1
        print(f"""{i} round : {pers_count[0]} a {pers_count[1]} de vie et {monstre_count[0]} a {monstre_count[1]} de vie.""")
    return(pers_count[1], monstre_count[1],monstre_count[0])        