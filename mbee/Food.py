import pygame, math, sys, os, random

WIDTH = 1200
HEIGHT = 700
FPS = 30
NOVO = 0
JOVEM = 1
MADURO = 2

def loadImage(fileName, useColorKey=False):
    if os.path.isfile(fileName):
        image = pygame.image.load(fileName)
        #image = image.convert_alpha()
        # Return the image
        return image
    else:
        raise Exception("Error loading image: " + fileName + " - Check filename and path?")


image1 = loadImage("food1.png")
image2 = loadImage("food2.png")
image3 = loadImage("food3.png")


class Food(pygame.sprite.Sprite):
    def __init__(self, energia=0):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(image1)
        self.images.append(image2)
        self.images.append(image3)
        self.image = pygame.Surface.copy(self.images[0])
        self.currentImage = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.originalWidth = self.rect.width
        self.originalHeight = self.rect.height
        self.indexns = 0
        self.itera = 0
        self.estado = JOVEM
        self.energia = energia
        self.t =0

    def comportamento(self,events):
        self.t = self.t + 1
        if self.energia < 100:
            self.energia = self.energia + (5 + random.randint(0, 5))/(1.*FPS)

    def update(self):
        if self.energia < 20 :  self.image = self.images[0]
        elif self.energia < 70 :  self.image = self.images[1]
        else:  self.image = self.images[2]
        self.changeImage(self.indexns)
        self.move( self.pos[0], self.pos[1])
       
    def addImage(self, filename):
        self.images.append(loadImage(filename))
        print(self.images)

    def move(self, xpos, ypos, centre=True):
        if centre:
            self.rect.center = [xpos, ypos]
        else:
            self.rect.topleft = [xpos, ypos]

    def changeImage(self, index):
        oldcenter = self.rect.center
        self.rect = self.image.get_rect()
        self.originalWidth = self.rect.width
        self.originalHeight = self.rect.height
        self.rect.center = oldcenter
        self.mask = pygame.mask.from_surface(self.image)


