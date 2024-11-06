from project.car import Car


class SportsCar(Car):
    def __init__(self):
        super().__init__()

    @staticmethod
    def race():
        return "racing..."