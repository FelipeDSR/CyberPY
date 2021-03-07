import pygame
from Configs import SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
  def __init__(self, path, speed, xpos, ypos, width, height):
    super(Enemy, self).__init__()
    self.image = pygame.image.load(path).convert_alpha()
    self.image = pygame.transform.scale(self.image, (width, height))
    self.mask = pygame.mask.from_surface(self.image)
    self.rect = self.image.get_rect()
    self.rect[0] = SCREEN_WIDTH + width + xpos
    self.rect[1] = SCREEN_HEIGHT - height - ypos
    self.speed = speed

  def update(self):
    self.rect[0] -= self.speed
