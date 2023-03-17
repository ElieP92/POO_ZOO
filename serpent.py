from animal import Animal

class Serpent(Animal): #sous classe annimal pour faire des serpent
    def __init__(self,poids,taille,nom) : #initialise le poids est la taille
        super().__init__(poids,taille,nom)
    
    def __str__(self):
        an_str=super().__str__()
        return an_str
    
    def se_deplacer(self):
            print("je rampe")
    
    def getInfo(self):  #permet de renvoyer les info sur l'objet , objet.getInfo()
        print("poids",self.poids,"taille",self.__user_taille)