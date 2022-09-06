#!/usr/bin/env/python3
from generation-du-monstre.py import generation_du_monste
def creation_du_monstre():
    nom_monstre=input('veuillez saisir le nom du monstre: ')
    
    monstre=[nom_monstre]

    monstre.append(generation_du_monstre())

print(creation_du_monstre())