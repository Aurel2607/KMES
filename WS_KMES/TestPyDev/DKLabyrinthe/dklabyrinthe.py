'''
Created on 25 avr. 2019

@author: apajadon

Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
'''

import pygame
from pygame.locals import *
import constantes
import classes

def manageMenu():
    print("manageMenu")
    

def manageGame():
    print("manageGame")
    


#Initialisation de la bibliothèque Pygame
pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((constantes.cote_fenetre, constantes.cote_fenetre))

# Icone
icone = pygame.image.load(constantes.image_icone)
pygame.display.set_icon(icone)

# Titre
pygame.display.set_caption(constantes.titre_fenetre)

#Chargement et collage du fond
fondMenu = pygame.image.load("res/accueil.png").convert()
fenetre.blit(fondMenu, (0,0))

#Limitation de vitesse de la boucle à 30 frames par secondes
pygame.time.Clock().tick(30)

# Boucle Principale
mainRunning = True
menuRunning = True
gameRunning = False
while(mainRunning == True):
    for event in pygame.event.get():    #On parcours la liste de tous les événements reçus
 
        if event.type == QUIT:          #Si un de ces événements est de type QUIT
            mainRunning = 0         #On arrête la boucle

    
    # Boucle de Menu
    if(menuRunning == True):
        gameRunning = False
        manageMenu()
    
    # Boucle de jeu
    if(gameRunning == True):
        menuRunning = False
        manageGame()




