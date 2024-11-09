import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)

        #general setup
        self.image = pygame.Surface((64,32))
        self.image.fill("red")
        self.rect=self.image.get_rect(center = pos)
        #movements attributes
        self.direction = pygame

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            print("UP") 
        elif keys[pygame.K_DOWN]:
            print("DOWN") 
        elif keys[pygame.K_RIGHT]:
            print("RIGHT") 
        elif keys[pygame.K_LEFT]:
            print("LEFT") 

    def update(self,dt):
        self.input()