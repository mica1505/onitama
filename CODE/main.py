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
    print("TOUR DU JOUEUR ",joueur.getCouleur()+".")
    print("\nCartes : \n" + "1. " + str(joueur.getCartes()[0]) + "\n2. " + str(joueur.getCartes()[1]))
    
    choixCarte=0
    while choixCarte !=1 and choixCarte !=2 :
        choixCarte = int(input("Choisissez la carte a jouer (1 ou 2) : "))
    carte=joueur.getCartes()[choixCarte-1]

    print("pions : ")
    pions = Mouvement.listePionsAutorises(plateau,joueur.getListePions(),carte.getMouvs())
    listePions = []
    for i in range (0,len(pions)):
        listePions.append(pions[i].getPos())
    print(listePions)
    i=0
    if len(listePions) != 0 :
        while i<1 or i>len(pions) :
            if len(pions) > 1 :
                print("Choissisez une piece entre 1 et " + str(len(pions)))
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
    # print("TOUR DE L'IA moyenne (minimax).")
    # print("Cartes : \n" + "1. " + str(joueurIA.getCartes()[0]) + "\n2. " + str(joueurIA.getCartes()[1]))

    if max :
        meilleurCoup = meilleur_coup_minimax(plateau,profondeur,joueurIA,joueurHumain, joueurIA, True)
    else :
        meilleurCoup = meilleur_coup_minimax(plateau,profondeur,joueurHumain,joueurIA, joueurIA, False)

    pion = meilleurCoup[0]
    carte = meilleurCoup[1]
    coup = meilleurCoup[2]

    Mouvement.deplacer(plateau,pion,coup)
    print("coup joué : ", coup, " carte joué : ", str(carte))
    return plateau.echange(joueurIA, carte)


def joueurIaAlphabeta(plateau,profondeur,joueurIA, joueurHumain, max) :
    """
    joueur ia alphabeta
    """
    # print("TOUR DE L'IA difficile (alphaBeta).")
    # print("Cartes : \n" + "1. " + str(joueurIA.getCartes()[0]) + "\n2. " + str(joueurIA.getCartes()[1]))

    if max :
        meilleurCoup = meilleur_coup_alpha_beta(plateau,profondeur,joueurIA,joueurHumain, joueurIA, True)
    else :
        meilleurCoup = meilleur_coup_alpha_beta(plateau,profondeur,joueurHumain,joueurIA, joueurIA, False)

    pion = meilleurCoup[0]
    carte = meilleurCoup[1]
    coup = meilleurCoup[2]

    Mouvement.deplacer(plateau,pion,coup)
    print("coup joué : ", coup, " carte joué : ", str(carte))
    return plateau.echange(joueurIA, carte)

def joueurIaGlouton(plateau,joueurIA, max) :
    """
    joueur ia glouton
    """
    # print("TOUR DE L'IA facile (glouton).")
    # print("Cartes : \n" + "1. " + str(joueurIA.getCartes()[0]) + "\n2. " + str(joueurIA.getCartes()[1]))
    meilleurCoup = meilleur_coup_glouton(plateau,joueurIA, max)

    pion = meilleurCoup[0]
    carte = meilleurCoup[1]
    coup = meilleurCoup[2]

    Mouvement.deplacer(plateau,pion,coup)
    print("coup joué : ", coup, " carte joué : ", str(carte))
    return plateau.echange(joueurIA, carte)

def partieHumain() :
    """
    partie avec 2 joueur humains
    """
    pioche = Pioche()
    cartes = pioche.melange()

    couleurs = ["Rouge", "Bleu"]
    random.shuffle(couleurs)
    joueur1 = Joueur(cartes[:2],couleurs[0],None)
    joueur2 = Joueur(cartes[2:4],couleurs[1],None)

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

    joueurH = Joueur(cartes[:2],couleurs[0],None)
    joueurIA = Joueur(cartes[2:4],couleurs[1],3)

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

    if cartePlateau.getCouleur() == joueurIA.getCouleur() :
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

    joueurH = Joueur(cartes[:2],couleurs[0],None)
    joueurIA = Joueur(cartes[2:4],couleurs[1],3)

    profondeur = 5
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

    if cartePlateau.getCouleur() == joueurIA.getCouleur() :
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

    joueurH = Joueur(cartes[:2],couleurs[0],None)
    joueurIA = Joueur(cartes[2:4],couleurs[1],None)

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

    if cartePlateau.getCouleur() == joueurIA.getCouleur() :
        max = True
        
    while gameOn :
        if tour%2 == 1 :
            print("\nCartes du joueur adverse (Bleu) : \n" + "1. " + str(plateau.getJoueurBleu().getCartes()[0]) + "\n2. " + str(plateau.getJoueurBleu().getCartes()[1]))
            print(plateau)
            if joueurH.getCouleur() == "Rouge" :
                cartePlateau = joueurHumain(joueurH, plateau)
            else :
                cartePlateau = joueurIaGlouton(plateau, joueurIA, max)

        if tour%2 == 0 :
            print("\nCartes du joueur adverse (Rouge) : \n" + "1. " + str(plateau.getJoueurRouge().getCartes()[0]) + "\n2. " + str(plateau.getJoueurRouge().getCartes()[1]))
            print(plateau)
            if joueurH.getCouleur() == "Bleu" :
                cartePlateau = joueurHumain(joueurH, plateau)
            else :
                cartePlateau = joueurIaGlouton(plateau, joueurIA, max)

        #on check si ya un coup gagnant si oui on arrete le jeu sinon tour suivant
        tour+=1
                
        if plateau.gameOver() :
            print("--------------------------------fin de partie-----------------------------------")
            print(plateau)
            print("Le joueur GAGNANT est le joueur "+plateau.joueurGagnant()+".")
            gameOn = False


