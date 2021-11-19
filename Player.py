from turtle import Turtle

class Player(Turtle):
  
  def __init__(self):
    super().__init__()
    self.shape('turtle')
    self.shapesize(1, 0.7)
    self.color('black')
    self.penup()
    self.goto(0, -230)
    self.setheading(90)
    
  def move(self):
    if self.ycor() <= 240:
      self.forward(20)
    else:
      pass
 
  def repeat(self):
    self.goto(0, -230)
    self.setheading(90)