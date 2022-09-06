#!/usr/bin/env/python3
from generation_du_monstre import generation_du_monstre
def creation_du_monstre():
    nom_monstre=input('veuillez saisir le nom du monstre: ')
    
    monstre=[nom_monstre]
#coucou
    monstre.append(generation_du_monstre())

print(creation_du_monstre())