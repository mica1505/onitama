import random
from Carte import Carte
class Pioche :
    def __init__(self):
        '''
        
        '''
        self.cartes = {"Dragon":[],"Lapin":[],"Tigre":[],"Elephant":[],"Cobra":[],"Boeuf":[],"Crabe":[],"Singe":[],
                       "Cheval":[],"Sanglier":[],"Oie":[],"Angille":[],"Grenouille":[],"Menthe":[],"Coque":[],"Grue":[]}
        
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
            cartesDist.append(str(Carte(c,self.cartes[c])))
                
        return cartesDist
    