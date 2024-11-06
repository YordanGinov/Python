from project.animal import Animal


class Cat(Animal):
    def __init__(self):
        super().__init__()

    @staticmethod
    def meow():
        return 'meowing...'