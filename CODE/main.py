from Pioche import Pioche
from Joueur import Joueur
from Plateau import Plateau
from Mouvement import Mouvement

# print("1. Jeu humain vs humain.")
# print("2. Jeu humain vs ia.")
# print("3. Jeu ia vs ia.")
# jeu = int(input())

def joueur1(joueurRouge, plateau) :
    print("Tour du joueur ROUGE.")
    print("Cartes : \n" + "1. " + str(joueurRouge.getCartes()[0]) + "\n2. " + str(joueurRouge.getCartes()[1]))
    
    choixCarte=0
    while choixCarte !=1 and choixCarte !=2 :
        choixCarte = int(input("Choisissez la carte a jouer (1 ou 2) : "))
    carte=joueurRouge.getCartes()[choixCarte-1]

    print("pions : ")
    pions = Mouvement.listePionsAutorises(plateau,joueurRouge.getListePions(),carte.getMouvs()) 
    print(pions)
    i=0
    while i<1 or i>len(pions) :
        if len(pions) > 1 :
            print("Choissisez une piece entre 1 et " + str(len(pions)))
        else :
            print("Choissisez le pion 1.")
        i = int(input("Entrer le numéro de la piece : "))

    choixPion = joueurRouge.getListePions()[i-1]

    print("Choisir le deplacement a effectuer.")
    listeCoups=Mouvement.listeCoupsPossibles(plateau,carte.getMouvs(),choixPion)
    print(listeCoups)
    
    j=0
    if len(listeCoups)>1 :
        while j<1 or j>len(listeCoups):
            j = int(input("Entrer le numéro du coup que vous souhaitez jouer : "))
    else :
        while j!=1 :
            j=int(input("Entrer le numéro du coup 1 : "))
    Mouvement.deplacer(plateau,choixPion,listeCoups[j-1])
    print(plateau.getListePions())
    return plateau.echange(joueurRouge, carte)

def joueur2(joueurBleu, plateau) : 
    print("Tour du joueur BLEU.")
    print("Cartes : \n" + "1. " + str(joueurBleu.getCartes()[0]) + "\n2. " + str(joueurBleu.getCartes()[1]))
    
    choixCarte=0
    while choixCarte !=1 and choixCarte !=2 :
        choixCarte = int(input("Choisissez la carte a jouer (1 ou 2) : "))
    carte=joueurBleu.getCartes()[choixCarte-1]

    print("pions : ")
    pions = Mouvement.listePionsAutorises(plateau,joueurBleu.getListePions(),carte.getMouvs()) 
    print(pions)

    i = 0
    while i<1 or i>len(pions) :
        if len(pions) > 1 :
            print("Choissisez une piece entre 1 et " + str(len(pions)))
        else :
            print("Choissisez le pion 1.")
        i = int(input("Entrer le numéro de la piece : "))
    choixPion = joueurBleu.getListePions()[i-1]

    print("Choisir le deplacement a effectuer.")
    listeCoups=Mouvement.listeCoupsPossibles(plateau,carte.getMouvs(),choixPion)
    print(listeCoups)

    j=0
    if len(listeCoups)>1 :
        while j<1 or j>len(listeCoups):
            j = int(input("Entrer le numéro du coup que vous souhaitez jouer : "))
    else :
        while j!=1 :
            j=int(input("Entrer le numéro du coup 1 : "))
    Mouvement.deplacer(plateau,choixPion,listeCoups[j-1])
    return plateau.echange(joueurBleu, carte)



def partie() :
    pioche = Pioche()
    cartes = pioche.melange()
    joueurRouge = Joueur(cartes[:2],"Rouge",None,None)
    joueurBleu = Joueur(cartes[2:4],"Bleu",None,None)
    plateau = Plateau(joueurRouge,joueurBleu,cartes[-1])
    plateau.initPlateau()
    gameOn = True
    cartePlateau = plateau.getCarte()
    if cartePlateau.getCouleur() == "Rouge" :
        tour = 1
    else :
        tour = 0
        
    while gameOn :
        print(plateau)
        #print("Carte plateau : \n" + str(cartePlateau))
        if tour%2 == 1 :
            cartePlateau = joueur1(joueurRouge, plateau)

        if tour%2 == 0 :
            cartePlateau = joueur2(joueurBleu, plateau)

        #on check si ya un coup gagnant si oui on arrete le jeu sinon tour suivant
        tour+=1
                
        if plateau.gameOver() :
            gameOn = False

partie()