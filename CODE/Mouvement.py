class Mouvement : 
    def __init__(self, plateau, piece, deplacements) :
        self.plateau = plateau
        self.piece=piece
        self.deplacements=deplacements

    def positionValide(pos):
        """
        """
        x = pos[0]
        y = pos[1]

        if((x>=0 and x<5) and (y>=0 and y<5)) :
            return True
        else :
            return False
    
    def couleurPion(self): 
        """
        """
        if self.piece.getCouleur() == "Rouge" :
            return "r"
        else : 
            return  'b'
        
    def couleurSensei(self):
        if self.piece.getCouleur() == "Rouge" :
            return "R"
        else : 
            return  'B'

    def senseiAdverse(self):
        if self.couleurSensei() == "B":
            return "R"
        else : 
            return "B" 
    def listeCoupsPossibles(self) :
        '''
        Retourne la liste des coups possibles pour une piece
        '''
        coups = []
        for deplacement in self.deplacements :
            if self.couleurPion() == "b" or self.couleurSensei() == "B" :
                x = self.piece.getPos()[0] + deplacement[0]*(-1)
                y = self.piece.getPos()[1] + deplacement[1]
            else :
                x = self.piece.getPos()[0] + deplacement[0]
                y = self.piece.getPos()[1] + deplacement[1]
            if Mouvement.positionValide((x,y)) and (self.plateau.getGrille()[x][y] == "." and (self.plateau.getGrille()[x][y]!=self.couleurPion() or self.plateau.getGrille()[x][y]!=self.couleurSensei())) :
                coups.append((x,y))
        return coups
    
    def pionAutorise(pions,coups) :
        """
        on recupere tous les pions et on garde que ceux qu'on peut bouger
        si parmis les coups a jouer ya un coup valide on l'ajoute a la liste
        """
        res = []
        for p in pions :
            x=p.getPos()[0]
            y = p.getPos()[1]
            for c in coups :
                if Mouvement.positionValide((x+c[0],y+c[1])):
                    if p.getPos() not in res:
                        res.append(p.getPos())
        return res

        
    def deplacer(self, coup) : 
        """
        """

        temp = self.piece.getPos()
        symbole = self.plateau.getGrille()[temp[0]][temp[1]]
        
        if self.plateau.getGrille()[coup[0]][coup[1]] == self.senseiAdverse():
            if self.senseiAdverse() == "B":
                self.plateau.captureSenseiBleu()
            else : 
                self.plateau.captureSenseiRouge()

        self.plateau.getGrille()[coup[0]][coup[1]]=symbole
        self.piece.setPos(coup)
        self.plateau.getGrille()[temp[0]][temp[1]]="."



    
