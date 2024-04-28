class Mouvement : 

    def positionValide(pos):
        """
        Vérifie que la position est sur le plateau
        """
        x = pos[0]
        y = pos[1]
        if((x>=0 and x<5) and (y>=0 and y<5)) :
            return True
        else :
            return False
    
    def couleurPion(piece): 
        """
        Retourne la couleur du pion
        """
        if piece.getCouleur() == "Rouge" :
            return "r"
        else : 
            return  'b'
        
    def couleurSensei(piece):
        """
        Retourne la couleur du sensei
        """
        if piece.getCouleur() == "Rouge" :
            return "R"
        else : 
            return  'B'

    def discipleAdverse(piece):
        """
        Retourne la couleur du disciple adverse
        """
        if Mouvement.couleurPion(piece) == "b":
            return "r"
        else : 
            return "b" 
        
    def senseiAdverse(piece):
        """
        Retourne la couleur du sensei adverse
        """
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
            if Mouvement.couleurPion(piece) == "b" or Mouvement.couleurSensei(piece) == "B" : #Verifie la couleur de la piece pour que les coordonnees des déplacements soient corrects sur les axes
                x = piece.getPos()[0] + deplacement[0]*(-1)
                y = piece.getPos()[1] + deplacement[1]
            else :
                x = piece.getPos()[0] + deplacement[0]
                y = piece.getPos()[1] + deplacement[1]
            

            if Mouvement.positionValide((x,y)) and plateau.getGrille()[x][y] == "." and (plateau.getGrille()[x][y]!=Mouvement.couleurPion(piece) or plateau.getGrille()[x][y]!=Mouvement.couleurSensei(piece)) : #Si la case est vide
                coups.append((x,y))
            elif Mouvement.positionValide((x,y)) and plateau.getGrille()[x][y] != "." and (plateau.getGrille()[x][y]==Mouvement.discipleAdverse(piece) or plateau.getGrille()[x][y]==Mouvement.senseiAdverse(piece)) and (plateau.getGrille()[x][y]!=Mouvement.couleurPion(piece) and plateau.getGrille()[x][y]!=Mouvement.couleurSensei(piece)) : #Si la case est occupe par une piece adverse
                coups.append((x,y))
        return coups
    
    def pionAutorise(plateau,pion,coup) :
        """
        Return True si le coup du pion est autorise sinon False
        """
        if Mouvement.couleurPion(pion) == "b" or Mouvement.couleurSensei(pion) == "B" : #Verifie la couleur de la piece pour que les coordonnees des déplacements soient corrects sur les axes
            x = pion.getPos()[0] + coup[0]*(-1)
            y = pion.getPos()[1] + coup[1]
        else :
            x = pion.getPos()[0] + coup[0]
            y = pion.getPos()[1] + coup[1]

        if Mouvement.positionValide((x,y)) and plateau.getGrille()[x][y] == "." and (plateau.getGrille()[x][y]!=Mouvement.couleurPion(pion) or plateau.getGrille()[x][y]!=Mouvement.couleurSensei(pion)) and (plateau.getGrille()[x][y]!=Mouvement.discipleAdverse(pion) or plateau.getGrille()[x][y]!=Mouvement.senseiAdverse(pion)) : #Si la case est vide 
            return True
        elif Mouvement.positionValide((x,y)) and plateau.getGrille()[x][y] != "." and (plateau.getGrille()[x][y]==Mouvement.discipleAdverse(pion) or plateau.getGrille()[x][y]==Mouvement.senseiAdverse(pion)) and (plateau.getGrille()[x][y]!=Mouvement.couleurPion(pion) and plateau.getGrille()[x][y]!=Mouvement.couleurSensei(pion)) : #Si la case est occupe par une piece adverse
            return True
        else : 
            return False
    
    def listePionsAutorises(plateau,pions,coups) :
        """
        on recupere tous les pions et on retourne les pions qui peuvent se deplacer
        si un coup est possible avec le pion, on ajoute le pion a la liste
        """
        pions_joue = []
        for p in pions :
            for coup in coups :
                if Mouvement.pionAutorise(plateau, p, coup) :
                    if p not in pions_joue :
                        pions_joue.append(p)

        return pions_joue
        
    def deplacer(plateau,piece,coup) : 
        """
        Deplace le pion en fonction du coup choisi
        """
        if plateau.getGrille()[coup[0]][coup[1]] == Mouvement.senseiAdverse(piece):
            if Mouvement.senseiAdverse(piece) == "B":
                plateau.captureSenseiBleu()
            else : 
                plateau.captureSenseiRouge()

        temp = piece.getPos() #position du pion a deplace
        symbole = plateau.getGrille()[temp[0]][temp[1]] #symbole du pion a deplace
        if symbole != "." : #si la case est occupee
            plateau.supPion(coup)

        plateau.getGrille()[coup[0]][coup[1]] = symbole #change le symbole sur la case a deplace
        piece.setPos(coup) #deplace le pion sur la case
        plateau.getGrille()[temp[0]][temp[1]] = "." #change la case precedente du pion en case vide

    def listeCoupsLegaux(plateau,joueur) :
            '''
            Retourne la liste des coups possibles du joueur
            '''
            coups = []
            listePions = joueur.getListePions()
            listeCartes = joueur.getCartes()
            for carte in listeCartes :
                for piece in listePions :
                    for deplacement in carte.getMouvs() :
                        if Mouvement.couleurPion(piece) == "b" or Mouvement.couleurSensei(piece) == "B" : #Verifie la couleur de la piece pour que les coordonnees des déplacements soient corrects sur les axes
                            x = piece.getPos()[0] + deplacement[0]*(-1)
                            y = piece.getPos()[1] + deplacement[1]
                        else :
                            x = piece.getPos()[0] + deplacement[0]
                            y = piece.getPos()[1] + deplacement[1]

                        if Mouvement.positionValide((x,y)) and plateau.getGrille()[x][y] == "." and (plateau.getGrille()[x][y]!=Mouvement.couleurPion(piece) or plateau.getGrille()[x][y]!=Mouvement.couleurSensei(piece)) : #Si la case est vide
                            coups.append(((piece),(x,y),carte))
                        elif Mouvement.positionValide((x,y)) and plateau.getGrille()[x][y] != "." and (plateau.getGrille()[x][y]==Mouvement.discipleAdverse(piece) or plateau.getGrille()[x][y]==Mouvement.senseiAdverse(piece)) and (plateau.getGrille()[x][y]!=Mouvement.couleurPion(piece) and plateau.getGrille()[x][y]!=Mouvement.couleurSensei(piece)) : #Si la case est occupe par une piece adverse
                            coups.append(((piece),(x,y),carte))
            return coups