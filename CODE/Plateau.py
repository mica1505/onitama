

class Plateau:
    #le constructeur cree un plateau vide apres on rajoute les pions uand on cree la classe pion
    def __init__(self):
        '''
        
        '''
        self.dim=5
        self.grille = [['.' for i in range(self.dim)]*self.dim]
        self.pions = [] #liste des pions dispo sur le plateau au debut ya tous les pions
        self.carte = None #la carte du plateau

    def __str__(self):
        '''
        
        '''
        for i in range(self.dim):
            print("\n")
            for j in range(self.dim):
                print(self.grille[i][j])

    def bougerPion(self,posPrec,posSuiv):
        '''
        
        '''
        #je pense aue ca va faire appelle a une fonction de la classe Pion
        self.grille[posSuiv[0]][posSuiv[1]]=self.grille[posPrec[0]][posPrec[1]]
        #verifier si on a bouffe un pion adverse
    #pour initialiser la carte du jeu et aussi echanger la carte du plateau avec notre carte
        
    def setCarte(self, carte):
        '''
        
        '''
        self.carte = carte

    def getCarte(self):
        '''
        
        '''
        return self.carte
    
    def gameOver(self):
        '''
        Teste si les deux senseis sont toujours sur la plateau
        '''
        return
    