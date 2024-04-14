from Ia import meilleur_coup_alpha_beta, meilleur_coup_minimax, meilleur_coup_glouton
from Pioche import Pioche
from Joueur import Joueur
from Plateau import Plateau
from Mouvement import Mouvement
import random

def joueurHumain(joueur, plateau) :
    """
    joueur humain
    """
    print("Tour du joueur",joueur.getCouleur()+".")
    print("\nCartes : \n" + "1. " + str(joueur.getCartes()[0]) + "\n2. " + str(joueur.getCartes()[1]))
    
    choixCarte=0
    while choixCarte !=1 and choixCarte !=2 :
        choixCarte = int(input("Choisissez la carte a jouer (1 ou 2) : "))
    carte=joueur.getCartes()[choixCarte-1]

    print("pions : ")
    pions = Mouvement.listePionsAutorises(plateau,joueur.getListePions(),carte.getMouvs())
    listePions = []
    for i in range (0,len(pions)-1):
        listePions.append(pions[i].getPos())
    print(listePions)
    i=0
    if len(listePions) != 0 :
        while i<1 or i>len(pions)-1 :
            if len(pions) > 1 :
                print("Choissisez une piece entre 1 et " + str(len(pions)-1))
            else :
                print("Choissisez le pion 1.")
            i = int(input("Entrer le numéro de la piece : "))

        choixPion = pions[i-1]

        print("Choisir le deplacement a effectuer.")
        listeCoups=Mouvement.listeCoupsPossibles(plateau,carte.getMouvs(),choixPion)
        print(listeCoups)
        
        j=0
        if len(listeCoups)>1 :
            while j<1 or j>len(listeCoups):
                j = int(input("Entrer le numero du coup que vous souhaitez jouer : "))
        else :
            while j!=1 :
                j=int(input("Entrer le numero du coup 1 : "))
        Mouvement.deplacer(plateau,choixPion,listeCoups[j-1])
    return plateau.echange(joueur, carte)


def joueurIaMinimax(plateau,profondeur,joueurIA, joueurHumain, max) :
    """
    joueur ia minimax
    """
    print("Tour de l'ia")
    print("Cartes : \n" + "1. " + str(joueurIA.getCartes()[0]) + "\n2. " + str(joueurIA.getCartes()[1]))

    if max :
        meilleurCoup = meilleur_coup_minimax(plateau,profondeur,joueurIA,joueurHumain, joueurIA, True)
    else :
        meilleurCoup = meilleur_coup_minimax(plateau,profondeur,joueurHumain,joueurIA, joueurIA, False)

    pion = meilleurCoup[0]
    carte = meilleurCoup[1]
    coup = meilleurCoup[2]

    Mouvement.deplacer(plateau,pion,coup)
    return plateau.echange(joueurIA, carte)


def joueurIaAlphabeta(plateau,profondeur,joueurIA, joueurHumain, max) :
    """
    joueur ia alphabeta
    """
    print("Tour de l'ia.")
    print("Cartes : \n" + "1. " + str(joueurIA.getCartes()[0]) + "\n2. " + str(joueurIA.getCartes()[1]))

    if max :
        meilleurCoup = meilleur_coup_alpha_beta(plateau,profondeur,joueurIA,joueurHumain, joueurIA, True)
    else :
        meilleurCoup = meilleur_coup_alpha_beta(plateau,profondeur,joueurHumain,joueurIA, joueurIA, False)

    pion = meilleurCoup[0]
    carte = meilleurCoup[1]
    coup = meilleurCoup[2]

    Mouvement.deplacer(plateau,pion,coup)
    return plateau.echange(joueurIA, carte)

def joueurIaGlouton(plateau,joueurIA) :
    """
    joueur ia glouton
    """
    print("Tour de l'ia.")
    print("Cartes : \n" + "1. " + str(joueurIA.getCartes()[0]) + "\n2. " + str(joueurIA.getCartes()[1]))
    meilleurCoup = meilleur_coup_glouton(plateau,joueurIA)

    pion = meilleurCoup[0]
    carte = meilleurCoup[1]
    coup = meilleurCoup[2]

    Mouvement.deplacer(plateau,pion,coup)
    return plateau.echange(joueurIA, carte)

