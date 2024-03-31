from Plateau import Plateau
from Mouvement import Mouvement
import copy
import random

#minimax
#alpha_beta
#montecarl
#glouton
#recherche heuristiques


#un noeud c'est le plateau les deux joueurs
#faut enumerer toutes les differentes combinaisons de cartes
#puis enumerer les coups possibles
#l'etat initial c'est le plateau avec cartes ( on a plusieurs etats initiaux)
#l'etat final soit la voieRuisseau soit voiePierre

#assigner des heuristiques aux differents etats
# une fonction eval

def eval(plateau,joueurMax):
    """
    Plateau x Joueur -> int
    """
    if joueurMax.getCouleur() == "Rouge":
        return plateau.getJoueurRouge().getScore() - plateau.getJoueurBleu().getScore()
    else : 
        return plateau.getJoueurBleu().getScore() - plateau.getJoueurRouge().getScore()
    
def minimax(plateau, profondeur, alpha, beta, joueurMax, joueurMin, joueurIA, listeMeilleursCoups, boolMax):
    """
    
    """
    # if profondeur == 0 or plateau.gameOver():
    print("-------------------------------plateauIA--------------------------------")
    print(plateau)
    print("----------------------------------------------------------------------------------")
    if plateau.gameOver() :
        print("gameOver")
        print("joueurGagnant",plateau.joueurGagnant())
        print("joueurMax ", joueurMax.getCouleur())
        print("pronfondeur",profondeur)
        if plateau.joueurGagnant() == joueurMax.getCouleur() :
            print("finnnnn1")
            return float('inf'), listeMeilleursCoups
        else : 
            print("finnnnn3")
            return -float('inf'), listeMeilleursCoups
    if profondeur <= 0 : 
        # nbPieceActuelles = len(joueurActif.getListePions())
        # redSensei = plateau.getJoueurRouge().getSensei()
        # blueSensei = plateau.getJoueurBleu().getSensei()

        # if joueurActif.getCouleur() == "Rouge" :
        #     nbPieceAdversaire = len(plateau.getJoueurBleu().getListePions())
        #     proximite_actuelle = ((redSensei.getPos()[0]-blueSensei.getPos()[0])*(redSensei.getPos()[0]-blueSensei.getPos()[0])) + ((redSensei.getPos()[1]-blueSensei.getPos()[1])*(redSensei.getPos()[1]-blueSensei.getPos()[1]))
        #     proximite_adversaire = ((blueSensei.getPos()[0]-redSensei.getPos()[0])*(blueSensei.getPos()[0]-redSensei.getPos()[0])) + ((blueSensei.getPos()[1]-redSensei.getPos()[1])*(blueSensei.getPos()[1]-redSensei.getPos()[1]))
        # else :
        #     nbPieceAdversaire = len(plateau.getJoueurRouge().getListePions())
        #     proximite_actuelle = ((blueSensei.getPos()[0]-redSensei.getPos()[0])*(blueSensei.getPos()[0]-redSensei.getPos()[0])) + ((blueSensei.getPos()[1]-redSensei.getPos()[1])*(blueSensei.getPos()[1]-redSensei.getPos()[1]))
        #     proximite_adversaire = ((redSensei.getPos()[0]-blueSensei.getPos()[0])*(redSensei.getPos()[0]-blueSensei.getPos()[0])) + ((redSensei.getPos()[1]-blueSensei.getPos()[1])*(redSensei.getPos()[1]-blueSensei.getPos()[1]))
        

        # return (nbPieceActuelles-proximite_actuelle) - (nbPieceAdversaire-proximite_adversaire), listeMeilleursCoups
        return eval(plateau, joueurMax), listeMeilleursCoups
    
    #meilleurCoup = None

    if boolMax :
        bestValue = -float('inf')
        listeCartes = joueurMax.getCartes()
        listePions = joueurMax.getListePions()
        for carte in listeCartes :
            for piece in listePions :
                mouvements = carte.getMouvs()
                for move in mouvements :
                    child = copy.deepcopy(plateau)
                    player = copy.deepcopy(joueurMax)
                    depart = piece.getPos()
                    arrive = Mouvement.pionAutorise(child,piece,move)
                    coup = (piece.getPos()[0] + move[0], piece.getPos()[1] + move[1])
 
                    if arrive == True : 
                        Mouvement.deplacer(child,piece,coup)
                        child.echange(player,carte)
                        print("La carte a ete supprime avec succes")
                        MeilleursCoups = [piece,carte,coup]
                        
                        retVal, listeMeilleursCoups = minimax(child,profondeur-1,alpha,beta,joueurMax, joueurMin, joueurIA, listeMeilleursCoups, False)
                        piece.setPos(depart)

                        if retVal > bestValue :
                            listeMeilleursCoups = MeilleursCoups
                            bestValue = retVal
                        
                            # if alpha < retVal :
                            #     alpha = max(retVal,alpha)
                            #     listeMeilleursCoups = MeilleursCoups

                        print("alpha : ",alpha," beta : ",beta," retVal :",retVal,"coup :",listeMeilleursCoups)

        return bestValue, listeMeilleursCoups
                        
    
    else :
        bestValue = float('inf')
        listeCartes = joueurMin.getCartes()
        listePions = joueurMin.getListePions()
        for carte in listeCartes :
            for piece in listePions :
                mouvements = carte.getMouvs()
                for move in mouvements :
                    child = copy.deepcopy(plateau)
                    player = copy.deepcopy(joueurMin)
                    depart = piece.getPos()
                    arrive = Mouvement.pionAutorise(child,piece,move)
                    coup = (piece.getPos()[0] + move[0], piece.getPos()[1] + move[1])

                    if arrive == True : 
                        Mouvement.deplacer(child,piece,coup)
                        child.echange(player,carte)
                        print("La carte a ete supprime avec succes")
                        MeilleursCoups = [piece,carte,coup]
 
                        retVal, listeMeilleursCoups = minimax(child,profondeur-1,alpha,beta,joueurMax, joueurMin, joueurIA, listeMeilleursCoups, True)
                        piece.setPos(depart)
                        if bestValue > retVal :
                            bestValue = retVal
                            listeMeilleursCoups = MeilleursCoups
                        
                        print("alpha : ",alpha," beta : ",beta," retVal :",retVal,"coup :",listeMeilleursCoups)
                        

        print("finnnnn5")
        return bestValue, listeMeilleursCoups
                        
                    
    # if joueurActif == joueurMax :
    #     print("finnnnn4")
    #     return alpha, listeMeilleursCoups
    # else : 
    #     print("finnnnn5")
    #     return beta, listeMeilleursCoups
    
