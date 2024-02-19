class Pion:
    def __init__(self, couleur, pos, sensei):
        self.couleur = couleur #sera toujour egale a la couleur du joueur
        self.pos = pos
        self.sensei=sensei #true si la piece est le sensei

    def getPos(self) :
        return self.pos

    def setPos(self,pos) :
        self.pos=pos

    def getSensei(self) :
        return self.sensei
