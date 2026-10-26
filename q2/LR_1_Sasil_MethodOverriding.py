class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, end=" ")

    def make_sound(self):
        print(self.name, end=" ")


class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        super().eat()
        print("eats fresh meat.")

    def make_sound(self):
        super().make_sound()
        print("roars loudly.")


class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        super().eat()
        print("eats grass and fruits.")

    def make_sound(self):
        super().make_sound()
        print("trumpets.")


class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        super().eat()
        print("eats bananas.")

    def make_sound(self):
        super().make_sound()
        print("chatters.")


animals = [
    Lion("Simba"),
    Elephant("Dumbo"),
    Monkey("George")
]

for animal in animals:  
    animal.make_sound()
    animal.eat()
    print("-" * 30)