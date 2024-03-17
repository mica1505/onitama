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
#l'etat initial c'est le plateau avec  cartes ( on a plusieurs etats initiaux)
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
    
def minimax(plateau, profondeur, alpha, beta, max):
    """
    
    """
    if profondeur == 0 or plateau.gameOver():
        return plateau
    
#a finir et test
def alphabeta(plateau, profondeur, alpha, beta, max) :
    if plateau.gameOver() :
        if plateau.joueurGagnant == "R" :
            return 100 + profondeur, None
        else : 
            return -(100 + profondeur), None
    
    if profondeur <= 0 : 
        # nbPieceActuelles = len(plateau.getJoueurRouge().getListePions())
        # nbPieceAdversaire = len(plateau.getJoueurBleu().getListePions())

        # redSensei = plateau.getJoueurRouge().getSensei()
        # blueSensei = plateau.getJoueurBleu().getSensei()

        # proximite_actuelle = ((redSensei.getPos()[0]-blueSensei.getPos()[0])*(redSensei.getPos()[0]-blueSensei.getPos()[0])) + ((redSensei.getPos()[1]-blueSensei.getPos()[1])*(redSensei.getPos()[1]-blueSensei.getPos()[1]))
        # proximité_adversaire = ((blueSensei.getPos()[0]-redSensei.getPos()[0])*(blueSensei.getPos()[0]-redSensei.getPos()[0])) + ((blueSensei.getPos()[1]-redSensei.getPos()[1])*(blueSensei.getPos()[1]-redSensei.getPos()[1]))

        # return (nbPieceActuelles-proximite_actuelle) - (nbPieceAdversaire-proximité_adversaire)
        return eval(plateau, plateau.getJoueurRouge() if max else plateau.getJoueurBleu()), None
    
    if max :
        val = float('-inf')
        for carte in plateau.getJoueurRouge().getCartes() :
            if carte == None : 
                continue
            for piece in plateau.getJoueurRouge().getListePions() :
                if piece == None : 
                    continue

                mouvements = carte.getMouvs()
                for move in mouvements :
                    child = copy.deepcopy(plateau)
                    depart = piece.getPos()
                    arrive = Mouvement.pionAutorise(child,piece,move)

                    if arrive == True : 
                        Mouvement.deplacer(child,piece,coup)

                        retVal, _ = alphabeta(child,profondeur-1,alpha,beta,False)

                        piece.setPos(depart)
                        meilleurCoup = [piece,carte,coup]
                        print("meilleurCOup dans max : ",meilleurCoup)
                        if val < retVal :
                            val = retVal
                            if alpha < val :
                                if profondeur == plateau.getJoueurRouge().getIa() :
                                    meilleurCoup = [piece,carte,coup]

                                alpha = val
                                if beta <= alpha :
                                    return val, meilleurCoup
                        elif val == retVal :
                            return val, meilleurCoup
        return val, meilleurCoup
    else :
        val = float('-inf')
        for carte in plateau.getJoueurBleu().getCartes() :
            if carte == None : 
                continue
            for piece in plateau.getJoueurBleu().getListePions() :
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

                        retVal, _ = alphabeta(child,profondeur-1,alpha,beta,True)

                        piece.setPos(depart)
                        meilleurCoup = [piece,carte,coup]
                        print("meilleurCOup dans min : ",piece.getPos(), coup)
                        if val > retVal :
                            val = retVal
                            if beta > val :
                                beta = val
                                if beta <= alpha :
                                    return val, meilleurCoup
        return val, meilleurCoup

def meilleur_coup_alpha_beta(plateau,profondeur, max) :
    val, meilleurCoup = alphabeta(plateau, profondeur, float('-inf'), float('inf'), max)
    print("meilleurCOup dans max : ",meilleurCoup)
    return  meilleurCoup