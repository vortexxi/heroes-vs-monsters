import random
from models.modifier import Modifier
#dices
from models.dice import Dice
#monsters
from models.dragon import Dragon
from models.orc import Orc
from models.wolf import Wolf
#heroes
from models.human import Human
from models.dwarf import Dwarf

class Fight:
    def __init__(self):
        self.choise_hero = 0
        self.choise_monster = 0
        self.hero = 0
        self.monster = 0
        self.first_hit = 0
        self.hit = 0
        self.mod_force = 0
        self.next_fight = True
        self.first_health = 0

    ##### Set Monster

    def SetMonster(self):
        self.choise_monster = random.randint(1,3)
        
        if self.choise_monster == 1:
            print('You found a wolfe!')
            self.monster = Wolf(0,0)
            self.monster.CreateWolf()
            print(self.monster)
            #print('resistence wolf: ', self.resistence)

        elif self.choise_monster == 2:
            print('You found a orc!')
            self.monster = Orc(0,0)
            self.monster.CreateOrc()
            print(self.monster)

        else:
            print('You found a dragon!')
            self.monster = Dragon(0, 0)
            self.monster.CreateDragon()
            print(self.monster)

    #### Set Hero

    def Choise(self):
        
        self.choise_hero = int(input('1 to choose a human\n2 to choose a dwarf\n'))

        if self.choise_hero == 1:
            print('\nYou choose Human')
            self.hero = Human(0,0)
            self.hero.CreateHuman()
            #print(self.hero.__dict__)
            self.first_health = self.hero.health
            print(self.hero)
            #print('resistencia', self.hero.resistence)
        
  
        
        elif self.choise_hero == 2:
            print('\nYou choose Dwarf')
            self.hero = Dwarf(0,0)
            self.hero.CreateDwarf()
            # print(self.hero.__dict__)
            print(self.hero)
            self.first_health = self.hero.health

       
    
    #### Hits
    

    def Hit(self):
        while self.next_fight:
            self.first_hit = random.randint(0, 1)

            #FIRST HIT
            if self.first_hit == 0:
                print('Hero hit first!\n')
                self.hit = Dice(1,4)
                self.hit.throw()
                #print(self.hit.tab[0])
                self.monster.health = self.monster.health - self.hit.tab[0]
                self.mod_force = Modifier(self.monster.force)
                #self.monster.health = self.mod_force.UpdateValue()
                print('mod force: ', self.mod_force)
                print('monster health: ', self.monster.health)
                    

            else: 
                print('Monster hit first!\n')
                self.hit = Dice(1,4)
                self.hit.throw()
                #print(self.hit.tab[0])
                #self.mod_force = Modifier(self.hero.force)
                # self.hero = self.mod_force.UpdateValue()
                #print('mod force: ', self.mod_force)
                self.hero.health = self.hero.health - self.hit.tab[0]
                print('hero health: ', self.hero.health)
                
            #MORE HITS
            while self.hero.health > 0 and self.monster.health > 0:
                
                self.first_hit = random.randint(0, 1)

                if self.first_hit == 0:
                    self.hit = Dice(1,4)
                    self.hit.throw()
                    #print(self.hit.tab[0])
                    self.monster.health = self.monster.health - self.hit.tab[0]
                    #self.mod_force = Modifier(self.monster.force)
                    #self.monster.health = self.mod_force.UpdateValue()
                    #  print('mod force: ', self.mod_force)
                    print('Hero hit! \nmonster health:', self.monster.health)
                        

                elif self.first_hit == 1: 
                    self.hit = Dice(1,4)
                    self.hit.throw()
                    #print(self.hit.tab[0])
                    #self.mod_force = Modifier(self.hero.force)
                    # self.hero = self.mod_force.UpdateValue()
                    #print('mod force: ', self.mod_force)
                    self.hero.health = self.hero.health - self.hit.tab[0]
                    print('Monster hit! \nhero health:', self.hero.health)
                    

            if self.monster.health <= 0:
                self.hero.gold = self.monster.gold
                self.hero.leather = self.monster.leather
                print('YOU WIN!\n\n')
                print(self.hero)
                self.hero.health = self.first_health
                self.next_fight = input('Ready for de next? True/ False\n')
                self.SetMonster()



            elif self.hero.health <= 0:
                self.next_fight = False
                print('You are dead.')



# game = Fight()
# game.Choise()
# game.SetMonster()
# game.Hit()
        