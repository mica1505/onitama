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

