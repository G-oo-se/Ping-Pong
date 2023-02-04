from pygame import *
from time import sleep
from random import randint

dx = 3
dy = 3
bck = 'background2.png'
font.init()
font = font.Font(None, 35)
win = font.render('Player 1 WIN!!', True, (0, 0, 255))
win2 = font.render('Player 2 WIN!!', True, (255, 0, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, pc, speed, x, y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(pc), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        wd.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 360:
            self.rect.y += self.speed
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 360:
            self.rect.y += self.speed



player1 = Player('pl1.png', 15, 50, 200, 30, 140)
player2 = Player2('pl2.png', 15, 615, 200, 30, 140)
ball = Player('bl2.png', 10, 250, 200, 50, 50)

pl1sc = 0
pl2sc = 0

WIDTH = 700
HEIGHT = 500
FPS = 60
clock = time.Clock()

wd = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Ping Pong')
back = transform.scale(image.load(bck), (WIDTH, HEIGHT))

sleep(2)
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    wd.blit(back, (0,0))
    player1.reset()
    player1.update()
    player2.reset()
    player2.update()
    ball.reset()
    score_game = font.render(str(pl1sc)+' - '+ str(pl2sc), True, (0, 0, 0))
    wd.blit(score_game, (350, 100))
    
    ball.rect.x += dx
    ball.rect.y += dy

    if ball.rect.y < 0 or ball.rect.y > 450:
        dy *= -1
    if sprite.collide_rect(ball ,player2):
        dx = randint(-12, -5)
        dy *= 1
    if sprite.collide_rect(ball, player1):
        dx = randint(5, 12)
        dy *= 1
    if ball.rect.x < 0:
        pl2sc += 1
        if pl2sc >= 3:
            wd.blit(win2, (250, 250))
        else:
            ball.rect.x = 250
            ball.rect.y = 200
            dx = 3
            dy = 3
    if ball.rect.x > 700:
        pl1sc += 1
        if pl1sc >= 3:
            wd.blit(win, (250, 250))
        else:
            ball.rect.x = 250
            ball.rect.y = 200
            dx = 3
            dy = 3

    clock.tick(FPS)
    display.update()
