from project.animals.birds import Owl, Hen
from project.animals.mammals import Tiger
from project.food import Meat, Vegetable, Fruit

hen = Hen("Harry", 10, 10)
tig = Tiger("Bard", 100, "Forest")
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)

