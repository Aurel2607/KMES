'''
Created on 24 avr. 2019

@author: apajadon
'''

if __name__ == '__main__':
    annee = input("Entrez l'année: ")
    try: # On essaye de convertir l'année en entier
        annee = int(annee)
        if(annee <=0):
            raise ValueError("l'année est négative ou nulle")
    except ValueError:
        print("La valeur saisie est invalide (l'année est peut-être négative).")


# if __name__ == '__main__':
#     try:
#         assert(numerateur == 0)
#         resultat = numerateur / denominateur
#     except NameError as exception_retournee:
#         print("La variable numerateur ou denominateur n'a pas été définie. (", exception_retournee, ")", sep='')
#     except TypeError as exception_retournee:
#         print("La variable numerateur ou denominateur possède un type incompatible avec la division. (", exception_retournee, ")", sep='')
#     except ZeroDivisionError as exception_retournee:
#         print("La variable denominateur est égale à 0. (", exception_retournee, ")", sep='')        
#     except AssertionError as exception_retournee:
#         print("Assertion Error. (", exception_retournee, ")", sep='')        
#     else:
#         print("le résultat obtenu est", resultat)
        
        