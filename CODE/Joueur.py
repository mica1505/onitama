class Joueur :
    def __init__(self, cartes, couleur, difficulte) :
        '''
        Initialisation d'un joueur
        '''
        self.cartes : list = cartes
        self.pions=[] #on les passe depuis le plateau au lancement du jeu
        self.couleur=couleur
        self.score = self.somVal()
        self.difficulte=difficulte

    def getCartes(self) :
        """
        Retourne les cartes du joueur
        """
        return self.cartes
    
    def setCarte(self, carte):
        """
        Ajoute une carte a la liste de cartes du joueur
        """
        self.cartes.append(carte)

    def removeCarte(self, carteSupp) :
        """
        Supprime une carte de la liste de cartes du joueur
        """
        for carte in self.cartes :
            if carte == carteSupp:
                self.cartes.remove(carte)
                break

    def getListePions(self) :
        """
        Retourne la liste des pions du joueur
        """
        return self.pions

    def setListePions(self,pion) :
        """
        Ajoute un pion a la liste de pions du joueur
        """
        self.pions.append(pion)

    def getCouleur(self):
        """
        Retourne la couleur du joueur
        """
        return self.couleur

    def getScore(self):
        """
        Retourne le score du joueur
        """
        return self.score

    def removePion(self,pion) :
        """
        Supprime le pion de la liste de pions du joueur
        """ 
        self.pions.remove(pion)

    def somVal(self):
        """
        Retourne la somme des scores des pions
        """
        somme=0
        for p in self.pions:
            somme+=p.getValeur()
        return somme
    
    def getPion(self,pos):
        """
        Retourne un pion du joueur
        """
        for p in self.pions:
            if p.getPos() == pos:
                return p
    
    def supPion(self,pos):
        """
        Supprime un pion du joueur
        """
        p = self.getPion(pos)
        if p != None :
            self.pions.remove(p)

    def getSensei(self) :
        """
        Retourne le sensei du joueur
        """
        for p in self.pions :
            if p.getSensei():
                return p
            
    def getDifficulte(self):
        """
        Retourne la difficulte de l'ia
        """ 
        return self.difficulte