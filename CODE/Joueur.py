class Joueur :
    def __init__(self, cartes, pions, couleur, ia, difficulte) :
        '''
        
        '''
        self.cartes=cartes
        self.pions=pions #on les passe depuis le plateau au lancement du jeu
        self.couleur=couleur
        self.ia=ia
        if ia == True :
            self.difficulte=difficulte



