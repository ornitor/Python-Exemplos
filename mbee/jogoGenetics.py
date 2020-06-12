import pygame
import random
import cvetorial
from Food import *
from Mbee import *

FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255,128,0)
GRAY = (128,128,128)

newfood_event = pygame.USEREVENT + 1

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Artificial World - RNBees")
clock = pygame.time.Clock()

def mundo(bees,foods,events):
    for food in foods:
        food.comportamento(events)
    for mbee in bees:
        mbee.comportamento(events,foods)
        if mbee.energia < 0:
            bees.remove(mbee)          
    foods.update()
    bees.update()

def drawVector(surface, color, a, campo):
    pygame.draw.aaline(surface, color , a, cvetorial.soma(a,campo))

all_foods = pygame.sprite.Group()
all_mbees = pygame.sprite.Group()

for i in range(20):
    all_foods.add(Food(20));
for i in range(80):
    all_mbees.add(Mbee());


running = True
while running:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == newfood_event:
            all_foods.add(Food())
    mundo(all_mbees, all_foods, events)
    screen.fill(BLACK)
    all_foods.draw(screen)
    all_mbees.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
