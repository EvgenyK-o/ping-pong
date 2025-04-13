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
        if keys[K_DOWN] and self.rect.y < 395:
            self.rect.y+=self.speed
    def update_l(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y-=self.speed
        if keys[K_s] and self.rect.y < 395:
            self.rect.y+=self.speed
l_player=Player('platform.jpg',50,200,10,100,8)
r_player=Player('platform.jpg',650,200,10,100,8)
ball=GameSprite('ball.png',350,250,60,60,15)
step_x=5
step_y=5
font.init()
font1=font.Font(None,70)
fail_1=font1.render('Player 1 lost',True,(180,0,0))
fail_2=font1.render('Player 2 lost',True,(180,0,0))


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
        ball.rect.y+=step_y
        ball.rect.x+=step_x
        if ball.rect.y>440 or ball.rect.y<0:
            step_y*=-1
        if sprite.collide_rect(ball, r_player) or sprite.collide_rect(ball, l_player):
            step_x*=-1
        if ball.rect.x<0:
            w.blit(fail_1,(200,220))
            finish=True
        if ball.rect.x>700:
            w.blit(fail_2,(200,220))
            finish=True
        
    else:
        finish=False
        time.delay(2000)
        l_player.rect.x,l_player.rect.y=50,200
        r_player.rect.x,r_player.rect.y=650,200
        ball.rect.x,ball.rect.y=350,250
        step_x=5
        step_y=5
    display.update()
    clock.tick(35)
