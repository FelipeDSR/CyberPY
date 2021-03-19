"""! @cyberPY Jogo cyberpunk 2D"""

##
# @file Ground.py
#
# @brief Arquivo da classe Ground
# @section Descrição
# Essa classe é responsável por movimentar cada um dos três backgrounds.

import pygame
from Configs import SCREEN_WIDTH, SCREEN_HEIGHT

class Ground(pygame.sprite.Sprite):
  def __init__(self, path, speed, xpos = 0):
    pygame.sprite.Sprite.__init__(self)
    # velocidade que ele se move
    self.speed = speed
    # imagem 
    self.image = pygame.image.load(path).convert_alpha()
    self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # rect é um atributo da classe Sprite do pygame que armazena 
    # referencia da posição de um sprite na tela e seu tamanho.
    self.rect = self.image.get_rect()
    self.rect[0] = xpos
    self.rect[1] = 0
  
  def update(self):
    # movimenta o fundo para trás (assim a Viper parece ir pra frente)
    self.rect[0] -= self.speed