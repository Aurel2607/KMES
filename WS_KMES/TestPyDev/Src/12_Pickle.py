'''
Created on 26 avr. 2019

@author: apajadon
'''

import pickle
saveFileName = "12_Pickle2.bin"

if __name__ == '__main__':
    
    scoreInitial = {
        "joueur 1":    5,
        "joueur 2":   35,
        "joueur 3":   20,
        "joueur 4":    2,
    }
    
    #------------------------------
    #         Chargement
    #------------------------------
    try:
        with open(saveFileName, 'rb') as myFile:
            myUnPickler = pickle.Unpickler(myFile)
            
            # Lecture
            score_recuperer = myUnPickler.load()
    except OSError:
        # Le fichier n'existe pas
        score_recuperer = scoreInitial
        print("No file", saveFileName, "- Init...")
        
    # Display
    print(score_recuperer)
    
       
    #------------------------------
    #         Modification
    #------------------------------
    score_recuperer["joueur 1"] += 5
    score_recuperer["joueur 2"] += 1
    score_recuperer["joueur 3"] += 2
    score_recuperer["joueur 4"] += 4
        
    # Display
    print(score_recuperer)
    
    #------------------------------
    #         Sauvegarde
    #------------------------------
    with open(saveFileName, 'wb') as myFile:
        myPickler = pickle.Pickler(myFile)
        
        # Enregistrement
        myPickler.dump(score_recuperer)

        
        