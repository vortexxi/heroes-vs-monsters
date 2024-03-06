import random 
class Dice():
    def __init__(self, tryes, diceFaces):
        self.tryes = tryes
        self.diceFaces = diceFaces
        self.tab = []
       

            
    def throw(self):  
        for i in range(0,self.tryes,1):
            i = random.randint(1,self.diceFaces)
            self.tab.append(i)

        if len(self.tab) > 1:    
            minimum = min(self.tab)
            self.tab.remove(minimum)
        #print(self.tab)

if __name__ == "__main__":
    dado = Dice(4,6)
    dado.throw()
    print(dado.__dict__)