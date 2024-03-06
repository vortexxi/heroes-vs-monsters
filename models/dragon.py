#import Character class to assign resistence, force and health values
from models.character import Character
#import Dice class to assign a random gold and leather values
from models.dice import Dice


class Dragon(Character):
    def __init__(self, gold, leather):
        '''The Dragon class herits Character class parameters and has two self parameters: gold and leather'''
        super().__init__()
        self.gold = gold
        self.leather = leather

    def CreateDragon(self):
        #call Character class
        dragon = Character()
        dragon.Resistence()
        dragon.ForceHealth()
        self.force = dragon.force
        self.resistence = dragon.resistence + 1
        self.health = dragon.health

        #assign leather
        leather_points = Dice(1,4)  
        leather_points.throw()
        self.leather = leather_points.tab[0]

        #assign gold
        gold_points = Dice(1,6)
        gold_points.throw()
        self.gold = gold_points.tab[0]

    def __str__(self) -> str:
        return f'Resistence: {self.resistence}\nForce: {self.force}\nHealth: {self.health}\nGold: {self.gold}\nLeather: {self.leather}\n'

# dragon = Dragon(0, 0)
# dragon.CreateDragon()
# print(dragon)





    
