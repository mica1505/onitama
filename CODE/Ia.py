import math
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
    
def distanceMaitre(plateau, joueur) :
    """
    Evalue la distance entre le maitre du joueur et celui de l'adversaire
    """
    nbPieceActuelles = len(joueur.getListePions())
    redSensei = plateau.getJoueurRouge().getSensei()
    blueSensei = plateau.getJoueurBleu().getSensei()

    if joueur.getCouleur() == "Rouge" :
        nbPieceAdversaire = len(plateau.getJoueurBleu().getListePions())
        proximite_actuelle = ((redSensei.getPos()[0]-blueSensei.getPos()[0])*(redSensei.getPos()[0]-blueSensei.getPos()[0])) + ((redSensei.getPos()[1]-blueSensei.getPos()[1])*(redSensei.getPos()[1]-blueSensei.getPos()[1]))
        proximite_adversaire = ((blueSensei.getPos()[0]-redSensei.getPos()[0])*(blueSensei.getPos()[0]-redSensei.getPos()[0])) + ((blueSensei.getPos()[1]-redSensei.getPos()[1])*(blueSensei.getPos()[1]-redSensei.getPos()[1]))
    else :
        nbPieceAdversaire = len(plateau.getJoueurRouge().getListePions())
        proximite_actuelle = ((blueSensei.getPos()[0]-redSensei.getPos()[0])*(blueSensei.getPos()[0]-redSensei.getPos()[0])) + ((blueSensei.getPos()[1]-redSensei.getPos()[1])*(blueSensei.getPos()[1]-redSensei.getPos()[1]))
        proximite_adversaire = ((redSensei.getPos()[0]-blueSensei.getPos()[0])*(redSensei.getPos()[0]-blueSensei.getPos()[0])) + ((redSensei.getPos()[1]-blueSensei.getPos()[1])*(redSensei.getPos()[1]-blueSensei.getPos()[1]))

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
    maitre = joueur.getSensei()
    protection = 0
    for i in range(-1,2) :
        for j in range(-1,2) :
            if plateau.getGrille()[maitre.getPos()[0] + i][maitre.getPos()[1] +j] == 'r' and joueur.getCouleur() == "Rouge" : 
                protection +=1
            elif plateau.getGrille()[maitre.getPos()[0] + i][maitre.getPos()[1] +j] == 'b' and joueur.getCouleur() == "Bleu" :
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
    return meilleurCoup

def meilleur_coup_alpha_beta(plateau,profondeur, joueurMax, joueurMin, joueurIA, boolIA) :
    """
    Retourne le meilleur coup d'alphabeta
    """
    val, meilleurCoup = alphabeta(plateau, profondeur, float('-inf'), float('inf'), joueurMax, joueurMin, joueurIA, [], boolIA)
    return meilleurCoup

def meilleur_coup_glouton(plateau, joueurIA) :
    """
    Retourne le meilleur coup de l'algo glouton
    """
    meilleurCoup = glouton(plateau, joueurIA)
    return meilleurCoup

def monteCarloTreeSearch(plateau, joueurMax, joueurMin, joueurIA, profondeurMax, simulations) :
    racine = {
        'state' : plateau,
        'parent' : None,
        'children' : [],
        'visit' : 0,
        'wins' : 0
    }

    for i in range(simulations) :
        #phase de selection
        noeudSelectionne = selectionnerNoeud(racine, joueurMax, joueurMin, joueurIA)

        #phase de simulation
        resultatSimulation = simuler(noeudSelectionne['state'], joueurMax, joueurMin, joueurIA, profondeurMax)

        #phase de backpropagation
        retropropagation(noeudSelectionne, resultatSimulation)

    #choisir le meilleur coup a partir du noeud racine
    meilleurCoup = choisirMeilleurCoup(racine)

    return meilleurCoup

def selectionnerNoeud(noeud, joueurMax, joueurMin, joueurIA) :
    #On parcours l'arbre en utilisant UCT (Upper Confidence Bound for Trees)
    while not estFeuille(noeud) : 
        noeud = choisirEnfantUct(noeud)

    #Si le noeud est une feuille, on fait une expansion
    if len(noeud['children']) == 0 : 
        expand(noeud, joueurMax, joueurMin, joueurIA)
    
    #On selectionne un enfant au hasard parmi les enfants de ce noeud
    return random.choice(noeud['children'])

def estFeuille(noeud) : 
    return len(noeud['children']) == 0

def choisirEnfantUct(noeud) :
    """
    algorithme uct
    """

    C=1.4

    #Calculer l'UCT pour chaque enfant et choisir celui avec la valeur maximale
    meilleursEnfants = []

    for enfant in noeud['children'] : 
        if enfant['visits'] == 0 : 
            return enfant #chosir un enfant non exploré immédiatement
        else : 
            uctValue = enfant['wins']/enfant['visits'] + C*math.sqrt(math.log(noeud['visits']/enfant['visits']))
            meilleursEnfants.append((enfant, uctValue))

    meilleurEnfant = max(meilleursEnfants, key=lambda x: x[1])[0]
    return meilleurEnfant

def expand(noeud, joueurMax, joueurMin, joueurIA) : 
    etat = noeud['state']

    coupsPossibles = Mouvement.listeCoupsLegaux(noeud, joueurIA)

    for coup in coupsPossibles : 
        nouvelEtat = 1#appliquer_action(etat, action)

        nouveauNoeud = {
            'state' : nouvelEtat,
            'parent' : None,
            'children' : [],
            'visit' : 0,
            'wins' : 0
        }
        noeud['children'].append(nouveauNoeud)

def simuler(plateau, joueurMax, joueurMin, joueurIA, profondeurMax) : 
    #Simuler un jeu a partir de l'etat du plateau jusqu'a une condition de fin
    while not plateau.gameOver() and profondeurMax > 0 : 
        coupsPossibles = Mouvement.listeCoupsLegaux(plateau, joueurIA)
        #On choisit des coups aleatoires a partir de l'etat actuel du plateau
        coupAleatoire = random.choice(coupsPossibles)
        Mouvement.deplacer(coupAleatoire[0], coupAleatoire[1])
        profondeurMax -= 1
    return eval(plateau, joueurIA)

def retropropagation(noeud, resultSimulation) :
    while noeud is not None :
        noeud['visits'] += 1
        if resultSimulation > 0 :
            noeud['wins'] += 1
        #aller au noeud parent
        noeud = noeud['parent']
    return

def choisirMeilleurCoup(racine) :
    meilleurCoup = max(racine['children'], key=lambda enfant : enfant['visits'])
    return #actionCorrespondante(meilleurCoup['state'], racine['state'])
