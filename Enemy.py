"""! @cyberPY Jogo cyberpunk 2D"""

##
# @file Enemy.py
#
# @brief Arquivo da classe Enemy

import pygame
from Configs import SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
  def __init__(self, path, speed, xpos, ypos, width, height):
    super(Enemy, self).__init__()
    # é a imagem do veículo, o convert_aplha() do pygame remove toda a parte 
    # transparente em volta da imagem, então a máscara dela será fiel ao contorno 
    # do veículo e não um block retangular.
    self.image = pygame.image.load(path).convert_alpha()
    self.image = pygame.transform.scale(self.image, (width, height))

    # é feita uma máscara em cima da imagem PNG do veículo onde todos os pixels 
    # do veiculo servirão para detectar colisões.
    self.mask = pygame.mask.from_surface(self.image)
    
    # é um atributo da classe Sprite do pygame para ter referência de posição e 
    # tamanho do objeto na tela.
    self.rect = self.image.get_rect()
    self.rect[0] = SCREEN_WIDTH + width + xpos
    self.rect[1] = SCREEN_HEIGHT - height - ypos
    # Velocidade do inimigo
    self.speed = speed

  def update(self):
    """
    Esse método: atualiza a posição horizontal do veículo (o que faz ele se mover em direção ao player).
    """
    self.rect[0] -= self.speed
