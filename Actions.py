"""! @cyberPY Jogo cyberpunk 2D"""

##
# @file Actions.py
#
# @brief Arquivo da classe de ações da personagem Viper

import pygame 
from os import listdir
from Animation import Animation
from Configs import PLAYER_SIZE

class Actions:
  def __init__(self):
    # basicamente todos as animações são carregadas
    self.run = Animation(self.loadSprites("./player/run/"))
    self.jump = Animation(self.loadSprites("./player/jump/"))
    self.crouch = Animation(self.loadSprites("./player/crouch/"))
    self.hurt = Animation(self.loadSprites("./player/hurt/"))
    
  def loadSprites(self, path):
    # carrega as imagens em um diretório especifico
    files = listdir(path)
    images = [pygame.image.load(path + file).convert_alpha() for file in files]
    images = [pygame.transform.scale(image, PLAYER_SIZE) for image in images]
    
    return images