from turtle import Turtle 
import random 

carz = [i for i in range(-200, 220, 40)]
sped = 5

class Cars(Turtle):

  def __init__(self):
    super().__init__()
    self.shape('square')
    self.color(random.choice(['red', 'green', 'blue', 'yellow', 'purple', 'gold']))
    self.penup()
    self.shapesize(0.6, 2)
    self.setpos(310, random.choice(carz))
    self.dist = sped
  
  def attack(self):
    self.backward(self.dist)
    
    
  def repeat(self):
    global sped
    sped += 5 
    
    
    
    