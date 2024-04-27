import math
from Plateau import Plateau
from Mouvement import Mouvement
import copy
import random


def evalScore(plateau,joueur,max):
    """
    Plateau x Joueur -> int
    """
    scoreJoueur = joueur.getScore()
    if joueur.getCouleur == "Rouge" :
        scoreAdverse = plateau.getJoueurBleu().getScore()
    else : 
        scoreAdverse = plateau.getJoueurRouge().getScore()

    if max:
        return scoreJoueur - scoreAdverse
    else : 
        return scoreAdverse - scoreJoueur
    
def distanceMaitre(plateau, joueur) :
    """
    Evalue la distance entre le maitre du joueur et celui de l'adversaire
    """
    nbPieceActuelles = len(joueur.getListePions())
    # joueurRouge =  plateau.getJoueurRouge().getListePions()
    # for i in joueurRouge :
    #     print(i.getPos())
    #     print(i.getSensei())
    #     print(plateau.voiePierre())
    # print(joueurRouge)
    # if plateau.voiePierre():
    #     Sensei = plateau.getJoueurRouge().getSensei()
    #     print("sensei : ",Sensei)
    #     redSensei = plateau.getJoueurRouge().getSensei().getPos()
    #     blueSensei = plateau.getJoueurBleu().getSensei().getPos()
    #     print(redSensei, blueSensei)

    if joueur.getCouleur() == "Rouge" :
        redSensei = joueur.getSensei().getPos()
        blueSensei = plateau.getJoueurBleu().getSensei().getPos()
        nbPieceAdversaire = len(plateau.getJoueurBleu().getListePions())
        proximite_actuelle = ((redSensei[0]-blueSensei[0])*(redSensei[0]-blueSensei[0])) + ((redSensei[1]-blueSensei[1])*(redSensei[1]-blueSensei[1]))
        proximite_adversaire = ((blueSensei[0]-redSensei[0])*(blueSensei[0]-redSensei[0])) + ((blueSensei[1]-redSensei[1])*(blueSensei[1]-redSensei[1]))
    else :
        redSensei = plateau.getJoueurRouge().getSensei().getPos()
        blueSensei = joueur.getSensei().getPos()
        nbPieceAdversaire = len(plateau.getJoueurRouge().getListePions())
        proximite_actuelle = ((blueSensei[0]-redSensei[0])*(blueSensei[0]-redSensei[0])) + ((blueSensei[1]-redSensei[1])*(blueSensei[1]-redSensei[1]))
        proximite_adversaire = ((redSensei[0]-blueSensei[0])*(redSensei[0]-blueSensei[0])) + ((redSensei[1]-blueSensei[1])*(redSensei[1]-blueSensei[1]))

    return (nbPieceActuelles-proximite_actuelle) - (nbPieceAdversaire-proximite_adversaire)

def nbMouvDispo(plateau,joueur) :
    """
    Retourne le nombre de mouvement disponibles pour le joueur
    """
    return len(Mouvement.listeCoupsLegaux(plateau,joueur))

def controleCentrePlateau(plateau, joueur):
    """
    Evalue le controle du centre du plateau pour le joueur
    """
    controleCentre = 0
    for i in range(1,4) :
        for j in range(1,4) :
            if (plateau.getGrille()[i][j] == 'r' or plateau.getGrille()[i][j] == "R") and joueur.getCouleur() == "Rouge" : 
                controleCentre +=1
            elif (plateau.getGrille()[i][j] == 'b' or plateau.getGrille()[i][j] == "B") and joueur.getCouleur() == "Bleu" :
                controleCentre +=1

    return controleCentre

def protectionMaitre(plateau, joueur) : 
    """
    Evalue le niveau de protection du maitre
    """
    maitre = joueur.getSensei().getPos()
    protection = 0
    for i in range(-1,2) :
        for j in range(-1,2) :
            x = maitre[0] + i
            y = maitre[1] + j
            if Mouvement.positionValide((x,y)) :
                if plateau.getGrille()[x][y] == 'r' and joueur.getCouleur() == "Rouge" : 
                    protection +=1
                elif plateau.getGrille()[x][y] == 'b' and joueur.getCouleur() == "Bleu" :
                    protection +=1

    return protection
    
def menaceMaitre(plateau, joueur) :
    """
    Evalue le nombre de piece qui menace le maitre adverse
    """
    menace = 0
    if joueur.getCouleur() == "Rouge" : 
        maitreAdverse = plateau.getJoueurBleu().getSensei()
    else :
        maitreAdverse = plateau.getJoueurRouge().getSensei()

    for coup in Mouvement.listeCoupsLegaux(plateau, joueur) :
        if coup == maitreAdverse :
            menace += 1

    return menace 

def mobilitePions(plateau, joueur) :
    """
    Evalue la mobilite des pions du joueur
    """
    listeCase = []
    mobilite = 0
    for coup in Mouvement.listeCoupsLegaux(plateau, joueur) :
        if coup not in listeCase :
            listeCase.append(coup)
            mobilite += 1
    
    return mobilite

