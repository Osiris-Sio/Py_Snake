# -*- coding: utf-8 -*-

'''
-> Classe pomme !

Auteurs : AMEDRO Louis / CAPPONI DELY Arthur
'''
####################################################################
### Importation :
####################################################################

import pyxel, random

####################################################################
### Code :
####################################################################

class Pomme():
    '''
    On crée une classe Pomme.
    '''
    
    def __init__(self) :
        '''
        Auteur : AMEDRO Louis / CAPPONI DELY Arthur
        Initialise une Pomme.
        '''
        self.x = 128
        self.y = 32
        self.valeur = 1
        
    ######################################################
    ### Accesseur :
    ######################################################    
        
    def acc_valeur(self):
        '''
        Auteur : CAPPONI DELY Arthur
        Renvoie la valeur de la pomme.
        '''
        return self.valeur
        
    ######################################################
    ### Mutateurs :
    ######################################################
    
    def mut_x(self, valeur):
        '''
        Auteur : AMEDRO Louis
        Modifie l'attribut x par la valeur passé en paramètre.
        : param valeur (int), doit être égal à -8, 0 ou 8
        : Pas de return, self est modifié par effet de bord.
        '''
        #Précondition :
        assert isinstance(valeur, int) and valeur % 8 == 0, 'Le paramètre doit être un entier (int) et multiple de 8 !' 
        #Code :
        self.x = valeur
    
    def mut_y(self, valeur):
        '''
        Auteur : AMEDRO Louis
        Modifie l'attribut y par la valeur passé en paramètre.
        : param valeur (int), doit être égal à -8, 0 ou 8
        : Pas de return, self est modifié par effet de bord.
        '''
        #Précondition :
        assert isinstance(valeur, int) and valeur % 8 == 0, 'Le paramètre doit être un entier (int) et multiple de 8 !' 
        #Code :
        self.y = valeur
    
    def mut_valeur(self, valeur):
        '''
        Auteur : CAPPONI DELY Arthur
        Modifie l'attribut valeur par la valeur passé en paramètre.
        : param valeur (int), 1 <= valeur <= 9
        : Pas de return, self est modifié par effet de bord.
        '''
        #Précondition :
        assert isinstance(valeur, int) and 1 <= valeur <= 9, "Le paramètre doit être un entier (int) compris dans l'intervalle [1, 9]"
        #Code :
        self.valeur = valeur
        
    ######################################################
    ### Afficher :
    ######################################################
    
    def afficher(self):
        '''
        Auteur : AMEDRO Louis
        Affiche la pomme et sa valeur dans la fenêtre pygame.
        '''
        #pyxel.blt(x_ecran, y_ecran, n° image, x_image, y_image, longueur, hauteur, noir (rien))
        pyxel.blt(self.x, self.y, 0, 0, 8, 8, 8, 0) #affiche le sprite de la pomme
        pyxel.text(self.x + 6, self.y, str(self.acc_valeur()), 7) #Affiche la valeur de la pomme en haut à droite de cette dernière.

    ######################################################
    ### Déplacer :
    ######################################################
    
    def deplacer(self):
        '''
        Auteur : CAPPONI DELY Arthur
        Place la pomme à de nouvelles coordonnées, de façon à ce qu'elle ne soit pas sur un anneau
        '''
        tab_multiple_huit = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248] # On crée un tableau avec tout les multiples de 8 entre 8 et 248.
        x = random.choice(tab_multiple_huit) # La coordonnée x est choisit au hasard dans le tableau de multiples de 8.
        y = random.choice(tab_multiple_huit) # La coordonnée y est choisit au hasard dans le tableau de multiples de 8.
        while pyxel.pget(x + 4, y + 4) in [9, 10] : # Tant que x et y ne sont pas dans 9 = Anneaux ; 10 = Tête
            x = random.choice(tab_multiple_huit) # La coordonnée x est choisit au hasard dans le tableau de multiples de 8.
            y = random.choice(tab_multiple_huit) # La coordonnée y est choisit au hasard dans le tableau de multiples de 8.
        self.mut_x(x) # Modifie la valeur de x par le nouveau x.
        self.mut_y(y) # Modifie la valeur de y par le nouveau y.
        self.mut_valeur(random.randint(1, 9)) # Modifie la valeur par un chiffre entre 2 et 9.

######################################################
# Doctest :
######################################################
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = False)