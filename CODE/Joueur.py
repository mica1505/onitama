class Joueur :
    def __init__(self, cartes, couleur, ia, difficulte) :
        '''
        
        '''
        self.cartes = cartes
        self.pions=[] #on les passe depuis le plateau au lancement du jeu
        self.couleur=couleur
        self.ia=ia
        if ia == True :
            self.difficulte=difficulte

    def getCartes(self) :
        return self.cartes

    def getPions(self) :
        return self.pions

    def setPions(self,pion) :
        self.pions.append(pion)