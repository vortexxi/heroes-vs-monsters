from models.character import Character
from models.dice import Dice


class Wolf(Character):
    def __init__(self, leather, gold):
        super().__init__()
        self.leather = leather
        self.gold = 0

    def CreateWolf(self):
        wolf = Character()
        wolf.Resistence()
        wolf.ForceHealth()
        self.force = wolf.force
        self.resistence = wolf.resistence
        self.health = wolf.health
        leather_points = Dice(1,4)  
        leather_points.throw()
        self.leather = leather_points.tab[0]

    def __str__(self):
        return f'Resistence: {self.resistence}\nForce: {self.force}\nHealth: {self.health}\nGold: {self.gold}\nLeather: {self.leather}\n'

if __name__ == "__main__":
    wolf = Wolf(0,0)
    wolf.CreateWolf()
    print(wolf)




    
