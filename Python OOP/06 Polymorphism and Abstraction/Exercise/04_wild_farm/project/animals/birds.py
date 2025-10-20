from project.animals.animal import Bird
from project.food import Seed, Meat, Vegetable, Fruit


class Owl(Bird):
    @property
    def allowed_food(self):
        return [Meat]

    @property
    def weight_increase(self):
        return 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    @property
    def allowed_food(self):
        return [Meat, Seed, Vegetable, Fruit]

    @property
    def weight_increase(self):
        return 0.35

    @staticmethod
    def make_sound():
        return "Cluck"

