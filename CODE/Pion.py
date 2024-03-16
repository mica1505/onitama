class Pion:
    def __init__(self, couleur, pos, sensei):
        """
        Iniatialise un pion
        """
        self.couleur = couleur #est toujours egale a la couleur du joueur
        self.pos = pos
        self.sensei=sensei #true si la piece est le sensei
        self.val = self.valeur()

    def getCouleur(self) :
        """
        Retourne la couleur de la piece
        """
        return self.couleur
    
    def getPos(self) :
        """
        Retourne la position de la piece
        """
        return self.pos

    def setPos(self,pos) :
        """
        Change la position de la piece
        """
        self.pos=pos

    def getSensei(self) :
        """
        Retourne True si la piece est le sensei
        """
        return self.sensei
    
    def getValeur(self):
        """
        Retourne le score de la piece
        """
        return self.val

    def valeur(self):
        """
        Initialise le score de la piece
        """
        if self.sensei:
            return 80
        else :
            return 20
        
    
