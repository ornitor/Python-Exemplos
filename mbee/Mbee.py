import pygame, math, sys, os, random
import cvetorial
from Food import * 


FPS = 30
NOVO = 0
JOVEM = 1
MADURO = 2

newfood_event = pygame.USEREVENT + 1

def loadImage(fileName, useColorKey=False):
    if os.path.isfile(fileName):
        image = pygame.image.load(fileName)
        #image = image.convert_alpha()
        # Return the image
        return image
    else:
        raise Exception("Error loading image: " + fileName + " - Check filename and path?")


mbeeimg1 = loadImage("mbee1.png")
mbeeimg2 = loadImage("mbee2.png")
mbeeimg3 = loadImage("mbee3.png")


class Mbee(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(mbeeimg1)
        self.images.append(mbeeimg2)
        self.images.append(mbeeimg3)
        self.image = pygame.Surface.copy(self.images[0])
        self.currentImage = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = (0.0 + random.randint(0, WIDTH), 0.0+random.randint(0,HEIGHT))
        self.originalWidth = self.rect.width
        self.originalHeight = self.rect.height
        self.indexns = 0
        self.itera = 0
        self.estado = JOVEM
        self.energia = 50
        self.t =0
        self.M = 10
        self.B = 0.2
        self.vel = (0.,0.)
        #print(self.pos)

    def comportamento(self,events,foods):
        f = self.gradiente(foods)
        acel = cvetorial.soma (cvetorial.mux(1/self.M,f), cvetorial.mux(-self.B/self.M, self.vel))
        self.vel = cvetorial.integral(acel,self.vel,1./FPS)
        self.pos = cvetorial.integral(self.vel,self.pos,1./FPS)
        self.t = self.t + 1
        self.energia = self.energia - (5 + random.randint(0, 5))/(10.*FPS)
        #self.pos = (self.pos[0] + 4. - random.randint(0, 8), self.pos[1] + 4. - random.randint(0, 8))
        #self.pos = (self.pos[0] + f[0]*random.randint(0, 1000)/100000., self.pos[1] + f[1]*random.randint(0,1000)/100000.)

    def gradiente(self,foods):
        resultante = (0,0)
        for food in foods:
            if food.energia > 20:
                campo = cvetorial.campo(food.energia, food.pos, self.pos)
                resultante = cvetorial.soma(resultante,campo)
                if cvetorial.distancia(self.pos,food.pos)< 5:
                    self.energia = self.energia + food.energia
                    foods.remove(food)
                    pygame.event.post(pygame.event.Event(newfood_event,{'a': "a" * 1024}))
                    #pygame.time.set_timer(newfood_event, 1000)
                    return (0,0)
        return resultante

    def update(self):
        if self.energia < 20 :  self.image = self.images[0]
        elif self.energia < 80 :  self.image = self.images[1]
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


