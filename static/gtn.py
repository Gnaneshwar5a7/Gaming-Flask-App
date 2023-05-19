from random import *
class gtn:
    def __init__(self):
        self.number= randint(1,100)
        self.count=0

    def score(self):
        if self.count<=7:
            return 100
        elif self.count<=10:
            return 50
        return 0
    
    def isWinner(self,n):
        self.count+=1
        if self.number>n:
            return -1
        elif self.number<n:
            return 1
        return self.score()
    
    
