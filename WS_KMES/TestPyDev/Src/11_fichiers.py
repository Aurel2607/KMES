'''
Created on 26 avr. 2019

@author: apajadon
'''

import os

if __name__ == '__main__':
    print(os.getcwd())
    with open("fichierTest.txt", "r") as myFile:
        print(myFile)
        print(myFile.closed)
        fileContents = myFile.read()
        print(fileContents)
    print(myFile.closed)
    
    myFile2 = open("fichierTest2.txt", "a")
    print(myFile2)

    
    myFile2.write("test écriture dans le fichier\r")
    
    myFile2.close()

