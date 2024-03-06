class Modifier:
    def __init__(self, points):
        self.points = points

    def UpdateValue(self):
        if self.points < 5:
            return self.points - 1
        elif self.points >= 5 and self.points < 10:
            return self.points
        elif self.points >= 10 and self.points < 15:
            return self.points + 1
        elif self.points >= 15:
            return self.points + 2
    def __str__(self) -> str:
        return f'{self.points}'

        
        