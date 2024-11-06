from animal import Animal
from mammal import Mammal
from reptile import Reptile
from bear import Bear
from gorilla import Gorilla
from snake import Snake
from lizard import Lizard

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)

