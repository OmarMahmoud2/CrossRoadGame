from turtle import Screen
from Player import Player
from Cars import Cars
import time
from score import Level
import random

wn = Screen()
wn.setup(800, 500)
wn.title('CrossRoad')
wn.bgcolor('white')
wn.listen()
wn.tracer(0)

level = Level()


player = Player()
wn.onkey(player.move, 'Up')
wn.update()
game_is_on = True
level.upz()

army = []
while game_is_on:
  time.sleep(0.1)
  rand = random.randint(1, 6)
  if rand == 1 :
    army.append(Cars())
  wn.update()
  for turt in army:
    turt.attack()
    if turt.distance(player) < 20:
      level.over()
      game_is_on = False
    else:
      if player.ycor() >= 240:
        level.upz()
        player.repeat()
        turt.repeat()
    
    

  




