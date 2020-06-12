import pygame
import random
import cvetorial
from Food import *
from Mbee import *

WIDTH = 800
HEIGHT = 380
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255,128,0)
GRAY = (128,128,128)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Genetic Algoritm - RNBees")
clock = pygame.time.Clock()

def mundo(bee,foods,events):
    for food in foods:
        food.comportamento(events)
    bee.comportamento(events, foods)        
    foods.update()
    bee.update()
    resultante = (0,0)
    for food in foods:
        campo = cvetorial.campo(food.energia, food.pos, bee.pos)
        resultante = cvetorial.soma(resultante,campo)
        pygame.draw.aaline(screen, GRAY, bee.pos,  cvetorial.soma(bee.pos,campo))
    drawVector(screen, ORANGE, bee.pos, resultante)

def drawVector(surface, color, a, campo):
    pygame.draw.aaline(surface, color , a, cvetorial.soma(a,campo))

all_foods = pygame.sprite.Group()
all_mbees = pygame.sprite.Group()
 
for i in range(10):
    all_foods.add(Food());
bee = Mbee()
all_mbees.add(bee)

running = True
while running:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            running = False
    screen.fill(BLACK)
    mundo(bee, all_foods, events)
    all_foods.draw(screen)
    all_mbees.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
