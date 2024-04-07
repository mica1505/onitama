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

def eval(plateau,joueur):
    """
    Plateau x Joueur -> int
    """
    if joueur.getCouleur() == "Rouge":
        return plateau.getJoueurRouge().getScore() - plateau.getJoueurBleu().getScore()
    else : 
        return plateau.getJoueurBleu().getScore() - plateau.getJoueurRouge().getScore()
    
def minimax(plateau, profondeur, alpha, beta, joueurMax, joueurMin, joueurIA, listeMeilleursCoups, boolMax):
    """
    algorithme minimax
    """
    if plateau.gameOver() :
        if plateau.joueurGagnant() == joueurMax.getCouleur() :
            return float('inf'), listeMeilleursCoups
        else : 
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
        return eval(plateau, joueurIA), listeMeilleursCoups

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
                        MeilleursCoups = [piece,carte,coup]
                        
                        retVal, listeMeilleursCoups = minimax(child,profondeur-1,alpha,beta,joueurMax, joueurMin, joueurIA, listeMeilleursCoups, False)
                        piece.setPos(depart)

                        if retVal > bestValue :
                            listeMeilleursCoups = MeilleursCoups
                            bestValue = retVal

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
                        MeilleursCoups = [piece,carte,coup]
 
                        retVal, listeMeilleursCoups = minimax(child,profondeur-1,alpha,beta,joueurMax, joueurMin, joueurIA, listeMeilleursCoups, True)
                        piece.setPos(depart)

                        if  retVal < bestValue :
                            bestValue = retVal
                            listeMeilleursCoups = MeilleursCoups
                        
        return bestValue, listeMeilleursCoups
                        
def alphabeta(plateau, profondeur, alpha, beta, joueurMax, joueurMin, joueurIA, listeMeilleursCoups, boolMax):
    """
    algorithme alphabeta
    """
    if plateau.gameOver() :
        if plateau.joueurGagnant() == joueurMax.getCouleur() :
            return float('inf'), listeMeilleursCoups
        else : 
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
        return eval(plateau, joueurIA), listeMeilleursCoups

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
                        MeilleursCoups = [piece,carte,coup]
                        
                        retVal, listeMeilleursCoups = alphabeta(child,profondeur-1,alpha,beta,joueurMax, joueurMin, joueurIA, listeMeilleursCoups, False)
                        piece.setPos(depart)

                        if retVal > bestValue :
                            listeMeilleursCoups = MeilleursCoups
                            bestValue = retVal
                        
                        alpha = max(alpha, bestValue)
                        if beta <= alpha :
                            break #elagage

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
                        MeilleursCoups = [piece,carte,coup]
 
                        retVal, listeMeilleursCoups = alphabeta(child,profondeur-1,alpha,beta,joueurMax, joueurMin, joueurIA, listeMeilleursCoups, True)
                        piece.setPos(depart)

                        if retVal < bestValue :
                            bestValue = retVal
                            listeMeilleursCoups = MeilleursCoups

                        beta = min(beta, bestValue)
                        if beta <= alpha :
                            break #elagage
                        
        return bestValue, listeMeilleursCoups
    
def glouton(plateau, joueurIA) :
    """
    Algorithme glouton
    """
    meilleurCoup = []
    meilleurVal = -float('inf')
    listeCartes = joueurIA.getCartes()
    listePions = joueurIA.getListePions()


    for carte in listeCartes :
        for piece in listePions :
            mouvements = carte.getMouvs()
            for move in mouvements :
                child = copy.deepcopy(plateau)
                player = copy.deepcopy(joueurIA)
                depart = piece.getPos()
                arrive = Mouvement.pionAutorise(child, piece, move)
                coup = (piece.getPos()[0] + move[0], piece.getPos()[1] + move[1])

                if arrive : 
                    Mouvement.deplacer(child, piece, coup)
                    child.echange(player, carte)

                    valeur = eval(child, joueurIA)
                    piece.setPos(depart)

                    if valeur > meilleurVal :
                        meilleurVal = valeur
                        meilleurCoup = [piece, carte, coup]
                    
                    if child.gameOver():
                        return meilleurCoup

    return meilleurCoup


def meilleur_coup_minimax(plateau,profondeur, joueurMax, joueurMin, joueurIA, boolIA) :
    """
    Retourne le meilleur coup du minimax
    """
    val, meilleurCoup = minimax(plateau, profondeur, float('-inf'), float('inf'), joueurMax, joueurMin, joueurIA, [], boolIA)
    return meilleurCoup#[choix]

def meilleur_coup_alpha_beta(plateau,profondeur, joueurMax, joueurMin, joueurIA, boolIA) :
    """
    Retourne le meilleur coup d'alphabeta
    """
    val, meilleurCoup = alphabeta(plateau, profondeur, float('-inf'), float('inf'), joueurMax, joueurMin, joueurIA, [], boolIA)
    return meilleurCoup#[choix]

def meilleur_coup_glouton(plateau, joueurIA) :
    """
    Retourne le meilleur coup de l'algo glouton
    """
    meilleurCoup = glouton(plateau, joueurIA)
    return meilleurCoup