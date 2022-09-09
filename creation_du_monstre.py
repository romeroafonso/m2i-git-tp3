#!/usr/bin/env/python3
from generation_du_monstre import generation_du_monstre
def creation_du_monstre():
    nom_monstre=input('veuillez saisir le nom du monstre: ')
    monstre=generation_du_monstre()
    monstre.insert(0, nom_monstre)
    return(monstre)