import pygame
from pygame.draw import *
pygame.init()
screen = pygame.display.set_mode((1000,800))

def get_yahta():
    x = -75
    y = -150
    surface = pygame.Surface((150, 175), pygame.SRCALPHA, 32)
    rect(surface, (255, 255, 255), (x+100, y+300, 100, 25))
    polygon(surface, (255, 255, 255), [(x+100,y+300), (x+75,y+300), (x+100,y+324)])
    polygon(surface, (255, 255, 255), [(x+225,y+300), (x+200,y+300), (x+200,y+324)])
    rect(surface, (255, 255, 255), (x+149, y+150, 2, 150))
    polygon(surface, (255, 255, 255), [(x+145,y+160), (x+100,y+290), (x+145,y+290)])
    polygon(surface, (255, 255, 255), [(x+155,y+150), (x+155,y+290), (x+212,y+290)])
    return surface

def get_seagull():
    s = pygame.Surface((175, 125), pygame.SRCALPHA, 32)
    #верхние круги
    circle(s, (240, 255, 255), (50, 100), 50)
    circle(s, (240, 255, 255), (125,100), 50)
    #нижние (ограничивающие) круги
    circle(s, (255, 255, 255,0), (50, 125), 60)
    circle(s, (255, 255, 255,0), (125, 125), 60)
    return s

Seagull = get_seagull()
Yahta = get_yahta()

def draw_image(screen, image, x, y, w, h, angle):
    s = pygame.transform.scale(image, (w, h))
    s = pygame.transform.rotate(s, angle)   #поворот на угол 60 градусов
    screen.blit(s, (x-s.get_size()[0], y - s.get_size()[1]))
    
screen.fill("#AFEEEE")
circle(screen, ("#FFFACD"), (500, 400), 100)
rect(screen, ("#87CEEB"), (0,400,1000,400))  
line(screen,(255, 255, 0), (500, 350), (500, 300))            

draw_image(screen, Yahta, 150, 600, 100, 100, 0)
draw_image(screen, Yahta, 500, 700, 100, 100, 0)
draw_image(screen, Yahta, 750, 500, 150, 150, 0)
draw_image(screen, Seagull, 300,300, 100, 50, -15)
draw_image(screen, Seagull, 300,370, 80, 35, 15)
draw_image(screen, Seagull, 650, 200, 110, 60, 20)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()