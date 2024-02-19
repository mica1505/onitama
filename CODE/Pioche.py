import random
from Carte import Carte
class Pioche :
    def __init__(self):
        '''
        
        '''
        #chaque carte a une couleur
        self.cartes = {"Dragon":("Rouge",[(-2,1),(-1,-1),(1,-1),(2,1)]),
                       "Lapin":("Bleu",[(1,1),(-1,-1),(2,0)]),
                       "Tigre":("Bleu",[(0,2),(0,-1)]),
                       "Elephant":("Rouge",[(1,0),(-1,0),(1,1),(-1,1)]),
                       "Cobra":("Rouge",[(1,1),(1,-1),(-1,0)]),
                       "Boeuf":("Bleu",[(1,0),(0,1),(0,-1)]),
                       "Crabe":("Bleu",[(2,0),(-2,0),(0,1)]),
                       "Singe":("Bleu",[(1,1),(-1,1),(1,-1),(-1,-1)]),
                       "Cheval":("Rouge",[(-1,0),(0,1),0,-1]),
                       "Sanglier":("Rouge",[(-1,0),(1,0),(0,1)]),
                       "Oie":("Bleu",[(-1,1),(1,-1),(-1,0),(1,0)]),
                       "Anguille":("Bleu",[(-1,1),(-1,-1),(1,0)]),
                       "Grenouille":("Rouge",[(-2,0),(-1,1),(1,-1)]),
                       "Menthe":("Rouge",[(0,-1),(-1,1),(1,1)]),
                       "Coque":("Rouge",[(-1,-1),(1,1),(-1,0),(1,0)]),
                       "Grue":("Bleu",[(-1,-1),(1,-1),(0,1)])}
        
    def getMouvs(self,nom):
        '''
        
        '''
        return self.cartes[nom]
    
    def melange(self):
        '''
        
        '''
        randCarte = random.sample(list(self.cartes.keys()),5)
        cartesDist = []
        for c in randCarte:
            cartesDist.append(str(Carte(c,self.cartes[c][1],self.cartes[c][0])))
                
        return cartesDist
