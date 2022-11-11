#створи гру "Лабіринт"!
from telnetlib import GA
from tkinter import W
import pygame
import os
pygame.init()
pygame.font.init()

font = pygame.font.Font(None, 70)

PATH= os.path.dirname(__file__) + os.sep

'''-------------------------------------------------------------------------------------'''
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, w,h, x,y, speed):
        super().__init__()
        self.image = image
        self.w = w
        self.h = h 
        self.x = x
        self.y = y
        self.speed = speed
        self.sprite = ""
        self.rect = pygame.Rect(x,y, w,h)

    def create(self):
        self.sprite = pygame.transform.scale(pygame.image.load(self.image), (self.w, self.h))
    def show(self):
        wind.blit(self.sprite, (self.x, self.y))

class Hero(GameSprite):

    def __init__(self, image, w,h, x,y, speed):
        super().__init__(image, w,h, x,y, speed)

    def wasd(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] == True:
            self.x -= 10
        if keys[pygame.K_RIGHT] == True:
            self.x += 10
        if keys[pygame.K_DOWN] == True:
            self.y += 10
        if keys[pygame.K_UP] == True:
            self.y -= 10
        self.rect.x = self.x
        self.rect.y = self.y

class Cyborg(GameSprite):
    def __init__(self, image, w,h, x,y, speed):
        super().__init__(image, w,h, x,y, speed)
        self.burder_left = self.x - 120
        self.burder_right = self.x + 50
        self.diraction = 3
    def enemy_move(self):
        if self.x <= self.burder_left or self.x >= self.burder_right:
            self.diraction *= -1
        
        self.x += self.diraction

class Wall(GameSprite):
    def __init__(self, image, w,h, x,y, speed):
        super().__init__(image, w,h, x,y, speed)
        self.sprite = pygame.Surface((w,h))
        self.sprite.fill((250,249,0))
        self.image = self.sprite

    def draw_wall(self):
        wind.blit(self.sprite, (self.x, self.y))


'''-----------------------------------------------------------------------------------------------'''#rgb(250,249,0)
wind = pygame.display.set_mode((1000, 700))

bg = pygame.transform.scale(pygame.image.load(PATH + "background.jpg"),(1000,700))

you = Hero(PATH + "hero.png", 70,70, 10,300, 10)
you.create()

wall_1 = Wall('', 1000,10, 0, 0, 0)
wall_2 = Wall('', 10,700, 0,0, 0)
wall_3 = Wall('', 1000,10, 0, 690, 0)
wall_4 = Wall('', 10,700, 990,0, 0)
wall_5 = Wall('', 10, 600, 100, 0 ,0)
wall_6 = Wall('', 300, 300, 100, 0 ,0)
wall_7 = Wall('',300, 300, 300, 500 ,0)
wall_8 = Wall('',200, 600, 600, 100 ,0)

enemy = Cyborg(PATH + 'cyborg.png', 70,70, 880,400, 10)
enemy.create()

treasure = GameSprite(PATH+'treasure.png', 80, 80, 880, 580, 0)
treasure.create()
#pygame.mixer.music.load(PATH + 'jungles.ogg')
#pygame.mixer.music.play()

nice_cock = pygame.time.Clock()
game = True
while game:
    wind.blit(bg, (0,0))

    you.show()
    you.wasd()

    enemy.show()
    enemy.enemy_move()

    treasure.show()

    wall_1.draw_wall()
    wall_2.draw_wall()
    wall_3.draw_wall()
    wall_4.draw_wall()
    wall_5.draw_wall()
    wall_6.draw_wall()
    wall_7.draw_wall()
    wall_8.draw_wall()
    

    if pygame.sprite.collide_rect(you, wall_1):
        game = False
    if pygame.sprite.collide_rect(you, wall_2):
        game = False
    if pygame.sprite.collide_rect(you, wall_3):
        game = False
    if pygame.sprite.collide_rect(you, wall_4):
        game = False
    if pygame.sprite.collide_rect(you, wall_5):
        game = False
    if pygame.sprite.collide_rect(you, wall_6):
        game = False
    if pygame.sprite.collide_rect(you, wall_7):
        game = False
    if pygame.sprite.collide_rect(you, wall_8):
        game = False
    if pygame.sprite.collide_rect(you, treasure):
        win = pygame.font.render(
            "WIN!", True, (0, 255,0)
        )
    if pygame.sprite.collide_rect(you, enemy):
        game = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    nice_cock.tick(30)

    pygame.display.update()