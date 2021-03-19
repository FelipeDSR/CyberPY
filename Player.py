"""! @cyberPY Jogo cyberpunk 2D"""

##
# @file Player.py
#
# @brief Arquivo da classe Player
# @section Descrição
# Essa classe é provavelmente a mais importante.
# Ela é responsavel por acionar as ações da Viper, verificar os inputs do jogo

import pygame
from Input import Input
from Actions import Actions
from Configs import *

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super(Player, self).__init__()
    # Instancia da classe Input
    self.input = Input(self)
    # diz se a Viper esta no ar (caindo)
    self.inAir = False
    # armazena as animações da Viper
    self.actions = Actions()
    # a animação atual
    self.currentAction = self.actions.run
    # a imagem da animação atual
    self.image = self.currentAction.image
    # mascara de colisão da imagem atual
    self.mask = pygame.mask.from_surface(self.image)
    # armazena posição na tela e tamanho de um sprite
    self.rect = self.image.get_rect()
    self.rect[0] = SCREEN_WIDTH / 2  - PLAYER_WIDTH
    self.rect[1] = FLOOR
    # velocidade vertical
    self.speedy = 0
    # gravidade
    self.gravity = 1

  def update(self):
    # é como a gravidade, ela ta sempre excencendo uma força
    # para a viper não cair no limbo a velocidade Y se torna zero quando atinge o chão
    self.rect[1] += self.speedy
    
    # verifica se a Viper não está tocando o chão
    if self.rect[1] < FLOOR:
      # se sim ela está no Ar e a gravidade é exercida sobre ela
      self.inAir = True
      self.speedy += self.gravity
    else:
      # se não ela não está no ar e ela para de cair
      self.inAir = False
      self.speedy = 0

    # atualiza a animação atual
    self.currentAction.update()
    # verifica inputs
    self.input.checkForInput()
    # atualiza a imagem atual da Viper
    self.image = self.currentAction.image
    # atualiza a mascara para colisão da Viper (importante porque a 
    # área de contato dela pode mudar depenndendo da ação dela)
    self.mask = pygame.mask.from_surface(self.image)

  def run(self):
    # muda a animação atual para "correndo" se ela nao estiver no ar
    if not self.inAir:
      self.currentAction = self.actions.run

  def jump(self):
    # muda a animação atual para "pulando" se ela nao estiver no ar
    # evita que ela de dois saltos no ar
    if not self.inAir:
      self.currentAction = self.actions.jump
      self.speedy = -15
  
  def crouch(self):
    # muda a animação atual para "abaixada" se ela nao estiver no ar
    if not self.inAir:
      self.currentAction = self.actions.crouch