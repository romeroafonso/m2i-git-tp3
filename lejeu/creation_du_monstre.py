#!/usr/bin/env/python3
from .generation_du_monstre import generation_du_monstre
import random
def creation_du_monstre():
    nom_monstre=random.choice(["Poulet ", "Cheval ", "Cochon de lait ", "Castor ", "Pinguin ", "Morse "])+\
        random.choice(["enragé", "malevolent", "mutant", "radioactive", "le jour du grand TP final"])
    monstre=generation_du_monstre()
    monstre.insert(0, nom_monstre)
    return(monstre)