def partieHumain() :
    """
    partie avec 2 joueur humains
    """
    pioche = Pioche()
    cartes = pioche.melange()

    couleurs = ["Rouge", "Bleu"]
    random.shuffle(couleurs)
    joueur1 = Joueur(cartes[:2],couleurs[0],None,None)
    joueur2 = Joueur(cartes[2:4],couleurs[1],None,None)

    if joueur1.getCouleur() == "Rouge" :
        plateau = Plateau(joueur1,joueur2,cartes[-1])
    else :
        plateau = Plateau(joueur2,joueur1,cartes[-1])

    plateau.initPlateau()
    gameOn = True
    cartePlateau = plateau.getCarte()

    if cartePlateau.getCouleur() == "Rouge" :     
        tour = 1
    else :
        tour = 0
        
    while gameOn :
        if  tour%2 == 1 :
            print("\nCartes du joueur adverse (Bleu) : \n" + "1. " + str(plateau.getJoueurBleu().getCartes()[0]) + "\n2. " + str(plateau.getJoueurBleu().getCartes()[1]))
            print(plateau)
            cartePlateau = joueurHumain(plateau.getJoueurRouge(), plateau)
        else :
            print("\nCartes du joueur adverse (Rouge) : \n" + "1. " + str(plateau.getJoueurRouge().getCartes()[0]) + "\n2. " + str(plateau.getJoueurRouge().getCartes()[1]))
            print(plateau)
            cartePlateau = joueurHumain(plateau.getJoueurBleu(), plateau)

        #on check si ya un coup gagnant si oui on arrete le jeu sinon tour suivant
        tour+=1
                
        if plateau.gameOver() :
            print("--------------------------------fin de partie-----------------------------------")
            print(plateau)
            print("Le joueur gagnant est le joueur "+plateau.joueurGagnant()+".")
            gameOn = False

def partieIaMinimax() :
    """
    partie avec une ia minimax
    """
    pioche = Pioche()
    cartes = pioche.melange()

    couleurs = ["Rouge", "Bleu"]
    random.shuffle(couleurs)

    joueurH = Joueur(cartes[:2],couleurs[0],False,None)
    joueurIA = Joueur(cartes[2:4],couleurs[1],True,3)

    profondeur = 3
    if joueurH.getCouleur() == "Rouge" :
        plateau = Plateau(joueurH,joueurIA,cartes[-1])
    else :
        plateau = Plateau(joueurIA,joueurH,cartes[-1])

    plateau.initPlateau()
    gameOn = True
    cartePlateau = plateau.getCarte()
    max = False 

    if cartePlateau.getCouleur() == "Rouge" :
        tour = 1
    else :
        tour = 0
        max = True
        
    while gameOn :
        if tour%2 == 1 :
            print("\nCartes du joueur adverse (Bleu) : \n" + "1. " + str(plateau.getJoueurBleu().getCartes()[0]) + "\n2. " + str(plateau.getJoueurBleu().getCartes()[1]))
            print(plateau)
            if joueurH.getCouleur() == "Rouge" :
                cartePlateau = joueurHumain(joueurH, plateau)
            else :
                cartePlateau = joueurIaMinimax(plateau,profondeur,joueurIA,joueurH,max)

        if tour%2 == 0 :
            print("\nCartes du joueur adverse (Rouge) : \n" + "1. " + str(plateau.getJoueurRouge().getCartes()[0]) + "\n2. " + str(plateau.getJoueurRouge().getCartes()[1]))
            print(plateau)
            if joueurH.getCouleur() == "Bleu" :
                cartePlateau = joueurHumain(joueurH, plateau)
            else :
                cartePlateau = joueurIaMinimax(plateau,profondeur,joueurIA,joueurH,max)

        #on check si ya un coup gagnant si oui on arrete le jeu sinon tour suivant
        tour+=1
                
        if plateau.gameOver() :
            print("--------------------------------fin de partie-----------------------------------")
            print(plateau)
            print("Le joueur gagnant est le joueur "+plateau.joueurGagnant()+".")
            gameOn = False

