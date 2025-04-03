from pygame import *
from random import randint
from time import time as timer
w=display.set_mode((700,500))
display.set_caption('Пинг-Понг')
w.fill((200,255,255))
game=True
finish=False

while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    display.update()
    time.delay(50)