from Plateau import Plateau
from Mouvement import Mouvement

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
    if joueurMax.getColor() == "Rouge":
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
            return 100 + profondeur
        else : 
            return -(100 + profondeur)
    
    if profondeur <= 0 : 
        nbPieceActuelles = len(plateau.getJoueurRouge().getListePions())
        nbPieceAdversaire = len(plateau.getJoueurBleu().getListePions())

        redSensei = plateau.getJoueurRouge().getSensei()
        blueSensei = plateau.getJoueurBleu().getSensei()

        proximite_actuelle = ((redSensei.getPos()[0]-blueSensei.getPos()[0])*(redSensei.getPos()[0]-blueSensei.getPos()[0])) + ((redSensei.getPos()[1]-blueSensei.getPos()[1])*(redSensei.getPos()[1]-blueSensei.getPos()[1]))
        proximité_adversaire = ((blueSensei.getPos()[0]-redSensei.getPos()[0])*(blueSensei.getPos()[0]-redSensei.getPos()[0])) + ((blueSensei.getPos()[1]-redSensei.getPos()[1])*(blueSensei.getPos()[1]-redSensei.getPos()[1]))

        return (nbPieceActuelles-proximite_actuelle) - (nbPieceAdversaire-proximité_adversaire)
    
    if max :
        val = float('-inf')
        for carte in plateau.getJoueurRouge().getCartes() :
            if carte == None : 
                continue
            for piece in plateau.getJoueurRouge().getListePiece() :
                if piece == None : 
                    continue

                for move in carte :
                    #child = Plateau(plateau) trouver un moyen de copier le plateau
                    arrive = Mouvement.pionAutorise(child,piece,move)

                    if arrive == True : 
                        coup = (piece.getPos()[0] + move[0], piece.getPos()[1] + move[1])
                        Mouvement.deplacer(child,piece,coup)

                    retVal = alphabeta(child,profondeur-1,alpha,beta,False)

                    if val < retVal :
                        val = retVal
                        if alpha < val :
                            if profondeur == plateau.getJoueurRouge().getIa() :
                                #TO DO
                                #ia = 
                                carte

                            alpha = val
                            if beta <= alpha :
                                return val
        return val
    else :
        val = float('-inf')
        for carte in plateau.getJoueurBleu().getCartes() :
            if carte == None : 
                continue
            for piece in plateau.getJoueurBleu().getListePiece() :
                if piece == None : 
                    continue

                for move in carte :
                    child = Plateau(plateau)
                    arrive = Mouvement.pionAutorise(child,piece,move)

                    if arrive == True :
                        coup = (piece.getPos()[0] + move[0], piece.getPos()[1] + move[1])
                        Mouvement.deplacer(child,piece,coup)

                    retVal = alphabeta(child,profondeur-1,alpha,beta,True)

                    if val > retVal :
                        val = retVal
                        if beta > val :
                            beta = val
                            if beta <= alpha :
                                return val
        return val

