class Animal:
#variable partagé accessible a tout les objet de la class

    def __init__(self,poids1,taille,nom) : #initialise le poids est la taille
        self.__set_poids(poids1) 
        self.nom = nom
        self.__user_taille=taille
    
    def __get_poids(self):
        return self.__poids
    
    def __set_poids(self,poids1):
        if poids1 <= 0:
            raise ValueError()
        else:
            self.__poids=poids1
    poids =property(__get_poids,__set_poids)        
    
    def __str__(self):
        return "(nom : {0}, poids : {1},taille :{2})".format(self.nom,self.poids, self.__user_taille)

    def se_deplacer(self):   #méthode pour se deplacer
        pass


    def getInfo(self):  #permet de renvoyer les info sur l'objet , objet.getInfo()
        print("poids",self.poids,"taille",self.__user_taille)