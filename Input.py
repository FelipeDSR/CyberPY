import pygame
from pygame.locals import *
import sys

class Input:
  """
    Essa classe gerencia todos os comandos acionados pelo jogador.

    Constructor:
      entity: é a entidade do jogador principal onde será possivel 
        acionar métodos de gerenciamento de animações e ações. 
        
        ex: quando o jogador aciona a seta para baixo o personagem abaixa
  """
  def __init__(self, entity):
    self.entity = entity

  def checkForInput(self):
    events = pygame.event.get()
    self.checkForKeyboardInput()
    self.checkForQuitAndRestartInputEvents(events)

  def checkForKeyboardInput(self):
    pressedKeys = pygame.key.get_pressed()
    if pressedKeys[K_DOWN] or pressedKeys[K_s] and not pressedKeys[K_SPACE]:
      self.entity.crouch()
    elif pressedKeys[K_SPACE] and not pressedKeys[K_DOWN]:
      self.entity.jump()
    else:
      self.entity.run()

  def checkForQuitAndRestartInputEvents(self, events):
    for event in events:
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
