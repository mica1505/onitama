class Mouvement : 

    def positionValide(pos):
        """
        """
        x = pos[0]
        y = pos[1]

        if((x>=0 and x<5) and (y>=0 and y<5)) :
            return True
        else :
            return False
    
    def couleurPion(piece): 
        """
        """
        if piece.getCouleur() == "Rouge" :
            return "r"
        else : 
            return  'b'
        
    def couleurSensei(piece):
        if piece.getCouleur() == "Rouge" :
            return "R"
        else : 
            return  'B'

    def senseiAdverse(piece):
        if Mouvement.couleurSensei(piece) == "B":
            return "R"
        else : 
            return "B" 
        
    def listeCoupsPossibles(plateau,deplacements,piece) :
        '''
        Retourne la liste des coups possibles pour une piece
        '''
        coups = []
        for deplacement in deplacements :
            if Mouvement.couleurPion(piece) == "b" or Mouvement.couleurSensei(piece) == "B" :
                x = piece.getPos()[0] + deplacement[0]*(-1)
                y = piece.getPos()[1] + deplacement[1]
            else :
                x = piece.getPos()[0] + deplacement[0]
                y = piece.getPos()[1] + deplacement[1]
            if Mouvement.positionValide((x,y)) and (plateau.getGrille()[x][y] == "." and (plateau.getGrille()[x][y]!=Mouvement.couleurPion(piece) or plateau.getGrille()[x][y]!=Mouvement.couleurSensei(piece))) :
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

        
    def deplacer(plateau,piece,coup) : 
        """
        """

        temp = piece.getPos()
        symbole = plateau.getGrille()[temp[0]][temp[1]]

        if plateau.getGrille()[coup[0]][coup[1]] == Mouvement.senseiAdverse(piece):
            if Mouvement.senseiAdverse(piece) == "B":
                plateau.captureSenseiBleu()
            else : 
                plateau.captureSenseiRouge()

        plateau.getGrille()[coup[0]][coup[1]]=symbole
        piece.setPos(coup)
        plateau.getGrille()[temp[0]][temp[1]]="."



    