def joueurIA(plateau, joueur1, joueur2, max, niveau):
    if niveau == 1 :
        return joueurIaGlouton(plateau, joueur1, max)
    elif niveau == 2 :
        return joueurIaMinimax(plateau, 3,joueur1, joueur2, max)
    elif niveau == 3 : 
        return joueurIaAlphabeta(plateau, 5,joueur1, joueur2, max)

# def partieIaVSHumain(difficulte):
def partieIaVSIa(ia1,ia2):
    pioche = Pioche()
    cartes = pioche.melange()

    couleurs = ["Rouge", "Bleu"]
    random.shuffle(couleurs)

    joueurIA1 = Joueur(cartes[:2],couleurs[0],ia1)
    joueurIA2 = Joueur(cartes[2:4],couleurs[1],ia2)

    if joueurIA1.getCouleur() == "Rouge" :
        plateau = Plateau(joueurIA1,joueurIA2,cartes[-1])
    else :
        plateau = Plateau(joueurIA2,joueurIA1,cartes[-1])

    plateau.initPlateau()
    gameOn = True
    cartePlateau = plateau.getCarte()
    max = False 

    if cartePlateau.getCouleur() == "Rouge" :
        tour = 1
    else :
        tour = 0

    if cartePlateau.getCouleur() == joueurIA1.getCouleur() :
        max = True

    while gameOn :
        print(plateau)
        if tour%2 == 1 :
            if joueurIA1.getCouleur() == "Rouge" :
                cartePlateau = joueurIA(plateau,joueurIA1,joueurIA2,max,ia1)
            else :
                cartePlateau = joueurIA(plateau,joueurIA2,joueurIA1,max,ia2)

        if tour%2 == 0 :
            if joueurIA1.getCouleur() == "Bleu" :
                cartePlateau = joueurIA(plateau,joueurIA1,joueurIA2,max,ia1)
            else :
                cartePlateau = joueurIA(plateau,joueurIA2,joueurIA1,max,ia2)

        #on check si ya un coup gagnant si oui on arrete le jeu sinon tour suivant
        tour+=1
                
        if plateau.gameOver() :
            gameOn = False
            print("--------------------------------fin de partie-----------------------------------")
            print(plateau)
            if(plateau.joueurGagnant() == joueurIA1.getCouleur()):
                print("Le joueur GAGNANT est le joueur de difficulte "+str(ia1)+".")
                return ia1
            else : 
                print("Le joueur GAGNANT est le joueur de difficulte "+str(ia2)+".")  
                return ia2 

def partieIaVSHumain(ia) :
    #differents niveaux de l'IA
    if ia == 1 :
        partieIaGlouton()
    elif ia == 2 :
        partieIaMinimax()
    elif ia == 3 : 
        partieIaAlphabeta()
        

def verifInput(chaine,debut,fin):
    print(chaine)
    numeric = False
    while (not numeric):
        nombre = input(f"Entrez un nombre entre {debut} et {fin} : ")
        if not nombre.isdigit():
            print("Veuillez entrer un nombre entier.")
            continue
        nombre = int(nombre)
        if nombre >= debut and nombre <= fin:
            numeric = True
        else:
            print(f"Nombre invalide. Veuillez entrer un nombre entre {debut} et {fin}.")
    return nombre

def menu() : 

    jeu = verifInput("1. Jeu humain vs humain.\n2. Jeu humain vs ia.\n3. Jeu ia vs ia.",1,3)

    if jeu == 1 :
        partieHumain()
    elif jeu == 2 :
        partieIaVSHumain(verifInput("1. Facile\n2. Moyen\n3. Difficle\n",1,3))
    elif jeu == 3 :
        print("Niveau IA1 : ")
        n1 = verifInput("1. Facile\n2. Moyen\n3. Difficle\n",1,3)
        print("Niveau IA2 : ")
        n2 = verifInput("1. Facile\n2. Moyen\n3. Difficle\n",1,3)
        partieIaVSIa(n1,n2)
        #ia contre ia

facile =0
moyen = 0
difficile = 0

for i in range(1,51): 
    print(f"+++++++++++++++++++++++++++++++++++partie {i}++++++++++++++++++++++++++++++++++")  
    res = partieIaVSIa(1,2)
    if res == 1:
        facile+=1
    elif res == 2:
        moyen+=1
    elif res == 3:
        difficile+=1
    print("facile : ",facile, "moyen : ",moyen, "difficile : ", difficile)

'''
    partieIaVSIa(1,2)
    partieIaVSIa(1,3)
    partieIaVSIa(2,3)


'''