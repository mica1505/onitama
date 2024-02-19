class Joueur :
    def __init__(self, cartes, pions, couleur, ia, difficulte) :
        self.cartes=cartes
        self.pions=pions
        self.couleur=couleur
        self.ia=ia
        if ia == True :
            self.difficulte=difficulte