def controleDiagonales(plateau, joueur) :
    """
    Evalue le controle des diagonales par le joueur
    """
    controle = 0
    for i in range(5) :
        if (plateau.getGrille()[i][i] == 'R' or plateau.getGrille()[i][i] == 'r') and joueur.getCouleur() == "Rouge" :
            controle +=1 
        elif (plateau.getGrille()[i][4-i] == 'R' or plateau.getGrille()[i][4-i] == 'r') and joueur.getCouleur() == "Rouge" :
            controle +=1
        elif (plateau.getGrille()[i][i] == 'B' or plateau.getGrille()[i][i] == 'b') and joueur.getCouleur() == "Bleu" :
            controle +=1 
        if (plateau.getGrille()[i][4-i] == 'B' or plateau.getGrille()[i][4-i] == 'b') and joueur.getCouleur() == "Bleu" :
            controle +=1 
        
    return controle

def evalPosition(plateau, joueur, max) :
    """
    Evalue la position d'un joueur
    """
    scoreJoueur = 0
    #scoreJoueur += distanceMaitre(plateau, joueur)
    scoreJoueur = nbMouvDispo(plateau, joueur) + controleCentrePlateau(plateau, joueur) + menaceMaitre(plateau, joueur) + mobilitePions(plateau, joueur) + controleDiagonales(plateau, joueur) #+ protectionMaitre(plateau, joueur)
    if joueur.getCouleur() == "Rouge" : 
        scoreAdverse = nbMouvDispo(plateau, plateau.getJoueurBleu()) + controleCentrePlateau(plateau, plateau.getJoueurBleu()) + menaceMaitre(plateau, plateau.getJoueurBleu()) + mobilitePions(plateau, plateau.getJoueurBleu()) + controleDiagonales(plateau, plateau.getJoueurBleu()) #+ protectionMaitre(plateau, plateau.getJoueurBleu())
    else :
        scoreAdverse = nbMouvDispo(plateau, plateau.getJoueurRouge()) + controleCentrePlateau(plateau, plateau.getJoueurRouge()) + menaceMaitre(plateau, plateau.getJoueurRouge()) + mobilitePions(plateau, plateau.getJoueurRouge()) + controleDiagonales(plateau, plateau.getJoueurRouge()) #+ protectionMaitre(plateau, plateau.getJoueurRouge())

    if max:
        return scoreJoueur - scoreAdverse
    else : 
        return scoreAdverse - scoreJoueur
    
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
        return evalScore(plateau, joueurIA,not(boolMax)), listeMeilleursCoups

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
                    if joueurMax.getCouleur() == "Rouge":
                        coup = (piece.getPos()[0] + move[0], piece.getPos()[1] + move[1])
                    else : 
                        coup = (piece.getPos()[0] - move[0], piece.getPos()[1] + move[1])
 
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
                    if joueurMin.getCouleur() == "Rouge":
                        coup = (piece.getPos()[0] + move[0], piece.getPos()[1] + move[1])
                    else : 
                        coup = (piece.getPos()[0] - move[0], piece.getPos()[1] + move[1])

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
        return evalPosition(plateau, joueurIA, boolMax), listeMeilleursCoups

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
                    if joueurMax.getCouleur() == "Rouge":
                        coup = (piece.getPos()[0] + move[0], piece.getPos()[1] + move[1])
                    else : 
                        coup = (piece.getPos()[0] - move[0], piece.getPos()[1] + move[1])
 
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
                    if joueurMin.getCouleur() == "Rouge":
                        coup = (piece.getPos()[0] + move[0], piece.getPos()[1] + move[1])
                    else : 
                        coup = (piece.getPos()[0] - move[0], piece.getPos()[1] + move[1])

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
    
def glouton(plateau, joueurIA, boolMax) :
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
                if joueurIA.getCouleur() == "Rouge":
                    coup = (piece.getPos()[0] + move[0], piece.getPos()[1] + move[1])
                else : 
                    coup = (piece.getPos()[0] - move[0], piece.getPos()[1] + move[1])

                if arrive : 
                    Mouvement.deplacer(child, piece, coup)
                    child.echange(player, carte)

                    valeur = evalPosition(child, joueurIA, boolMax)
                    piece.setPos(depart)

                    if valeur > meilleurVal :
                        meilleurVal = valeur
                        meilleurCoup = [piece, carte, coup]
                    
                    if child.gameOver():
                        meilleurVal = float('inf')
                        meilleurCoup = [piece, carte, coup]
                        return meilleurCoup

    return meilleurCoup


def meilleur_coup_minimax(plateau,profondeur, joueurMax, joueurMin, joueurIA, boolIA) :
    """
    Retourne le meilleur coup du minimax
    """
    val, meilleurCoup = minimax(plateau, profondeur, float('-inf'), float('inf'), joueurMax, joueurMin, joueurIA, [], boolIA)
    return meilleurCoup

def meilleur_coup_alpha_beta(plateau,profondeur, joueurMax, joueurMin, joueurIA, boolIA) :
    """
    Retourne le meilleur coup d'alphabeta
    """
    val, meilleurCoup = alphabeta(plateau, profondeur, float('-inf'), float('inf'), joueurMax, joueurMin, joueurIA, [], boolIA)
    return meilleurCoup

def meilleur_coup_glouton(plateau, joueurIA, boolMax) :
    """
    Retourne le meilleur coup de l'algo glouton
    """
    meilleurCoup = glouton(plateau, joueurIA, boolMax)
    return meilleurCoup

