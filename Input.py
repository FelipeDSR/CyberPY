"""! @cyberPY Jogo cyberpunk 2D"""

##
# @file Input.py
#
# @brief Arquivo da classe Input
# @section Descrição
# Essa classe é responsável por verificar todos comandos acionados pelo jogador.

import pygame
from pygame.locals import *
import sys

class Input:
  def __init__(self, entity):
    # é a entidade do jogador principal onde será possivel 
    # acionar métodos de gerenciamento de animações e ações. 
    self.entity = entity

  def checkForInput(self):
    # esse método verifica os eventos do teclado ou se o jogo, acabou ou reiniciou
    events = pygame.event.get()
    self.checkForKeyboardInput()
    self.checkForQuitAndRestartInputEvents(events)

  def checkForKeyboardInput(self):
    # verifica a tecla apetada
    pressedKeys = pygame.key.get_pressed()
    # abaixa
    if pressedKeys[K_DOWN] or pressedKeys[K_s] and not pressedKeys[K_SPACE]:
      self.entity.crouch()
    # pula
    elif pressedKeys[K_SPACE] and not pressedKeys[K_DOWN]:
      self.entity.jump()
    # corre (ação padrão no jogo)
    else:
      self.entity.run()

  def checkForQuitAndRestartInputEvents(self, events):
    # verifica se o jogo foi fechado
    for event in events:
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
