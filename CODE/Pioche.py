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