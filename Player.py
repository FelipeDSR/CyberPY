import pygame
from Input import Input
from Actions import Actions
from Configs import *

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super(Player, self).__init__()
    self.input = Input(self)
    self.inAir = False
    self.actions = Actions()
    self.currentAction = self.actions.run
    self.image = self.currentAction.image
    self.mask = pygame.mask.from_surface(self.image)
    self.rect = self.image.get_rect()
    self.rect[0] = SCREEN_WIDTH / 2  - PLAYER_WIDTH
    self.rect[1] = FLOOR
    self.speedy = 0
    self.gravity = 1

  def update(self):
    self.rect[1] += self.speedy
    
    if self.rect[1] < FLOOR:
      self.inAir = True
      self.speedy += self.gravity
    else:
      self.inAir = False
      self.speedy = 0

    self.currentAction.update()
    self.input.checkForInput()
    self.image = self.currentAction.image
    self.mask = pygame.mask.from_surface(self.image)

  def run(self):
    if not self.inAir:
      self.currentAction = self.actions.run

  def jump(self):
    if not self.inAir:
      self.currentAction = self.actions.jump
      self.speedy = -15
  
  def crouch(self):
    if not self.inAir:
      self.currentAction = self.actions.crouch