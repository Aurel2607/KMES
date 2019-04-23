
chaine = "Bonjour les ZER0S"
for lettre in chaine:
    if lettre in "AEIOUYaeiouy": # lettre est une voyelle
        print("vo: ", lettre)
    else:
        if lettre in "0123456789": # lettre est un chiffre
            print("ch: ", lettre)
        else: # lettre est une consonne... ou plus exactement, lettre n'est pas une voyelle
            print("co: ", lettre)
        