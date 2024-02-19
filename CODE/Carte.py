class Carte:
    def __init__(self,nom,mouvements,couleur):
        self.nom = nom
        self.mouvements = mouvements
        self.couleur = couleur
    '''
    {"Dragon":[],"Lapin":[],"Tigre":[],"Elephant":[],"Cobra":[],"Boeuf":[],"Crabe":[],"Singe":[],
    "Cheval":[],"Sanglier":[],"Oie":[],"Angille":[],"Grenouille":[],"Menthe":[],"Coque":[],"Grue":[]}
    '''
    def __str__(self):
        mouvs = ""
        for m in self.mouvements:
            mouvs += str(m) 
        return self.nom + ' : ' + mouvs
    
    def getCouleur(self):
        return self.couleur
    
    def getMouvs(self):
        return self.mouvements