#!/usr/bin/env/python3

<<<<<<< HEAD
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
=======
from flask import Flask, render_template, request, send_file, redirect, url_for, Response, redirect
from lejeu.jeumain import jeu

app = Flask(__name__)

import sys
import os


@app.route('/', methods=['GET', 'POST'])
def menu():
    pseudo=None
    monstres=[]
    if request.form:
        pseudo=request.form["nom"]
        print(request.form["nom"])
        monstres=jeu(pseudo)
    return render_template("index.html", monstres=monstres, pseudo=pseudo, nbr_monstres=len(monstres))
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8001)

>>>>>>> master