#a finir et test
def alphabeta(plateau, profondeur, alpha, beta, joueurMax, joueurActif) :
    listeMeilleursCoups = []
    if plateau.gameOver() :
        if plateau.joueurGagnant() == joueurMax :
            return eval(plateau, joueurMax), listeMeilleursCoups
        else : 
            return -eval(plateau, joueurMax), listeMeilleursCoups
    if profondeur <= 0 : 
        # nbPieceActuelles = len(joueurActif.getListePions())
        # redSensei = plateau.getJoueurRouge().getSensei()
        # blueSensei = plateau.getJoueurBleu().getSensei()

        # if joueurActif.getCouleur() == "Rouge" :
        #     nbPieceAdversaire = len(plateau.getJoueurBleu().getListePions())
        #     proximite_actuelle = ((redSensei.getPos()[0]-blueSensei.getPos()[0])*(redSensei.getPos()[0]-blueSensei.getPos()[0])) + ((redSensei.getPos()[1]-blueSensei.getPos()[1])*(redSensei.getPos()[1]-blueSensei.getPos()[1]))
        #     proximite_adversaire = ((blueSensei.getPos()[0]-redSensei.getPos()[0])*(blueSensei.getPos()[0]-redSensei.getPos()[0])) + ((blueSensei.getPos()[1]-redSensei.getPos()[1])*(blueSensei.getPos()[1]-redSensei.getPos()[1]))
        # else :
        #     nbPieceAdversaire = len(plateau.getJoueurRouge().getListePions())
        #     proximite_actuelle = ((blueSensei.getPos()[0]-redSensei.getPos()[0])*(blueSensei.getPos()[0]-redSensei.getPos()[0])) + ((blueSensei.getPos()[1]-redSensei.getPos()[1])*(blueSensei.getPos()[1]-redSensei.getPos()[1]))
        #     proximite_adversaire = ((redSensei.getPos()[0]-blueSensei.getPos()[0])*(redSensei.getPos()[0]-blueSensei.getPos()[0])) + ((redSensei.getPos()[1]-blueSensei.getPos()[1])*(redSensei.getPos()[1]-blueSensei.getPos()[1]))
        

        # return (nbPieceActuelles-proximite_actuelle) - (nbPieceAdversaire-proximite_adversaire), None
        return eval(plateau, joueurMax), listeMeilleursCoups
    
    if joueurActif == joueurMax :
        val = eval(plateau, joueurMax)
        #meilleurCoup = None
        for carte in joueurActif.getCartes() :
            if carte == None : 
                continue
            for piece in joueurActif.getListePions() :
                if piece == None : 
                    continue

                mouvements = carte.getMouvs()
                for move in mouvements :
                    child = copy.deepcopy(plateau)
                    depart = piece.getPos()
                    arrive = Mouvement.pionAutorise(child,piece,move)
                    coup = (piece.getPos()[0] + move[0], piece.getPos()[1] + move[1])

                    if arrive == True : 
                        Mouvement.deplacer(child,piece,coup)
                        
                        if child.gameOver() and child.joueurGagnant() == joueurMax :
                            return float('inf'), [[piece,carte,coup]]

                        retVal, _ = alphabeta(child,profondeur-1,alpha,beta,joueurMax, joueurActif)
                        piece.setPos(depart)
                        
                        if val < retVal :
                            val = retVal
                            listeMeilleursCoups = [[piece,carte,coup]]
                            if alpha < val :
                                alpha = val
                                if beta <= alpha :
                                    return val#, meilleurCoup
                        elif val == retVal :
                            listeMeilleursCoups.append([piece,carte,coup])
                        #     meilleurCoup = [piece,carte,coup]
        return val, listeMeilleursCoups
    else :
        val = eval(plateau, joueurActif)
        # meilleurCoup = None
        for carte in joueurActif.getCartes() :
            if carte == None : 
                continue
            for piece in joueurActif.getListePions() :
                if piece == None : 
                    continue
                
                mouvements = carte.getMouvs()
                for move in mouvements :
                    child = copy.deepcopy(plateau)
                    depart = piece.getPos()
                    arrive = Mouvement.pionAutorise(child,piece,move)
                    coup = (piece.getPos()[0] + move[0], piece.getPos()[1] + move[1])

                    if arrive == True :
                        Mouvement.deplacer(child,piece,coup)

                        retVal, _ = alphabeta(child,profondeur-1,alpha,beta,joueurMax, joueurActif)
                        piece.setPos(depart)

                        if val > retVal :
                            val = retVal
                            listeMeilleursCoups = [[piece,carte,coup]]
                            if beta > val :
                                beta = val
                                if beta <= alpha :
                                    return val#, meilleurCoup
                        elif val == retVal :
                            listeMeilleursCoups.append([piece,carte,coup])
                print("alpha : ",alpha," beta : ",beta," retVal :",retVal)
        return val, listeMeilleursCoups#, meilleurCoup

