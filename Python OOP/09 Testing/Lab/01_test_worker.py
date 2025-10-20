from unittest import TestCase, main


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class TestWorker(TestCase):
    def setUp(self):
        self.worker = Worker("Test", 1000, 0)

    def test_worker_init(self):

        self.assertEqual(self.worker.name, 'Test')
        self.assertEqual(self.worker.salary, 1000)
        self.assertEqual(self.worker.energy, 0)
        self.assertEqual(self.worker.money, 0)

    def test_worker_energy_increment(self):
        self.worker.rest()

        self.assertEqual(self.worker.energy, 1)

    def test_worker_work_with_no_energy(self):
        with self.assertRaises(Exception) as exception:
            result = self.worker.work()
        self.assertEqual(self.worker.money, 0)
        self.assertEqual(str(exception.exception), "Not enough energy.")
        self.assertEqual(self.worker.energy, 0)

    def test_worker_money_increment(self):
        w = Worker("Test", 1000, 500)
        self.assertEqual(w.money, 0)
        self.assertEqual(w.energy, 500)

        result = w.work()
        self.assertEqual(w.money, 1000)
        self.assertEqual(w.energy, 499)

        self.assertIsNone(result)

    def test_worker_get_info(self):
        result = self.worker.get_info()
        expected = "Test has saved 0 money."
        self.assertEqual(result, expected)

if __name__ == '__main__':
    main()