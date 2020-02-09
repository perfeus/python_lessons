import pytest
from main import Food


class TestFood:

    def test_food(self):
        butter = Food(4, 2, 2)
        assert butter.energy_food() == 43.2

    def test_food_type(self):
        bread = Food(0, 0, 0)
        assert bread.energy_food() == 0

    def test_food_equal(self):
        apple = Food(34, 2, 11)
        assert apple.energy_food() != 3

    def test_food_double(self):
        nuts = Food(44, 93, 23)
        food = nuts * 2
        assert food.energy_food() != 0

    def test_energy(self):
        cabbage = Food(22, 92, 1)
        assert cabbage.energy_food() == 52