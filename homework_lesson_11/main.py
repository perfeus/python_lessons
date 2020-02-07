class Food:
    def __init__(self, proteins, carbs, fats):
        self.proteins = proteins
        self.carbs = carbs
        self.fats = fats
        self.elements = [proteins, carbs, fats]

    def __str__(self):
        return f"количество каллорий продукта: {self.energy_food()}"

    def __add__(self, other):
        return Food(self.proteins + other.proteins, self.carbs + other.carbs, \
                    self.fats + other.fats)

    def __mul__(self, other):
        return Food(self.proteins * other, self.carbs * other, self.fats * other)

    def __iadd__(self, other):
        return Food(self.proteins * other, self.carbs * other, self.fats * other)

    def __sub__(self, other):
        return self.energy_food() - other.energy_food()

    def __eq__(self, other):
        return self.energy_food() == other.energy_food()

    def __lt__(self, other):
        return self.energy_food() < other.energy_food()

    def __getitem__(self, item):
        return self.elements[item]

    def __len__(self):
        return len(self.elements)

    def __setitem__(self, key, value):
        return self.elements.append(value)

    def energy_food(self):
        return self.fats * 9 + (self.carbs + self.proteins) * 4.2


if __name__ == "__main__":
    apple = Food(4, 2, 28)
    milk = Food(47, 23, 2)
    print(apple < milk)
    print("the length of the object:", len(apple))
    apple[2] = 55
    print("the length of the object:", len(apple))
