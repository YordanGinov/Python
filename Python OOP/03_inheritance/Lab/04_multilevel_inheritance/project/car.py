from project.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self):
        super().__init__()

    @staticmethod
    def drive():
        return "driving..."