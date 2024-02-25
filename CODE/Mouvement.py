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

    def discipleAdverse(piece):
        if Mouvement.couleurPion(piece) == "B":
            return "r"
        else : 
            return "b" 
        
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
            elif Mouvement.positionValide((x,y)) and (plateau.getGrille()[x][y] != "." and ((plateau.getGrille()[x][y]==Mouvement.discipleAdverse(piece) or plateau.getGrille()[x][y]==Mouvement.senseiAdverse(piece)) 
                                                                                            and 
                                                                                            (plateau.getGrille()[x][y]!=Mouvement.couleurPion(piece) or plateau.getGrille()[x][y]!=Mouvement.couleurSensei(piece)))):
                coups.append((x,y))
        return coups
    
    def pionAutorise(plateau,pions,coups) :
        """
        on recupere tous les pions et on garde que ceux qu'on peut bouger
        si parmis les coups a jouer ya un coup valide on l'ajoute a la liste
        """
        res = []
        for p in pions :
            x=p.getPos()[0]
            y = p.getPos()[1]
            # print("x1 : ",x)
            # print("y1 : ",y)
            for c in coups :
            #     print("coups : ",coups)
            #     print("c : ", c)

                if Mouvement.positionValide((x+c[0],y+c[1])) and (plateau.getGrille()[x+c[0]][y+c[1]]!=Mouvement.couleurPion(p) or plateau.getGrille()[x+c[0]][y+c[1]]!=Mouvement.couleurSensei(p)) :
                    # print("x2 : ",x+c[0])
                    # print("y2 : ",y+c[1])
                    # print("couleur1 : ",Mouvement.couleurPion(p))
                    # print("couleur2 : ",Mouvement.couleurSensei(p))
                    if p.getPos() not in res:
                        res.append(p.getPos())
                        # print("res : ", res)
        return res

        
    def deplacer(plateau,piece,coup) : 
        """
        """
        if plateau.getGrille()[coup[0]][coup[1]] == Mouvement.senseiAdverse(piece):
            if Mouvement.senseiAdverse(piece) == "B":
                plateau.captureSenseiBleu()
            else : 
                plateau.captureSenseiRouge()

        temp = piece.getPos()
        symbole = plateau.getGrille()[temp[0]][temp[1]]
        if symbole != ".":
            plateau.supPion(coup) 
        plateau.getGrille()[coup[0]][coup[1]]=symbole
        piece.setPos(coup)
        plateau.getGrille()[temp[0]][temp[1]]="."



    
