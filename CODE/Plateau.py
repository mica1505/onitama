from Pion import Pion

class Plateau:
    #le constructeur cree un plateau vide apres on rajoute les pions uand on cree la classe pion
    def __init__(self,joueurBleu,joueurRouge,carte):
        '''
        Pioche -> None
        '''
        self.dim=5
        self.grille = []
        self.carte = carte #la carte du plateau
        self.joueurBleu = joueurBleu
        self.joueurRouge = joueurRouge
        self.pions = [] #liste des pions dispo sur le plateau au debut ya tous les pions
        self.rs = True
        self.bs = True

    def __str__(self):
        '''
        
        '''
        res = ""
        for i in range(self.dim):
            res+="\n"
            for j  in range(self.dim):
                res+= self.grille[i][j] + " "
        return res

    def getGrille(self):
        return self.grille
    
    def getPion(self):
        return self.pions
    
    def getCarte(self):
        '''
        
        '''
        return self.carte
    
    def creerSensei(self,couleur,pos):
        '''
        
        '''
        return Pion(couleur,pos,True)
    
    def creerDisciple(self,couleur,pos):
        '''
        
        '''
        return Pion(couleur,pos,False)
    
    def initPlateau(self):
        '''
        
        '''

        for i in range(self.dim) :
            ligne = []
            for j in range(self.dim):
                ligne.append('.')
            self.grille.append(ligne)
        print(self.grille)
        for i in range(5):
            if i==2:
                self.pions.append(self.creerSensei("Bleu",(0,i)))
                self.pions.append(self.creerSensei("Rouge",(4,i)))
                self.grille[0][i] = 'R'
                self.grille[4][i] = 'B'

            else:
                self.pions.append(self.creerDisciple("Bleu",(0,i)))
                self.pions.append(self.creerDisciple("Rouge",(4,i)))
                self.grille[0][i] = 'r'
                self.grille[4][i] = 'b'
    
    def echange(self, carte):
        """
        """
        temp=self.carte
        self.carte=carte
        carte=temp
        return temp
    
    def voiePierre(self) : #gagner en mangeant le sensei adverse
        """

        """
        if (self.rs == True and self.bs == True) : 
            return True
        else : 
            return False
        
    def voieRuisseau(self) : #gagner en déplacant son sensei sur le temple adverse
        """
        """
        if self.grille[4][2] == "R" or self.grille[0][2] == 'B' :
            return True
        else : 
            return False
    
    def gameOver(self):
        '''
        Teste si les deux senseis sont toujours sur le plateau
        '''
        if (not(self.voiePierre()) or not(self.voieRuisseau())) :
            return True
        else : 
            return False