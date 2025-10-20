from main import Car

#Submite to Judge

from unittest import TestCase, main

class CarTests(TestCase):
    def setUp(self):
        self.car = Car("testMake", "testModel", 2, 5)

    def test_init(self):
        c = Car("testMake", "testModel", 2, 5)
        self.assertEqual(c.make, "testMake")
        self.assertEqual(c.model, "testModel")
        self.assertEqual(c.fuel_consumption, 2)
        self.assertEqual(c.fuel_capacity, 5)
        self.assertEqual(c.fuel_amount, 0)

    def test_make_empty_string_raises(self):
        with self.assertRaises(Exception) as ex:
            c = Car("", "testModel", 2, 5)
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_model_empty_string_raises(self):
        with self.assertRaises(Exception) as ex:
            c = Car("testMake", "", 2, 5)
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_empty_string_raises(self):
        with self.assertRaises(Exception) as ex:
            c = Car("testMake", "testModel", 0, 5)
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            c = Car("testMake", "testModel", -1, 5)
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_empty_string_raises(self):
        with self.assertRaises(Exception) as ex:
            c = Car("testMake", "testModel", 2, 0)
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

        with self.assertRaises(Exception) as ex1:
            c = Car("testMake", "testModel", 2, -5)
        self.assertEqual(str(ex1.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_empty_string_raises(self):
        c = Car("testMake", "testModel", 2, 5)
        with self.assertRaises(Exception) as ex:
            c.fuel_amount = -1
        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

    def test_refuel_zero_or_negative_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            self.car.refuel(-2)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel(self):
        self.car.refuel(4)
        self.assertEqual(self.car.fuel_amount, 4)

        self.car.refuel(2)
        self.assertEqual(self.car.fuel_amount, 5)

    def test_drive_too_big_distance_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(700)
        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")

    def test_drive(self):
        self.car.refuel(5)
        self.car.drive(200)
        self.assertEqual(self.car.fuel_amount, 1)

if __name__ == '__main__':
    main()