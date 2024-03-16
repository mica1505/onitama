class Carte:
    def __init__(self,nom,mouvements,couleur):
        """
        Initialisation d'une carte
        """
        self.nom = nom
        self.mouvements = mouvements
        self.couleur = couleur
    '''
    {"Dragon":[],"Lapin":[],"Tigre":[],"Elephant":[],"Cobra":[],"Boeuf":[],"Crabe":[],"Singe":[],
    "Cheval":[],"Sanglier":[],"Oie":[],"Angille":[],"Grenouille":[],"Menthe":[],"Coque":[],"Grue":[]}
    '''
    def __str__(self):
        """
        Retourne sous forme de chaine de caractere attributs de la carte
        """
        mouvs = ""
        for m in self.mouvements:
            mouvs += str(m) 
        return self.nom + '('+self.couleur+')'+' : ' + mouvs
    
    def getCouleur(self):
        """
        Retourne la couleur de la carte
        """
        return self.couleur
    
    def getMouvs(self):
        """
        Retourne les mouvements de la carte
        """
        return self.mouvements