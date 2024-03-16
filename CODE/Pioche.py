import random
from Carte import Carte
class Pioche :
    def __init__(self):
        '''
        Initialise la pioche du jeu
        '''
        #chaque carte a une couleur
        self.cartes = {"Dragon":("Rouge",[(1,-2),(-1,-1),(-1,1),(1,2)]),
                       "Lapin":("Bleu",[(1,1),(-1,-1),(0,2)]),
                       "Tigre":("Bleu",[(2,0),(-1,0)]),
                       "Elephant":("Rouge",[(0,1),(0,-1),(1,1),(1,-1)]),
                       "Cobra":("Rouge",[(1,1),(-1,1),(0,-1)]),
                       "Boeuf":("Bleu",[(1,0),(0,1),(-1,0)]),
                       "Crabe":("Bleu",[(0,2),(0,-2),(1,0)]),
                       "Singe":("Bleu",[(1,1),(-1,1),(1,-1),(-1,-1)]),
                       "Cheval":("Rouge",[(-1,0),(1,0),(0,-1)]),
                       "Sanglier":("Rouge",[(0,-1),(1,0),(0,1)]),
                       "Oie":("Bleu",[(-1,1),(1,-1),(0,-1),(0,1)]),
                       "Anguille":("Bleu",[(1,-1),(-1,-1),(0,1)]),
                       "Grenouille":("Rouge",[(0,-2),(-1,1),(1,-1)]),
                       "Menthe":("Rouge",[(-1,0),(1,-1),(1,1)]),
                       "Coque":("Rouge",[(-1,-1),(1,1),(0,-1),(0,1)]),
                       "Grue":("Bleu",[(-1,-1),(-1,1),(1,0)])}
    
    def melange(self):
        '''
        Distribue de maniere aleatoire les cartes de la partie
        '''
        randCarte = random.sample(list(self.cartes.keys()),5)
        cartesDist = []
        for c in randCarte:
            cartesDist.append(Carte(c,self.cartes[c][1],self.cartes[c][0]))
                
        return cartesDist
