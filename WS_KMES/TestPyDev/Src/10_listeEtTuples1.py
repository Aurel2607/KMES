'''
Created on 25 avr. 2019

@author: apajadon
'''

def convertToFlottant(flottant):
    """ Fonction prenant en paramètre un flottant et renvoyant une chaîne de caractères représentant la troncature de ce nombre.
    La partie flottante doit avoir une longueur maximum de 3 caractères.

    De plus, on va remplacer le point décimal par la virgule"""
    if type(flottant) != float:
        raise TypeError("Le paramètre attendu doit être un flottant")
    flottant = str(flottant)
    partie_entiere, partie_flottante = flottant.split(".")
    
    # La partie entière n'est pas à modifier
    #Seule la partie flottante doit être tronquée.
    return ",".join([partie_entiere, partie_flottante[:3]])
    
def fonction_inconnue(*parametres):
    """Test d'une fonction pouvant être appelée avec un nombre variable de paramètres"""
    print("J'ai reçu : {}.".format(parametres))


if __name__ == '__main__':
    print(convertToFlottant(3.99999999999))
    fonction_inconnue() # On appelle la fonction sans paramètre
    fonction_inconnue(33)
    fonction_inconnue('a', 'e', 'f')
    var = 3.5
    fonction_inconnue(var, [4], "...")
    
    