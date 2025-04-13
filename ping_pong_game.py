from pygame import *
from random import randint
from time import time as timer
w=display.set_mode((700,500))
display.set_caption('Пинг-Понг')
w.fill((200,255,255))
game=True
finish=False
clock=time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self,p_image,x,y,size_x,size_y,speed):
        sprite.Sprite.__init__(self)
        self.image=transform.scale(image.load(p_image),(size_x,size_y))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.speed=speed
    def reset(self):
        w.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y-=self.speed
        if keys[K_DOWN] and self.rect.y < 695:
            self.rect.y+=self.speed
    def update_l(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y-=self.speed
        if keys[K_s] and self.rect.y < 695:
            self.rect.y+=self.speed
l_player=Player('platform.jpg',50,200,10,100,10)
r_player=Player('platform.jpg',650,200,10,100,10)
ball=GameSprite('ball.png',350,250,60,60,15)
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if finish!=True:
        w.fill((200,255,255))
        l_player.reset()
        l_player.update_l()
        r_player.reset()
        r_player.update_r()
        ball.reset()
    display.update()
    clock.tick(30)
