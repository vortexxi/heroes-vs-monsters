from models.character import Character


class Dwarf(Character):
    def __init__(self, gold, leather):
        super().__init__()
        self.gold = gold
        self.leather = leather

    def CreateDwarf(self):
        dwarf = Character()
        dwarf.Resistence()
        dwarf.ForceHealth()
        self.force = dwarf.force
        self.resistence = dwarf.resistence + 2
        self.health = dwarf.health
        self.gold = 0
        self.leather = 0   

    def __str__(self) -> str:
        return f'Resistence: {self.resistence}\nForce: {self.force}\nHealth: {self.health}\nGold: {self.gold}\nLeather: {self.leather}\n'

# dwarf = Dwarf(0,0)
# dwarf.CreateDwarf()
# print(dwarf)




    
