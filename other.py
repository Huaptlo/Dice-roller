import random

class Dice():
    
    def __init__(self, amount):
        self.amount = amount    
    
    def d6():
        return random.randint(1,6)

