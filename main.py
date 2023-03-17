from animal import Animal
from oiseau import Oiseau
from serpent import Serpent
from zoo import Zoo


pie= Oiseau(1,15,50,"pie")
moineau=Oiseau(0.5,5,25,"moineau")
couleuvre=Serpent(1,30,"couleuvre")
boa=Serpent(3,150,"boa")


liste_oiseau=[pie,moineau]
liste_serpent =[couleuvre,boa]   

zoo_serpent= Zoo(liste_serpent)   
zoo_oiseau=Zoo(liste_oiseau)

gros_zoo=zoo_serpent+zoo_oiseau

print(repr(gros_zoo))
print(pie)

