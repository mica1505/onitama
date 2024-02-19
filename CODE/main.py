from Pioche import Pioche
from Joueur import Joueur
from Plateau import Plateau


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
        print("Tour du joueurRouge.")
        print("Carte du joueur rouge : \n" + "1. " + str(joueurRouge.getCartes()[0]) + "\n2. " + str(joueurRouge.getCartes()[1]))
       
        choix = int(input("Choisissez la carte a jouer : "))
       
        i = int(input("Entrer la ligne : "))
        j = int(input("Entrer la colonne : "))

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

        tour+=1
        cartePlateau = plateau.echange()
            
    if plateau.gameOver() : 
        gameOn = False