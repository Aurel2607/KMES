# Programme testant si une année, saisie par l'utilisateur,
# est bissextile ou non

annee = input("Saisissez une année : ") # On attend que l'utilisateur saisisse l'annee qu'il desire tester
annee = int(annee)  # Risque d'erreur si l'utilisateur n'a pas saisi un nombre
bissextile = False  # On cree un booleen qui vaut vrai ou faux
                    # selon que l'annee est bissextile ou non

if annee % 400 == 0:
    bissextile = True
elif annee % 100 == 0:
    bissextile = False
elif annee % 4 == 0:
    bissextile = True
else:
    bissextile = False

if bissextile: # Si l'annee est bissextile
    print("L'annee saisie est bissextile.")
else:
    print("L'annee saisie n'est pas bissextile.")
    