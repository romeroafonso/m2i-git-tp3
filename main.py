#!/usr/bin/env/python3
from flask import Flask, render_template, request, send_file, redirect, url_for, Response, redirect
from lejeu.lejeu import jeu

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
    # app.run(debug=True, host='0.0.0.0', port=8001)
    print(jeu("Avant"))