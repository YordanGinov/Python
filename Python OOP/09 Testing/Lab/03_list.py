from main import IntegerList

#Submittion to Judge

from unittest import TestCase, main

class IntegerListTestCase(TestCase):
    def setUp(self):
        self.integet_list = IntegerList(4, -5, 100, -95)

    def test_init_stores_only_int(self):
        #No args

        i = IntegerList()
        self.assertEqual(i._IntegerList__data, [])

        #With args
        i = IntegerList(1, "str", 9.5, [1, 2, 3])
        self.assertEqual(i._IntegerList__data, [1])

    def test_get_data(self):
        result = self.integet_list.get_data()

        expected = [4, -5, 100, -95]

        self.assertEqual(expected, result)

    def test_add_not_integer_raises(self):
        result = self.integet_list.get_data()
        expected = [4, -5, 100, -95]
        self.assertEqual(expected, result)

        with self.assertRaises(ValueError) as ex:
            self.integet_list.add('zdr')
        self.assertEqual(str(ex.exception), "Element is not Integer")
        self.assertEqual(expected, result)

    def test_add(self):
        result = self.integet_list.get_data()
        expected = [4, -5, 100, -95]
        self.assertEqual(expected, result)

        result = self.integet_list.add(6)
        expected = [4, -5, 100, -95, 6]
        self.assertEqual(expected, result)

        result= self.integet_list.get_data()
        self.assertEqual(expected, result)
        self.assertEqual(self.integet_list._IntegerList__data, expected)

    def test_remove_index_invalid_index_raises(self):
        self.assertEqual(len(self.integet_list.get_data()), 4)

        with self.assertRaises(IndexError) as ex:
            self.integet_list.remove_index(4)

        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.integet_list.get_data()), 4)

        with self.assertRaises(IndexError) as ex:
            self.integet_list.remove_index(7)

        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.integet_list.get_data()), 4)

    def test_remove_index(self):
        self.assertEqual(len(self.integet_list.get_data()), 4)
        self.assertEqual(self.integet_list.get_data()[2], 100)

        self.integet_list.remove_index(2)
        self.assertEqual(len(self.integet_list.get_data()), 3)
        self.assertEqual(self.integet_list.get_data()[2], -95)

    def test_get_invalid_index(self):
        self.assertEqual(len(self.integet_list.get_data()), 4)

        with self.assertRaises(IndexError) as ex:
            self.integet_list.get(4)
        self.assertEqual(str(ex.exception), "Index is out of range")

        with self.assertRaises(IndexError) as ex:
            self.integet_list.get(5)
        self.assertEqual(str(ex.exception), "Index is out of range")


    def test_index(self):
        self.assertEqual(self.integet_list.get(2), 100)

    def test_insert_invalid_index(self):
        self.assertEqual(len(self.integet_list.get_data()), 4)

        with self.assertRaises(IndexError) as ex:
            self.integet_list.insert(4, -1)

        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.integet_list.get_data()), 4)

        with self.assertRaises(IndexError) as ex:
            self.integet_list.insert(7, -1)
        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.integet_list.get_data()), 4)

    def test_insert_invalid_data(self):
        self.assertEqual(len(self.integet_list.get_data()), 4)

        with self.assertRaises(ValueError) as ex:
            self.integet_list.insert(2, "zdr")

        self.assertEqual(str(ex.exception), "Element is not Integer")
        self.assertEqual(len(self.integet_list.get_data()), 4)

    def test_insert(self):
        self.assertEqual(len(self.integet_list.get_data()), 4)

        self.integet_list.insert(2, -1)

        self.assertEqual(len(self.integet_list.get_data()), 5)
        self.assertEqual(self.integet_list.get(2), -1)

    def test_biggest(self):
        result = self.integet_list.get_biggest()
        expected = 100
        self.assertEqual(expected, result)

    def test_get_index(self):
        result = self.integet_list.get_index(100)
        expected = 2
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()