from models.character import Character


class Human(Character):
    def __init__(self, gold, leather):
        super().__init__()
        self.gold = gold
        self.leather = leather

    def CreateHuman(self):
        human = Character()
        human.Resistence()
        human.ForceHealth()
        self.force = human.force + 1
        self.resistence = human.resistence + 1
        self.health = human.health
        self.gold = 0
        self.leather = 0   

    def __str__(self) -> str:
        return f'Resistence: {self.resistence}\nForce: {self.force}\nHealth: {self.health}\nGold: {self.gold}\nLeather: {self.leather}\n'

# humano = Human(0,0)
# humano.CreateHuman()
# print(humano)




    
