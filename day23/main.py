import time
from turtle import Turtle,Screen

from player import Player

screen =Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
player=Player()
screen.onkeypress(player.move_up,'Up')
screen.onkeypress(player.move_left,'Left')
screen.onkeypress(player.move_right,'Right')
screen.listen()
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()