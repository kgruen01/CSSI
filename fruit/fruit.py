class Fruit:
    name = ""
    poisonous = False

    def __init__(self, nameOfFruit, willIDie):
        self.name = nameOfFruit
        self.poisonous = willIDie

    def describe(self):
        print self.name


fruit1 = Fruit("Apple", True)

fruit2 = Fruit("Banana", False)

fruit1.describe()
fruit2.describe()
