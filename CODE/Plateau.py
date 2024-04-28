from Pion import Pion

class Plateau:
    #le constructeur cree un plateau vide apres on rajoute les pions uand on cree la classe pion
    def __init__(self,joueurRouge,joueurBleu,carte):
        '''
        Pioche -> None
        Initialisation d'un plateau
        '''
        self.dim=5
        self.grille = []
        self.carte = carte #la carte du plateau
        self.joueurRouge = joueurRouge
        self.joueurBleu = joueurBleu
        self.pions = [] #liste des pions dispo sur le plateau au debut ya tous les pions
        self.rs = True
        self.bs = True

    def __str__(self):
        '''
        Retourne sous forme de chaine de caractere le plateau et la carte du plateau
        '''
        res = ""
        for i in range(self.dim):
            res+="\n"
            for j  in range(self.dim):
                res+= self.grille[i][j] + " "
            if i==2:
                res+='\t Carte Plateau -> ' + str(self.carte)
        return res

    def getGrille(self):
        '''
        Retourne la grille du plateau
        '''
        return self.grille
    
    def getListePions(self):
        '''
        Retourne les pions sur le plateau
        '''
        return self.pions
    
    def getCarte(self):
        '''
        Retourne la carte du plateau
        '''
        return self.carte
    
    def getJoueurRouge(self):
        '''
        Retourne le joueur rouge
        '''
        return self.joueurRouge
    
    def getJoueurBleu(self):
        '''
        Retourne le joueur bleu
        '''
        return self.joueurBleu
    
    def creerSensei(self,couleur,pos):
        '''
        Creer une piece sensei
        '''
        return Pion(couleur,pos,True)
    
    def creerDisciple(self,couleur,pos):
        '''
        Creer une piece disciple
        '''
        return Pion(couleur,pos,False)
    
    def captureSenseiBleu(self):
        '''
        Retourne false lorsque le sensei bleu est mange sinon True
        '''
        self.bs = False

    def captureSenseiRouge(self):
        '''
        Retourne false quand le sensei rouge est mange sinon True
        '''
        self.rs = False
    
    def initPlateau(self):
        '''
        Initialise le plateau de jeu
        '''

        for i in range(self.dim) :
            ligne = []
            for j in range(self.dim):
                ligne.append('.')
            self.grille.append(ligne)
        
        for i in range(5):
            if i==2:
                senseiRouge = self.creerSensei("Rouge",(0,i))
                senseiBleu = self.creerSensei("Bleu",(4,i))
                self.pions.append(senseiRouge)
                self.pions.append(senseiBleu)
                self.joueurRouge.setListePions(senseiRouge)
                self.joueurBleu.setListePions(senseiBleu)
                self.grille[0][i] = 'R'
                self.grille[4][i] = 'B'

            else:
                discipleRouge = self.creerDisciple("Rouge",(0,i))
                discipleBleu = self.creerDisciple("Bleu",(4,i))
                self.pions.append(discipleRouge)
                self.pions.append(discipleBleu)
                self.joueurRouge.setListePions(discipleRouge)
                self.joueurBleu.setListePions(discipleBleu)
                self.grille[0][i] = 'r'
                self.grille[4][i] = 'b'

    def echange(self, joueur, carte):
        """
        Echange la carte du plateau avec la carte joue par un joueur
        """
        joueur.removeCarte(carte)
        joueur.setCarte(self.carte)
        self.carte=carte
        return self.carte
    
    def voiePierre(self) : #gagner en mangeant le sensei adverse
        """
        Retourne false si un sensei a ete mange sinon True pour dire que les 2 senseis sont en vies
        """
        return self.bs and self.rs
        
    def voieRuisseau(self) : #gagner en déplacant son sensei sur le temple adverse
        """
        Retourne True si un sensei a atteint le temple adverse sinon False
        """
        if self.grille[4][2] == "R" or self.grille[0][2] == 'B' :
            return True
        else : 
            return False
    
    def gameOver(self):
        '''
        Retourne True si une des conditions de victoire a ete realisee sinon False
        '''
        if not(self.voiePierre()) or self.voieRuisseau() :
            return True
        else : 
            return False
        
    def coupGagnant(self):
        return not(self.voiePierre()) or self.voieRuisseau()
    
    def getPion(self,pos):
        """
        Retourne un pion du plateau
        """
        for p in self.pions :
            if p.getPos() == pos:
                return p
        
    def supPion(self,pos):
        """
        Supprime un pion du plateau
        """
        p = self.getPion(pos)
        if p != None:
            self.pions.remove(p)
            self.joueurBleu.supPion(pos)
            self.joueurRouge.supPion(pos)

    def joueurGagnant(self):
        """
        Retourne le joueur gagnant
        """
        if not(self.rs) or self.grille[0][2] == 'B' :
            return "Bleu"
        else : 
            return "Rouge"
        
    