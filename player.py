import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos , group):
        super().__init__(group)
        # general setup
        self.image = pygame.Surface((64, 32))
        self.image.fill("green")
        self.rect = self.image.get_rect(center = pos)
        
        # movement variables
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 100
        self.pos = pygame.math.Vector2(self.rect.center)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.direction.x = 0    
        
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = +1
        else:
            self.direction.y = 0
    def move(self,dt):
        self.pos += self.direction * dt * self.speed
        self.rect.center = self.pos
    
    def update(self,dt):
        self.input()
        self.move(dt)