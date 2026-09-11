class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def take_damage(self, amount):
        self.hp -= amount
Arthur = Hero("Arthur", 100)
Morgana = Hero("Morgana", 100)
Arthur.take_damage(10)
print(Arthur.hp)
print(Morgana.hp)
