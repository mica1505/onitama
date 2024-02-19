class Carte:

    def __init__(self,nom,mouvements):
        self.nom = nom
        self.mouvements = mouvements
    '''
    {"Dragon":[],"Lapin":[],"Tigre":[],"Elephant":[],"Cobra":[],"Boeuf":[],"Crabe":[],"Singe":[],
    "Cheval":[],"Sanglier":[],"Oie":[],"Angille":[],"Grenouille":[],"Menthe":[],"Coque":[],"Grue":[]}
    '''
    def __str__(self):
        mouvs = ""
        for m in self.mouvements:
            mouvs += "(" + m[0] + "," + m[1] + ")"
        return self.nom + ' : ' + mouvs
    

    
