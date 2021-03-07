import pygame
from Configs import SCREEN_WIDTH, SCREEN_HEIGHT

class Ground(pygame.sprite.Sprite):
  def __init__(self, path, speed, xpos = 0):
    pygame.sprite.Sprite.__init__(self)
    self.speed = speed
    self.image = pygame.image.load(path).convert_alpha()
    self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    self.rect = self.image.get_rect()
    self.rect[0] = xpos
    self.rect[1] = 0
  
  def update(self):
    self.rect[0] -= self.speed