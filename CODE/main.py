from Pioche import Pioche
from Joueur import Joueur
from Plateau import Plateau
from Mouvement import Mouvement

print("1. Jeu humain vs humain.")
print("2. Jeu humain vs ia.")
print("3. Jeu ia vs ia.")
jeu = int(input())

pioche = Pioche()
cartes = pioche.melange()
joueurRouge = Joueur(cartes[:2],None,"Rouge",None,None)
joueurBleu = Joueur(cartes[2:4],None,"Bleu",None,None)
plateau = Plateau(joueurRouge,joueurBleu,cartes[-1])
plateau.initPlateau()
print(plateau)

gameOn = True
cartePlateau = plateau.getCarte()
if cartePlateau.getCouleur() == "Rouge" :
    tour = 1
else :
    tour = 0

while gameOn :
    print("Carte plateau : \n" + str(cartePlateau))
    if tour%2 == 1 :
        print("Tour du joueur rouge.")
        print("Carte du joueur rouge : \n" + "1. " + str(joueurRouge.getCartes()[0]) + "\n2. " + str(joueurRouge.getCartes()[1]))
       
        choix = int(input("Choisissez la carte a jouer : "))
        print("Choisir la piece a jouer : ")
        i = int(input("Entrer la ligne : "))
        j = int(input("Entrer la colonne : "))

        piece = ()
        coups = Mouvement(plateau, piece, joueurRouge.getCartes()[choix-1].getMouvs())
        print("Choisir le deplacement a effectue : ")
        mouvement=False
        while(not(mouvement)) : #tant que le mouvement n'est pas autorisé
            i = int(input("Entrer la ligne : "))
            j = int(input("Entrer la colonne : "))
        tour+=1
        cartePlateau = plateau.echange()

    if tour%2 == 0 :
        print("Tour du joueur bleu.")
        print("Carte du joueur bleu : \n" + "1. " + str(joueurBleu.getCartes()[0]) + "\n2. " + str(joueurBleu.getCartes()[1]))
        choix = int(input("Choisissez la carte a jouer : "))
        i = int(input("Entrer la ligne : "))
        j = int(input("Entrer la colonne : "))
        mouvement=False
        while(not(mouvement)) : #tant que le mouvement n'est pas autorisé
            i = int(input("Entrer la ligne : "))
            j = int(input("Entrer la colonne : "))
            piece = ()
            coups = Mouvement(plateau, piece, joueurRouge.getCartes()[choix-1].getMouvs())

        tour+=1
        cartePlateau = plateau.echange()
            
    if plateau.gameOver() : 
        gameOn = False