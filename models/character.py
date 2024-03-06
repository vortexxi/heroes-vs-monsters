from models.dice import Dice
from models.modifier import Modifier

class Character():
    def __init__(self):
        self.__resistence = 0
        self.__force = 0
        self.__health = 0

    #resistence
    @property
    def resistence(self):
        return self.__resistence

    @resistence.setter
    def resistence(self, value):
        self.__resistence = value 
    
    #force
    @property
    def force(self):
        return self.__force 

    @force.setter
    def force(self, value):
        self.__force = value

    #health
    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    def Resistence(self):
        resistence_array = Dice(4,6)
        resistence_array.throw()
        # self.__resistence = resistence_array.tab[0]
        #print('array resistencia: ', resistence_array)
        for i in range(len(resistence_array.tab)):
            self.__resistence += resistence_array.tab[i]      

    def ForceHealth(self):
        force_array = Dice(4,6)
        force_array.throw()
        # self.__resistence = resistence_array.tab[0]
        # print('resistence: ', self.__resistence)
        for i in range(len(force_array.tab)):
            self.__force += force_array.tab[i]      
        #print('fuerza: ', self.__force)
        mod = Modifier(self.__force)
        self.__health = mod.UpdateValue()
        #print('salud: ', self.__health)
        
        

  
        

    
    #to string
    def __str__(self) -> str:
        return f'Resistence: {self.__resistence}\nForce: {self.__force}\nHealth: {self.__health}'




# char = Character()
# char.Resistence()
# char.ForceHealth()
# print(char)