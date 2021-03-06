import pygame
from pygame.locals import *

perso_deplacement = 5

#Initialisation de la bibliothèque Pygame
pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640,480))

#Chargement et collage du fond
fond = pygame.image.load("Res/background.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("Res/perso.png").convert_alpha()
# position_perso = perso.get_rect()
position_perso_x = 0
position_perso_y = 0
# fenetre.blit(perso, position_perso)
fenetre.blit(perso, (position_perso_x, position_perso_y))

#Rafraîchissement de l'écran
pygame.display.flip()

pygame.key.set_repeat(100, 20)

#Boucle infinie
continuer = 1
while continuer:
    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
 
        if event.type == QUIT:     #Si un de ces événements est de type QUIT
            continuer = 0      #On arrête la boucle

        if event.type == KEYDOWN:
            if event.key == K_DOWN:    #Si "flèche bas"
                position_perso_y += perso_deplacement #On descend le perso
            if event.key == K_UP:    #Si "flèche haut"
                position_perso_y -= perso_deplacement #On monte le perso
            if event.key == K_LEFT:    #Si "flèche gauche"
                position_perso_x -= perso_deplacement #On bouge le perso à gauche
            if event.key == K_RIGHT:    #Si "flèche droite"
                position_perso_x += perso_deplacement #On bouge le perso à droite

        # Si clique
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 3 and event.pos[1] < 100:    # Clique droit et bande de 100px en haut
                print("Zone Dangereuse!!")
            else :
                if event.button == 1:                       # Clique gauche
                    #On change les coordonnées du perso
                    position_perso_x = event.pos[0]
                    position_perso_y = event.pos[1]
                    print("evtX:", event.pos[0], " - evtY:", event.pos[1])

#         if event.type == MOUSEMOTION and event.buttons[0] == 1:
#             continuer = 0

        if event.type == MOUSEMOTION: #Si mouvement de souris
                #On change les coordonnées du perso
                position_perso_x = event.pos[0]
                position_perso_y = event.pos[1]
            
    #Re-collage
    fenetre.blit(fond, (0,0))    
    fenetre.blit(perso, (position_perso_x, position_perso_y))
    #Rafraichissement
    pygame.display.flip()
    
    