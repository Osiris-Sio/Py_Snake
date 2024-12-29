# -*- coding: utf-8 -*-

'''
-> classe snake!

Auteurs : AMEDRO Louis / CAPPONI DELY Arthur
'''
####################################################################
### Importation :
####################################################################

import pyxel, module_lineaire, classe_pomme

####################################################################
# Code :
####################################################################

class Snake():
    '''
    On crée une classe Snake.
    '''
    
    def __init__(self) :
        '''
        Auteur : AMEDRO Louis / CAPPONI DELY Arthur
        Initialise le Snake.
        '''
        
        #Coordonnées de la tête du Snake :
        self.x = 24
        self.y = 32
        
        #Direction du Snake :
        self.dx = 8
        self.dy = 0
        
        #Le nombre d'anneau en plus qui seront ajoutés au Sanke :
        self.grandir = 0
        
        #La partie est perdu ?:
        self.perdu = False
        
        #Score du joueur :
        self.score = 0
        
        #File vide pour le corps du Snake :
        self.anneaux = module_lineaire.File()
        self.anneaux.enfiler((self.x - 16, self.y))
        self.anneaux.enfiler((self.x - 8, self.y))
        self.anneaux.enfiler((self.x, self.y))
        
        
    ######################################################
    ### Accesseurs :
    ######################################################
    
    def acc_x(self):
        '''
        Auteur : CAPPONI DELY Arthur
        Renvoie l'attribut x.
        : return (int)
        '''
        return self.x
    
    def acc_y(self):
        '''
        Auteur : CAPPONI DELY Arthur
        Renvoie l'attribut y.
        : return (int)
        '''
        return self.y
        
    def acc_dx(self):
        '''
        Auteur : AMEDRO Louis
        Renvoie l'attribut dx.
        : return (int), soit 8, -8 ou 0
        '''
        return self.dx
    
    def acc_score(self):
        '''
        Auteur : CAPPONI DELY Arthur
        Renvoie l'attribut score.
        : return (int)
        '''
        return self.score
        
    def acc_dy(self):
        '''
        Auteur : CAPPONI DELY Arthur
        Renvoie l'attribut dy.
        : return (int), soit 8, -8 ou 0
        '''
        return self.dy
        
    def acc_grandir(self):
        '''
        Auteur : AMEDRO Louis
        Renvoie l'attribut grandir.
        : return (int), soit 8, -8 ou 0
        '''
        return self.grandir
    
    def acc_perdu(self):
        '''
        Auteur : AMEDRO Louis
        Renvoie l'attribut perdu.
        : return (int)
        '''
        return self.perdu    
    
    ######################################################
    ### Mutateurs :
    ######################################################
    
    def mut_x(self, valeur):
        '''
        Auteur : AMEDRO Louis
        Modifie l'attribut x par la valeur passé en paramètre.
        : param valeur (int), doit être un multiple de 8
        : Pas de return, self est modifié par effet de bord.
        '''
        #Précondition :
        assert isinstance(valeur, int) and valeur % 8 == 0, 'Le paramètre doit être un entier (int) et un multiple de 8' 
        #Code :
        self.x = valeur
        
    def mut_y(self, valeur):
        '''
        Auteur : AMEDRO Louis
        Modifie l'attribut y par la valeur passé en paramètre.
        : param valeur (int), doit être un multiple de 8
        : Pas de return, self est modifié par effet de bord.
        '''
        #Précondition :
        assert isinstance(valeur, int) and valeur % 8 == 0, 'Le paramètre doit être un entier (int) et un multiple de 8' 
        #Code :
        self.y = valeur
       
    def mut_score(self, valeur):
        '''
        Auteur : CAPPONI DELY Arthur
        Modifie l'attribut score par la valeur passé en paramètre.
        : param valeur (int)
        : Pas de return, self est modifié par effet de bord.
        '''
        #Précondition :
        assert isinstance(valeur, int) 
        #Code :
        self.score = valeur
        
    def mut_dx(self, valeur):
        '''
        Auteur : AMEDRO Louis
        Modifie l'attribut dx par la valeur passé en paramètre.
        : param valeur (int), doit être égal à -8, 0 ou 8
        : Pas de return, self est modifié par effet de bord.
        '''
        #Précondition :
        assert isinstance(valeur, int) and valeur in [-8, 0, 8], 'Le paramètre doit être un entier (int) et égal à -8, 0 ou 8' 
        #Code :
        self.dx = valeur
        
    def mut_dy(self, valeur):
        '''
        Auteur : CAPPONI DELY Arthur
        Modifie l'attribut dy par la valeur passé en paramètre.
        : param valeur (int), doit être égal à -8, 0 ou 8
        : Pas de return, self est modifié par effet de bord.
        '''
        #Précondition :
        assert isinstance(valeur, int) and valeur in [-8, 0, 8], 'Le paramètre doit être un entier (int) et égal à -8, 0 ou 8' 
        #Code :
        self.dy = valeur
       
    def mut_grandir(self, valeur):
        '''
        Auteur : AMEDRO Louis
        Modifie l'attribut grandir par la valeur passé en paramètre.
        : param valeur (int)
        : Pas de return, self est modifié par effet de bord.
        '''
        #Précondition :
        assert isinstance(valeur, int), 'Le paramètre doit être un entier (int)' 
        #Code :
        self.grandir = valeur
        
    def mut_perdu(self, valeur):
        '''
        Auteur : AMEDRO Louis
        Modifie l'attribut perdu par la valeur passé en paramètre.
        : param valeur (boolean) True ou False
        : return (int)
        '''
        #Précondition :
        assert isinstance(valeur, bool), 'Le paramètre doit être un boolean (True ou False)'
        #Code :
        self.perdu = valeur
        
    ######################################################
    ### Affichage :
    ######################################################
        
    def afficher(self):
        '''
        Auteur : AMEDRO Louis
        Affiche les anneaux du Snake (sans effet de bord sur la pile) et le score
        en haut à gauche de l'écran
        : pas de return, afficher avec l'interface du module pyxel.
        '''
        stock = module_lineaire.File() #Creer une file vide (le stock)
        while not self.anneaux.est_vide() : #Tant que la file d'anneaux n'est pas vide :
            valeur = self.anneaux.defiler() #valeur est l'anneau défilé de la file d'anneaux
            stock.enfiler(valeur) #valeur (l'anneau) est stocké dans le stock
            if self.anneaux.est_vide() : #Si la file d'anneaux est vide :
                dic_tete = {
                    (8, 0) : 8,
                    (-8, 0) : 16,
                    (0, -8) : 24,
                    (0, 8) : 32
                } #Dictionnaire par chaque sprite de direction pour la tête du serpent
                
                #pyxel.blt(x_ecran, y_ecran, n° image, x_image, y_image, longueur, hauteur, noir (rien))
                pyxel.blt(valeur[0], valeur[1], 0, dic_tete[(self.acc_dx(), self.acc_dy())], 0, 8, 8, 0) #affiche la queue de la file / la tête du snake
            else : #Sinon (si la file d'anneau n'est pas vide)
                pyxel.blt(valeur[0], valeur[1], 0, 0, 0, 8, 8, 0) #Affiche un anneau
                
        #Replace chaque anneaux stocké dans la file stock dans la file d'anneaux tant que cette dernière n'est pas vide.
        while not stock.est_vide() :
            self.anneaux.enfiler(stock.defiler())
        
        #Afficher Score :
        pyxel.text(10, 10, 'Score : ' + str(self.score), 7)

        
    ######################################################
    ### Autres :
    ######################################################
        
    def deplacer(self):
        '''
        Auteur : CAPPONI DELY Arthur
        Modifie les attributs x et y en leur ajoutant respectivement dx et dy,
        on ajoute le couple de coordonnées (x, y) aux anneaux.
        Si la valeur de grandir vaut 0 alors on defile un anneau du snake 
        sinon la valeur de grandir diminue de 1.
        : pas de return, self est modifié par effet de bord.
        >>> s = Snake()
        >>> s.acc_x()
        24
        >>> s.acc_y()
        32
        >>> s.deplacer()
        >>> s.acc_x()
        32
        >>> s.acc_y()
        32
        >>> s.mut_dx(0)
        >>> s.mut_dy(8)
        >>> s.deplacer()
        >>> s.acc_x()
        32
        >>> s.acc_y()
        40
        '''
        self.mut_x(self.acc_x() + self.acc_dx()) # Modifie la coordonnée x du snake.
        self.mut_y(self.acc_y() + self.acc_dy()) # Modifie la coordonnée y du snake.
        self.anneaux.enfiler((self.acc_x(), self.acc_y())) # Enfile les nouvelles coordonnées de la nouvelle tête du snake.
        
        if self.grandir == 0 : # Si la valeur de grandir est égale à 0.
            self.anneaux.defiler() # Défile l'anneau.
        else : # Sinon
            self.mut_grandir(self.acc_grandir() - 1) # Modifie la valeur de grandir en enlevant 1 à sa valeur.
            
    def mord_pomme(self):
        '''
        Auteur : CAPPONI DELY Arthur
        Renvoie True s'il y a une pomme devant le serpent, False sinon.
        '''
        return pyxel.pget(self.acc_x() + 4, self.acc_y() + 4) == 8 # Renvoie vrai si la tête du snake se trouve sur la pomme grâce à sa couleur en son milieu.
        
    def est_perdu(self):
        '''
        Auteur : AMEDRO Louis
        Modifie l'attribut perdu si le Snake se percute lui même ou 
        touche le bord de l'écran. perdu prend alors la valeur True. 
        A la fin de la méthode, la valeur de l'attribut perdu est renvoyé.
        : return (boolean), l'attribut perdu.
        '''
        #Si le serpent touche le bord de la fenêtre pygame :
        if not (0 <= self.acc_x() <= 256) or not (0 <= self.acc_y() <= 256) :
            self.mut_perdu(True) #La partie est perdu
            
        #Si le serpent se touche lui même (touche un anneau)
        if pyxel.pget(self.acc_x() + 4, self.acc_y() + 4) == 9 :
            self.mut_perdu(True) #La partie est perdu
        
        return self.acc_perdu() #Renvoie l'attribut perdu
        
    def fin_de_partie(self):
        '''
        Auteur : CAPPONI DELY Arthur
        Si la pile anneaux n'est pas vide, on lui enlève un anneau.
        : return (bool), True si le serpent est totalement vidé (si la file est vide), False sinon
        
        >>> snake = Snake()
        >>> snake.fin_de_partie()
        False
        >>> snake.fin_de_partie()
        False
        >>> snake.fin_de_partie()
        False
        >>> snake.fin_de_partie()
        True
        '''
        if not self.anneaux.est_vide() :
            self.anneaux.defiler()
            return False
        else :
            return True

        
######################################################
# Doctest :
######################################################
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = False)