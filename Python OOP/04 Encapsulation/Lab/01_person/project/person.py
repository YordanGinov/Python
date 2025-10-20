class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age


import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        p = Person("Alabala", 25)
        self.assertEqual(p._Person__name, "Alabala")
        self.assertEqual(p._Person__age, 25)

    def test_get_name(self):
        p = Person("X", 11)
        self.assertEqual(p.get_name(), "X")

    def test_get_age(self):
        p = Person("LA", 61)
        self.assertEqual(p.get_age(), 61)


if __name__ == "__main__":
    unittest.main()