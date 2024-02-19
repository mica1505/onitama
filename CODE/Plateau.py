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
        
    def __str__(self):
        '''
        
        '''
        res = ""
        for i in range(self.dim):
            res+="\n"
            for j  in range(self.dim):
                res+= self.grille[i][j] + " "
        return res


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
    
    def getPioche(self):
        '''
        
        '''
        return self.pioche
    
    def gameOver(self):
        '''
        Teste si les deux senseis sont toujours sur la plateau
        '''
        return
    
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
                self.grille[0][i] = 'd'
                self.grille[4][i] = 'd'

            else:
                self.pions.append(self.creerDisciple("Bleu",(0,i)))
                self.pions.append(self.creerDisciple("Rouge",(4,i)))
                self.grille[0][i] = 's'
                self.grille[4][i] = 's'



    def premierJoueur(self):
        '''
        
        '''
        return self.carte.getCouleur() # soit on retourne la chaine de caractere soit on retourne le joueur
    
    def initCartePlateau(self):
        '''
        
        '''
        return 