def partieIaAlphabeta() :
    """
    partie avec une ia alphabeta
    """
    pioche = Pioche()
    cartes = pioche.melange()

    couleurs = ["Rouge", "Bleu"]
    random.shuffle(couleurs)

    joueurH = Joueur(cartes[:2],couleurs[0],False,None)
    joueurIA = Joueur(cartes[2:4],couleurs[1],True,3)

    profondeur = 3
    if joueurH.getCouleur() == "Rouge" :
        plateau = Plateau(joueurH,joueurIA,cartes[-1])
    else :
        plateau = Plateau(joueurIA,joueurH,cartes[-1])

    plateau.initPlateau()
    gameOn = True
    cartePlateau = plateau.getCarte()
    max = False 

    if cartePlateau.getCouleur() == "Rouge" :
        tour = 1
    else :
        tour = 0
        max = True
        
    while gameOn :
        if tour%2 == 1 :
            print("\nCartes du joueur adverse (Bleu) : \n" + "1. " + str(plateau.getJoueurBleu().getCartes()[0]) + "\n2. " + str(plateau.getJoueurBleu().getCartes()[1]))
            print(plateau)
            if joueurH.getCouleur() == "Rouge" :
                cartePlateau = joueurHumain(joueurH, plateau)
            else :
                cartePlateau = joueurIaAlphabeta(plateau,profondeur,joueurIA,joueurH,max)

        if tour%2 == 0 :
            print("\nCartes du joueur adverse (Rouge) : \n" + "1. " + str(plateau.getJoueurRouge().getCartes()[0]) + "\n2. " + str(plateau.getJoueurRouge().getCartes()[1]))
            print(plateau)
            if joueurH.getCouleur() == "Bleu" :
                cartePlateau = joueurHumain(joueurH, plateau)
            else :
                cartePlateau = joueurIaAlphabeta(plateau,profondeur,joueurIA,joueurH,max)

        #on check si ya un coup gagnant si oui on arrete le jeu sinon tour suivant
        tour+=1
                
        if plateau.gameOver() :
            print("--------------------------------fin de partie-----------------------------------")
            print(plateau)
            print("Le joueur gagnant est le joueur "+plateau.joueurGagnant()+".")
            gameOn = False

def partieIaGlouton() :
    """
    partie avec une ia glouton
    """
    pioche = Pioche()
    cartes = pioche.melange()

    couleurs = ["Rouge", "Bleu"]
    random.shuffle(couleurs)

    joueurH = Joueur(cartes[:2],couleurs[0],False,None)
    joueurIA = Joueur(cartes[2:4],couleurs[1],True,4)

    profondeur = 3
    if joueurH.getCouleur() == "Rouge" :
        plateau = Plateau(joueurH,joueurIA,cartes[-1])
    else :
        plateau = Plateau(joueurIA,joueurH,cartes[-1])

    plateau.initPlateau()
    gameOn = True
    cartePlateau = plateau.getCarte()
    max = False 

    if cartePlateau.getCouleur() == "Rouge" :
        tour = 1
    else :
        tour = 0
        max = True
        
    while gameOn :
        if tour%2 == 1 :
            print("\nCartes du joueur adverse (Bleu) : \n" + "1. " + str(plateau.getJoueurBleu().getCartes()[0]) + "\n2. " + str(plateau.getJoueurBleu().getCartes()[1]))
            print(plateau)
            if joueurH.getCouleur() == "Rouge" :
                cartePlateau = joueurHumain(joueurH, plateau)
            else :
                cartePlateau = joueurIaGlouton(plateau, joueurIA)

        if tour%2 == 0 :
            print("\nCartes du joueur adverse (Rouge) : \n" + "1. " + str(plateau.getJoueurRouge().getCartes()[0]) + "\n2. " + str(plateau.getJoueurRouge().getCartes()[1]))
            print(plateau)
            if joueurH.getCouleur() == "Bleu" :
                cartePlateau = joueurHumain(joueurH, plateau)
            else :
                cartePlateau = joueurIaGlouton(plateau, joueurIA)

        #on check si ya un coup gagnant si oui on arrete le jeu sinon tour suivant
        tour+=1
                
        if plateau.gameOver() :
            print("--------------------------------fin de partie-----------------------------------")
            print(plateau)
            print("Le joueur gagnant est le joueur "+plateau.joueurGagnant()+".")
            gameOn = False

def partieIA() :
    print("1. IA minimax")
    print("2. IA alphabeta")
    print("3. IA glouton")
    
    ia = int(input())
    while ia<1 and ia > 3 :
        ia = int(input())

    if ia == 1 :
        partieIaMinimax()
    elif ia == 2 :
        partieIaAlphabeta()
    elif ia == 3 : 
        partieIaGlouton()

def menu() : 
    print("1. Jeu humain vs humain.")
    print("2. Jeu humain vs ia.")
    print("3. Jeu ia vs ia.")
    jeu = int(input())
    while jeu<1 and jeu > 3 :
        jeu = int(input())

    if jeu == 1 :
        partieHumain()
    elif jeu == 2 :
        partieIA()
    elif jeu == 3 :
        return