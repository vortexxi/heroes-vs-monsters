#import Character class to assign resistence, force and health values
from models.character import Character
#import Dice class to assign a random gold and leather values
from models.dice import Dice


class Orc(Character):
    def __init__(self, gold, leather):
        '''The Orc class herits Character class parameters and has one self parameters: gold'''
        super().__init__()
        self.gold = gold
        self.leather = 0
        
    def CreateOrc(self):
        #call Character class
        orc = Character()
        orc.Resistence()
        orc.ForceHealth()
        self.force = orc.force + 1
        self.resistence = orc.resistence 
        self.health = orc.health

        #assign gold
        gold_points = Dice(1,6)
        gold_points.throw()
        self.gold = gold_points.tab[0]

    def __str__(self) -> str:
        return f'Resistence: {self.resistence}\nForce: {self.force}\nHealth: {self.health}\nGold: {self.gold}\nLeather: {self.leather}\n'

# orc = Orc(0)
# orc.CreateOrc()
# print(orc)





    
