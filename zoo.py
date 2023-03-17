from animal import Animal
class Zoo:
    def __init__(self, animaux):
        self.animaux = animaux

    def ajouter_animal(self, animal):
        if isinstance(animal,list):
            self.animaux.extend(animal)
        else:
            self.animaux.append(animal)
    
    def __add__(self, autre_zoo):
        nouveaux_animaux = self.animaux + autre_zoo.animaux
        return Zoo(nouveaux_animaux)
    
    def __repr__(self):
        animal_list = ", ".join(str(animal) for animal in self.animaux)
        return f"Zoo({animal_list})"
