import unittest
from main import Food


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, False)

    def setUp(self):
        print("start test")
        self.butter = Food(4, 2, 1)

    def tearDown(self):
        print("test completed")

    def test_food(self):
        self.assertEqual(self.butter.energy_food(), 32)

    def test_food_type(self):
        self.assertFalse(self.butter.energy_food() > 10)

    def test_food_equal(self):
        self.assertEqual(self.butter.energy_food(), 34.2)

    def test_energy(self):
        self.assertFalse(self.butter.energy_food() == 0)


if __name__ == '__main__':
    unittest.main()
