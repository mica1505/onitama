class Joueur :
    def __init__(self, cartes, couleur, ia, difficulte) :
        '''
        
        '''
        self.cartes : list = cartes
        self.pions=[] #on les passe depuis le plateau au lancement du jeu
        self.couleur=couleur
        self.ia=ia
        self.score = self.somVal()
        if ia == True :
            self.difficulte=difficulte

    def getCartes(self) :
        return self.cartes
    
    def setCarte(self, carte):
        self.cartes.append(carte)

    def removeCarte(self, carte) :
        self.cartes.remove(carte)

    def getPions(self) :
        return self.pions

    def setPions(self,pion) :
        self.pions.append(pion)

    def getScore(self):
        return self.score

    def removePion(self,pion) : 
        self.pions.remove(pion)

    def somVal(self):
        res=0
        for p in self.pions:
            res+=p.getValeur()
        return res
    
    def getPion(self,pos):
        for p in self.pions:
            if p.getPos() == pos:
                return p
    
    def supPion(self,pos):
        p = self.getPion(pos)
        if p != None :
            self.pions.remove(p)