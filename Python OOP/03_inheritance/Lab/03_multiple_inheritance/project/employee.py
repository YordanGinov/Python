from project.person import Person


class Employee(Person):
    @staticmethod
    def get_fired():
        return "fired..."