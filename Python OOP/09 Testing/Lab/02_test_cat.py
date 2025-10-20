from unittest import TestCase, main


class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False

class CatTests(TestCase):
    def test_cat_size(self):
        c = Cat("Tom")
        self.assertEqual(c.size, 0)
        c.eat()
        result = c.size
        expected = 1
        self.assertEqual(result, expected)

    def test_cat_is_fed_after_feeding(self):
        c = Cat("Tom")
        self.assertEqual(c.fed, False)
        c.eat()
        result = c.fed
        expected = True
        self.assertEqual(result, expected)

    def test_cannot_eat_if_fed(self):
        c = Cat("Tom")
        self.assertEqual(c.fed, False)
        c.eat()
        with self.assertRaises(Exception) as context:
            c.eat()
        self.assertEqual(str(context.exception), "Already fed.")

    def test_cannot_sleep_if_fed(self):
        c = Cat("Tom")
        self.assertEqual(c.fed, False)
        with self.assertRaises(Exception) as context:
            c.sleep()
        self.assertEqual(str(context.exception), "Cannot sleep while hungry")

    def test_cat_not_sleepy(self):
        c = Cat("Tom")
        self.assertEqual(c.sleepy, False)
        c.eat()
        self.assertEqual(c.sleepy, True)
        c.sleep()
        self.assertEqual(c.sleepy, False)


if __name__ == '__main__':
    main()