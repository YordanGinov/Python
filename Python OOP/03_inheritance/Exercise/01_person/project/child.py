from project.person import Person


class Child(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
