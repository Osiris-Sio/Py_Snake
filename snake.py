# -*- coding: utf-8 -*-

'''
-> Snake !

Auteurs : AMEDRO Louis / CAPPONI DELY Arthur
'''
####################################################################
### Importations :
####################################################################

import classe_snake, classe_pomme, pyxel

class Jeu():
    '''
    On crée une classe Jeu.
    '''

    def __init__(self):
        '''
        Initialise le jeu du Snake.
        '''
        #Attributs Importations :
        self.snake = classe_snake.Snake() #Initialise la classe Snake
        self.pomme = classe_pomme.Pomme() #Initialise la classe Pomme
        
        #Attributs pour le jeu :
        self.menu = True
        self.partie_terminee = False
        self.vitesse_jeu = 10
        self.vitesse_passee = False
        self.dx_provisoire = self.snake.acc_dx()
        self.dy_provisoire = self.snake.acc_dy()

    ######################################################
    ### Accesseurs :
    ######################################################

    def acc_dx_provisoire(self):
        '''
        Auteur : AMEDRO Louis
        Renvoie l'attribut dx_provisoire.
        : return (int), soit 8, -8 ou 0
        '''
        return self.dx_provisoire
        
    def acc_dy_provisoire(self):
        '''
        Auteur : CAPPONI DELY Arthur
        Renvoie l'attribut dy_provisoire.
        : return (int), soit 8, -8 ou 0
        '''
        return self.dy_provisoire
    
    def acc_vitesse_jeu(self):
        '''
        Auteur : AMEDRO Louis
        Renvoie l'attribut vitesse_jeu .
        : return (int), 4 <= vitesse_jeu <= 10
        '''
        return self.vitesse_jeu
    
    def acc_vitesse_passee(self):
        '''
        Auteur : AMEDRO Louis
        Renvoie l'attribut vitesse_passee .
        : return (boolean)
        '''
        return self.vitesse_passee
    
    def acc_menu(self):
        '''
        Auteur : AMEDRO Louis
        Renvoie l'attribut menu.
        : return (bool)
        '''
        return self.menu
    
    def acc_partie_terminee(self):
        '''
        Auteur : AMEDRO Louis
        Renvoie l'attribut partie terminee.
        : return (bool)
        '''
        return self.partie_terminee

    ######################################################
    ### Mutateurs :
    ######################################################

    def mut_dx_provisoire(self, valeur):
        '''
        Auteur : AMEDRO Louis
        Modifie l'attribut dx_provisoire par la valeur passé en paramètre.
        : param valeur (int), doit être égal à -8, 0 ou 8
        : Pas de return, self est modifié par effet de bord.
        '''
        #Précondition :
        assert isinstance(valeur, int) and valeur in [-8, 0, 8], 'Le paramètre doit être un entier (int) et égal à -8, 0 ou 8' 
        #Code :
        self.dx_provisoire = valeur
        
    def mut_dy_provisoire(self, valeur):
        '''
        Auteur : CAPPONI DELY Arthur
        Modifie l'attribut dy_provisoire par la valeur passé en paramètre.
        : param valeur (int), doit être égal à -8, 0 ou 8
        : Pas de return, self est modifié par effet de bord.
        '''
        #Précondition :
        assert isinstance(valeur, int) and valeur in [-8, 0, 8], 'Le paramètre doit être un entier (int) et égal à -8, 0 ou 8' 
        #Code :
        self.dy_provisoire = valeur
        
    def mut_dx_dy(self):
        '''
        Auteur : AMEDRO Louis
        Modifie les attributs dx et dy par les valeurs des attributs dx_provisoire et dy_provisoire.
        : Pas de return, self est modifié par effet de bord.
        '''
        self.snake.mut_dx(self.acc_dx_provisoire())
        self.snake.mut_dy(self.acc_dy_provisoire())
        
    def mut_vitesse_jeu(self, valeur):
        '''
        Auteur : CAPPONI DELY Arthur
        Modifie l'attribut vitesse_jeu par la valeur passé en paramètre.
        : param valeur (int), 4 <= valeur <= 10
        : Pas de return, self est modifié par effet de bord.
        '''
        #Précondition :
        assert isinstance(valeur, int) and 4 <= valeur <= 10, 'Le paramètre doit être un entier (int) et 4 <= valeur <= 10' 
        #Code :
        self.vitesse_jeu = valeur
        
    def mut_vitesse_passee(self, valeur):
        '''
        Auteur : CAPPONI DELY Arthur
        Modifie l'attribut vitesse_passee par la valeur passé en paramètre.
        : param valeur (bool)
        : Pas de return, self est modifié par effet de bord.
        '''
        #Précondition :
        assert isinstance(valeur, bool), 'Le paramètre doit être un boolean (bool)' 
        #Code :
        self.vitesse_passee = valeur
        
    def mut_menu(self, valeur):
        '''
        Auteur : AMEDRO Louis
        Modifie l'attribut dx_provisoire par la valeur passé en paramètre.
        : param valeur (bool)
        : Pas de return, self est modifié par effet de bord.
        '''
        #Précondition :
        assert isinstance(valeur, bool), 'Le paramètre doit être un boolean (bool).' 
        #Code :
        self.menu = valeur
    
    def mut_partie_terminee(self, valeur):
        '''
        Auteur : CAPPONI DELY Arthur
        Modifie l'attribut partie terminee par la valeur passé en paramètre.
        : param valeur (bool)
        : Pas de return, self est modifié par effet de bord.
        '''
        #Précondition :
        assert isinstance(valeur, bool), 'Le paramètre doit être un boolean (bool)' 
        #Code :
        self.partie_terminee = valeur
    
    ####################################################################
    # Fonctions Calculer :
    ####################################################################

    def gerer_clavier_menu(self):
        '''
        Gestions du clavier.
        '''
        #Lancer jeu :
        if pyxel.btnr(pyxel.KEY_RETURN) :
            self.menu = False

    def gerer_clavier_jeu(self):
        '''
        Gestions du clavier.
        '''
        #Allez à droite :
        if pyxel.btnr(pyxel.KEY_RIGHT) and self.snake.acc_dx() != -8 :
            self.mut_dx_provisoire(8)
            self.mut_dy_provisoire(0)
            
        #Allez à gauche :
        if pyxel.btnr(pyxel.KEY_LEFT) and self.snake.acc_dx() != 8 :
            self.mut_dx_provisoire(-8)
            self.mut_dy_provisoire(0)
            
        #Allez en haut :
        if pyxel.btnr(pyxel.KEY_UP) and self.snake.acc_dy() != 8 :
            self.mut_dx_provisoire(0)
            self.mut_dy_provisoire(-8)
            
        #Allez en bas :
        if pyxel.btnr(pyxel.KEY_DOWN) and self.snake.acc_dy() != -8 :
            self.mut_dx_provisoire(0)
            self.mut_dy_provisoire(8)
            
        if self.snake.acc_perdu() and pyxel.btnr(pyxel.KEY_RETURN) :
            self.__init__()
            
    def deroulement_du_jeu(self):
        '''
        Auteur : AMEDRO Louis
        Gére le déroulement du jeu. C'est à dire le déplacement du serpent, si la partie est perdu,
        si le serpent mord la pomme, augmente le score par la valeur de la pomme, passe la vitesse et plus encore pour un
        bon déroulement du jeu.
        : pas de return
        '''
        #Si le nombre de frames passées est un multiple de l'attribut vitesse_jeu :
        if pyxel.frame_count % self.vitesse_jeu == 1 :
            self.mut_dx_dy() #Change définitivement les attributs dx et dy de la classe Snake
            
            #Si le jeu n'est pas perdu :
            if not self.snake.est_perdu() :
                self.snake.deplacer() #Déplace le serpent vers la direction souhaité (dx et dy)
                self.snake.est_perdu()
            
        #Si le serpent mord la pomme :
        if self.snake.mord_pomme() :
            self.snake.mut_score(self.snake.acc_score() + self.pomme.acc_valeur()) #Augmente le score par la valeur de la pomme
            self.mut_vitesse_passee(False) 
            self.snake.mut_grandir(self.snake.acc_grandir() + self.pomme.acc_valeur())
            self.pomme.deplacer()
            
        #Si la vitesse n'as pas été passé au dernier score, que le score est un multiple de 146 et que la vitesse du jeu (les frames) est supérieur à 4 : 
        if not self.acc_vitesse_passee() and self.snake.acc_score() % 146 == 0 and 4 < self.acc_vitesse_jeu():
            self.mut_vitesse_jeu(self.acc_vitesse_jeu() - 1) #Diminue la vitesse du jeu de 1
            self.mut_vitesse_passee(True) #La vitesse est donc passé à ce score précisément et redeviendra False à la prochaine augmentation du score
            
    def calculer(self):
        '''
        La partie dédiée aux calculs
        '''
        #Menu :
        if self.menu :
            self.gerer_clavier_menu() #Gestion des différents évenements du clavier pendant le menu
        
        #Jeu :
        else :
            self.gerer_clavier_jeu() #Gestion des différents évenements du clavier pendant le jeu
            
            #Si le jeu n'est pas perdu :
            if not self.snake.est_perdu() :
                self.deroulement_du_jeu()
                
            #Sinon (si la partie n'est pas perdu)
            else :
                
                #Animation de déroulement du serpent avant que la partie est terminée.
                if not self.acc_partie_terminee() and pyxel.frame_count % 2 == 1 :
                    self.mut_partie_terminee(self.snake.fin_de_partie())

                
    ####################################################################
    # Fonctions Afficher :
    ####################################################################
    
    def afficher_menu(self):
        '''
        Affiche le menu
        '''
        pyxel.text(115, 80, 'Snake', 7)
        pyxel.text(100, 175, 'Presse Entree', 7)
        
    def afficher_partie_terminee(self):
        '''
        Affiche la fin de la partie
        '''
        if self.snake.acc_score() >= 1000 :
            pyxel.text(112, 110, 'Felicitation !', 7)
        else :
            pyxel.text(100, 100, 'Partie Terminee', 7)
            pyxel.text(80, 110, 'Il te manque ' + str(1000 - self.snake.acc_score()) + ' points !', 7)
        pyxel.text(100, 175, 'Presse Entree', 7)
    

    def dessiner(self):
        '''
        la partie dédié aux graphismes
        '''
        pyxel.cls(0)
        
        #Si la partie n'est pas terminée :
        if not self.acc_partie_terminee() :
            self.snake.afficher()
            self.pomme.afficher()
            
            #Menu :
            if self.menu:
                self.afficher_menu()
            
        #Sinon, affiche que la partie est terminée :
        else :
            self.afficher_partie_terminee()


    ######################################################
    ### Jouer ! :
    ######################################################                                  

    def jouer(self):
        '''
        On lance le jeu
        '''
        pyxel.init(256, 256, 'Snake') #Initialise la fenêtre de jeu de dimension 256x256 et comme titre 'Snake'
        pyxel.load('ressources.pyxres')
        pyxel.run(self.calculer, self.dessiner)
        
#Lance automatiquement le jeu à l'éxécution du programme :
Jeu().jouer()