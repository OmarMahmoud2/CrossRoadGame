from turtle import Turtle 

class Level(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.pencolor('black')
    self.goto(-390, 220)
    self.hideturtle()
    self.lev = 0 
    
  def upz(self):
    self.lev += 1
    self.clear()
    self.write(f'Level: {self.lev}', align = 'left', font =('Ariel', 13, 'normal'))
  def over(self):
    self.goto(0, 0)
    self.write('Game Over', align = 'center', font =('Ariel', 19, 'normal'))