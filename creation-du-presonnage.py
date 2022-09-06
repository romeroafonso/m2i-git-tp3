#! /bin/python

# Code pour création des personnages

def creation_du_personnage():
    Pseudo = input (" \n Merci de saisir le pseudo: ")    
    PV = 100
    Force = 10
    Armure = 5
    # print (f'''Le personnage {Pseudo} a {PV} points de vie, {Force} de force et {Armure} point d'armure. \n''' )
    personnage = [Pseudo, PV, Force, Armure]    
    print(personnage)
    return (personnage)


