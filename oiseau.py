
from animal import Animal
class Oiseau(Animal):
    
    
    def __init__(self,poids,taille,altitude,nom) : #initialise le poids est la taille
        super().__init__(poids,taille,nom)
        self.__user_alt_max=altitude

    def se_deplacer(self):
        print("je vol")

    def __str__(self):
        an_str=super().__str__()
        ois_str= "(alt max de vol:{0})".format(self.__user_alt_max)
        return an_str+ois_str

    def getInfo(self):  #permet de renvoyer les info sur l'objet , objet.getInfo()
        print("poids",self.poids,"taille",self.__user_taille,"altitude",self.__user_alt_max)