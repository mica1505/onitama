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
def alphabeta(plateau, profondeur, alpha, beta, joueurMax, joueurActif) :
    listeMeilleursCoups = []
    if plateau.gameOver() :
        if plateau.joueurGagnant == "R" :
            return 100 + profondeur
        else : 
            return -(100 + profondeur),
    
    if profondeur <= 0 : 
        nbPieceActuelles = len(joueurActif.getListePions())
        redSensei = plateau.getJoueurRouge().getSensei()
        blueSensei = plateau.getJoueurBleu().getSensei()

        if joueurActif.getCouleur() == "Rouge" :
            nbPieceAdversaire = len(plateau.getJoueurBleu().getListePions())
            proximite_actuelle = ((redSensei.getPos()[0]-blueSensei.getPos()[0])*(redSensei.getPos()[0]-blueSensei.getPos()[0])) + ((redSensei.getPos()[1]-blueSensei.getPos()[1])*(redSensei.getPos()[1]-blueSensei.getPos()[1]))
            proximite_adversaire = ((blueSensei.getPos()[0]-redSensei.getPos()[0])*(blueSensei.getPos()[0]-redSensei.getPos()[0])) + ((blueSensei.getPos()[1]-redSensei.getPos()[1])*(blueSensei.getPos()[1]-redSensei.getPos()[1]))
        else :
            nbPieceAdversaire = len(plateau.getJoueurRouge().getListePions())
            proximite_actuelle = ((blueSensei.getPos()[0]-redSensei.getPos()[0])*(blueSensei.getPos()[0]-redSensei.getPos()[0])) + ((blueSensei.getPos()[1]-redSensei.getPos()[1])*(blueSensei.getPos()[1]-redSensei.getPos()[1]))
            proximite_adversaire = ((redSensei.getPos()[0]-blueSensei.getPos()[0])*(redSensei.getPos()[0]-blueSensei.getPos()[0])) + ((redSensei.getPos()[1]-blueSensei.getPos()[1])*(redSensei.getPos()[1]-blueSensei.getPos()[1]))
        

        return (nbPieceActuelles-proximite_actuelle) - (nbPieceAdversaire-proximite_adversaire), None
        # return eval(plateau, joueurMax), listeMeilleursCoups
    
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
        return val, listeMeilleursCoups#, meilleurCoup

def meilleur_coup_alpha_beta(plateau,profondeur, joueurMax, joueurMin) :
    val, meilleurCoup = alphabeta(plateau, profondeur, float('-inf'), float('inf'), joueurMax, joueurMin)
    print("meilleurCOup dans max : ",meilleurCoup)
    choix = random.randint(0,len(meilleurCoup)-1)
    return meilleurCoup[choix]