def meilleur_coup_minimax(plateau,profondeur, joueurMax, joueurMin, joueurActif, boolIA) :
    val, meilleurCoup = minimax(plateau, profondeur, float('-inf'), float('inf'), joueurMax, joueurMin, joueurActif, [], boolIA)
    # print("alphabetaBis(plateau, profondeur, float('-inf'), float('inf'), joueurMax, joueurMin : ",alphabetaBis(plateau, profondeur, float('-inf'), float('inf'), joueurMax, joueurMin))
    # print("minimax(plateau, profondeur, float('-inf'), float('inf'), joueurMax, joueurMin, [])", val, meilleurCoup)
    print("meilleurCoup : ",meilleurCoup)
    print("couleur pion : ", meilleurCoup[0].getCouleur(), " carte : ", str(meilleurCoup[1]))
    #choix = random.randint(0,len(meilleurCoup))
    return meilleurCoup#[choix]

def meilleur_coup_alpha_beta(plateau,profondeur, joueurMax, joueurMin, joueurActif, boolIA) :
    val, meilleurCoup = minimax(plateau, profondeur, float('-inf'), float('inf'), joueurMax, joueurMin, joueurActif, [], boolIA)
    # print("alphabetaBis(plateau, profondeur, float('-inf'), float('inf'), joueurMax, joueurMin : ",alphabetaBis(plateau, profondeur, float('-inf'), float('inf'), joueurMax, joueurMin))
    # print("minimax(plateau, profondeur, float('-inf'), float('inf'), joueurMax, joueurMin, [])", val, meilleurCoup)
    print("meilleurCoup : ",meilleurCoup)
    print("couleur pion : ", meilleurCoup[0].getCouleur(), " carte : ", str(meilleurCoup[1]))
    #choix = random.randint(0,len(meilleurCoup))
    return meilleurCoup#[choix]

