nb_txt = input("saisissez la table ") # On garde la variable contenant le nombre dont on veut la table de multiplication
nb = int(nb_txt)
i = 0 # C'est notre variable compteur que nous allons incrémenter dans la boucle

while i < 10: # Tant que i est strictement inférieure à 10
    print(i + 1, "*", nb, "=", (i + 1) * nb)
    i += 1 # On incrémente i de 1 à chaque tour de boucle
    