
def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb
    de 1*nb à max*nb
    
    (max >= 0)"""
    i = 0 # Notre compteur ! L'auriez-vous oublié ?
    while i < max: # Tant que i est strictement inférieure à 10,
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1 # On incrémente i de 1 à chaque tour de boucle.
   
       
def fonc(a=1, b=2, c=3, d=4, e=5):
    print("a=", a, ", b=", b, ", c=", c, ", d=", d, ", e=", e, sep='')
       
def carre(valeur):
    return valeur * valeur


fonc()
fonc(4)
fonc(b=8, d=5)
fonc(b=35, c=48, a=4, e=9)
        
nbr = 3
print ("carré de", nbr, "=", carre(nbr))

# nbr = int(input("entrez la table: "))
nbr = 10
table(nbr)


# Fonction Lambda
nbr = 5
nbr2 = 1
f = lambda x: x * x
g = lambda x,y: x+2*y
print("lambda function: f(", nbr, ")=",f(nbr), sep='')
print("lambda function: g(", nbr, ",", nbr2, ")=",g(nbr, nbr2), sep='')

