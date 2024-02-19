class Carte:

    def __init__(self,nom,mouvements,pioche):
        self.nom = nom
        self.mouvements = mouvements
        self.pioche = pioche
    '''
    {"Dragon":[],"Lapin":[],"Tigre":[],"Elephant":[],"Cobra":[],"Boeuf":[],"Crabe":[],"Singe":[],
    "Cheval":[],"Sanglier":[],"Oie":[],"Angille":[],"Grenouille":[],"Menthe":[],"Coque":[],"Grue":[]}
    '''
    def creerCarte(self,nom):
        return Carte(nom,self.pioche.getMouvs(nom),self.pioche)
    
    def getMouvs(self):
        return self.mouvements
    

    