def alphabetaBis(plateau, profondeur, alpha, beta, joueurMax, joueurActif, listeMeilleursCoups) :
    print("-------------------------------plateauIA--------------------------------")
    print(plateau)
    print("----------------------------------------------------------------------------------")
    if plateau.gameOver() :
        print("gameOver")
        print("joueurGagnant",plateau.joueurGagnant())
        print("joueurMax ", joueurMax.getCouleur())
        print("pronfondeur",profondeur)
        if plateau.joueurGagnant() == joueurMax.getCouleur() :
            print("finnnnn1")
            return float('inf'), listeMeilleursCoups
        else : 
            print("finnnnn3")
            return -float('inf'), listeMeilleursCoups
    if profondeur <= 0 : 
        # nbPieceActuelles = len(joueurActif.getListePions())
        # redSensei = plateau.getJoueurRouge().getSensei()
        # blueSensei = plateau.getJoueurBleu().getSensei()

        # if joueurActif.getCouleur() == "Rouge" :
        #     nbPieceAdversaire = len(plateau.getJoueurBleu().getListePions())
        #     proximite_actuelle = ((redSensei.getPos()[0]-blueSensei.getPos()[0])*(redSensei.getPos()[0]-blueSensei.getPos()[0])) + ((redSensei.getPos()[1]-blueSensei.getPos()[1])*(redSensei.getPos()[1]-blueSensei.getPos()[1]))
        #     proximite_adversaire = ((blueSensei.getPos()[0]-redSensei.getPos()[0])*(blueSensei.getPos()[0]-redSensei.getPos()[0])) + ((blueSensei.getPos()[1]-redSensei.getPos()[1])*(blueSensei.getPos()[1]-redSensei.getPos()[1]))
        # else :
        #     nbPieceAdversaire = len(plateau.getJoueurRouge().getListePions())
        #     proximite_actuelle = ((blueSensei.getPos()[0]-redSensei.getPos()[0])*(blueSensei.getPos()[0]-redSensei.getPos()[0])) + ((blueSensei.getPos()[1]-redSensei.getPos()[1])*(blueSensei.getPos()[1]-redSensei.getPos()[1]))
        #     proximite_adversaire = ((redSensei.getPos()[0]-blueSensei.getPos()[0])*(redSensei.getPos()[0]-blueSensei.getPos()[0])) + ((redSensei.getPos()[1]-blueSensei.getPos()[1])*(redSensei.getPos()[1]-blueSensei.getPos()[1]))
        

        # return (nbPieceActuelles-proximite_actuelle) - (nbPieceAdversaire-proximite_adversaire), listeMeilleursCoups
        return eval(plateau, joueurMax), listeMeilleursCoups
    
    #meilleurCoup = None
    listeCartes = joueurActif.getCartes()
    listePions = joueurActif.getListePions()

    for carte in listeCartes :
        print("carte : ",str(carte))
        for piece in listePions :
            mouvements = carte.getMouvs()
            for move in mouvements :
                child = copy.deepcopy(plateau)
                depart = piece.getPos()
                arrive = Mouvement.pionAutorise(child,piece,move)
                coup = (piece.getPos()[0] + move[0], piece.getPos()[1] + move[1])

                if arrive == True : 
                    Mouvement.deplacer(child,piece,coup)
                    
                    # if child.gameOver() and child.joueurGagnant() == joueurMax :
                    #     print("finnnnn2")
                    #     return float('inf'), [piece,carte,coup]
                    # elif child.gameOver() and child.joueurGagnant() != joueurMax:
                    #     print("finnnnn6")
                    #     return float('-inf'), [piece,carte,coup]


                    retVal, listeMeilleursCoups = alphabetaBis(child,profondeur-1,alpha,beta,joueurMax, joueurActif, listeMeilleursCoups)
                    piece.setPos(depart)
                    print("alpha : ",alpha," beta : ",beta," retVal :",retVal,"coup :",listeMeilleursCoups)
                    
                    if joueurActif == joueurMax and retVal > alpha :
                        alpha = max(alpha,retVal)
                        listeMeilleursCoups = [piece,carte,coup]
                        if beta <= alpha:
                            break
                    elif joueurActif != joueurMax and retVal < beta :
                        beta = min(beta,retVal)
                        listeMeilleursCoups = [piece,carte,coup]
                        if beta <= alpha :
                            break
                    
    if joueurActif == joueurMax :
        print("finnnnn4")
        return alpha, listeMeilleursCoups
    else : 
        print("finnnnn5")
        return beta, listeMeilleursCoups
                   