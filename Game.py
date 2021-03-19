"""! @cyberPY Jogo cyberpunk 2D"""

##
# @file Game.py
#
# @brief Arquivo principal do jogo CyberPY
#
# @section Descrição
# O objetivo do jogo é alcançar o máximo de pontos possíveis.
# O jogador controla a personagem Viper que pode abaixar e pular 
# equanto segue correndo e desviando dos veículos para continuar viva.

import pygame

from random import randrange

# Classe que contém controles e informações personagem Viper
from Player import Player

# Classe do drone
from Drone import Drone

# Classe do veículo vermelho
from RedVehicle import RedVehicle

# Classe do veículo amarelo
from YellowVehicle import YellowVehicle

# Classe que controla o plano de fundo
from Ground import Ground

# Constantes usadas no jogo como velociade, altura etc.
from Configs import *

# inicialização do pygame
pygame.init()

# carregando a fonte para o score
font = pygame.font.SysFont("monospace", 16)
GREEN = (0,255,0)

# colocando uma música de fundo
pygame.mixer.music.load("./sounds/cyberpunk-street.ogg")
# o play(-1) serve para a música ficar em loop eterno
pygame.mixer.music.play(-1)
# configurando a tela do jogo
screen = pygame.display.set_mode(SCREEN_SIZE)

# o jogo contém três fundo
# cada fundo tem uma velocidade menor para dar impressão de movimento
bg_1_group = pygame.sprite.Group()
bg_2_group = pygame.sprite.Group()
bg_3_group = pygame.sprite.Group()

for i in range(2):
  # a imagem de cada fundo é carregada e adicionad em um grupo de sprites
  # elas são adicionadas duas vezes

  bg_1 = Ground("./layers/bg-1.png", BG_1_SPEED, i * SCREEN_WIDTH)
  bg_1_group.add(bg_1)
  
  bg_2 = Ground("./layers/bg-2.png", BG_2_SPEED, i * SCREEN_WIDTH)
  bg_2_group.add(bg_2)
  
  bg_3 = Ground("./layers/bg-3.png", BG_3_SPEED, i * SCREEN_WIDTH)
  bg_3_group.add(bg_3)

# instancia da personagem Viper
player = Player()
player_group = pygame.sprite.Group(player)

# o primeiro veículo é o vermelho
redVehicle = RedVehicle()

# enemy_group é o grupo de inimigos que podem colidir com a Viper
enemy_group = pygame.sprite.Group(redVehicle)

# clock do jogo
clock = pygame.time.Clock()

# essa função verifica se um sprite saiu da tela
def shouldKillSprite(sprite):
  return sprite.rect[0] < -(sprite.rect[2])

score = 0

while True:
  # quando um background sai da tela, removemos ele e adicionamos no final
  # dessa forma os prédios no fundo nunca deixam de aparecer 
  if shouldKillSprite(bg_1_group.sprites()[0]):
    bg_1_group.remove(bg_1_group.sprites()[0])
    new_ground = Ground("./layers/bg-1.png", BG_1_SPEED, SCREEN_WIDTH)
    bg_1_group.add(new_ground)
  
  if shouldKillSprite(bg_2_group.sprites()[0]):
    bg_2_group.remove(bg_2_group.sprites()[0])
    new_ground = Ground("./layers/bg-2.png", BG_2_SPEED, SCREEN_WIDTH)
    bg_2_group.add(new_ground)
  
  if shouldKillSprite(bg_3_group.sprites()[0]):
    bg_3_group.remove(bg_3_group.sprites()[0])
    new_ground = Ground("./layers/bg-3.png", BG_3_SPEED, SCREEN_WIDTH - (FPS/BG_3_SPEED))
    bg_3_group.add(new_ground)

  # se não houver inimigos na tela iremos adicionar um de forma aleatória
  if len(enemy_group.sprites()) == 0 or shouldKillSprite(enemy_group.sprites()[0]):
    if len(enemy_group.sprites()) > 0:
      enemy_group.remove(enemy_group.sprites()[0])
    
    # vamos usar um alcance de 0 a 30
    x = randrange(31)
    
    # para x entre 0 e 10 adicionaremos o veiculo vermelho
    if x <= 10 :
      newEnemy = RedVehicle()
    # para x entre 10 e 20 adicionaremos o veiculo amarelo
    elif x <= 20:
      newEnemy = YellowVehicle()
    # acima de 20 teremos um drone na tela
    else:
      newEnemy = Drone()  
    enemy_group.add(newEnemy)
  
  # atualizamos os backgrounds, player e inimigos
  bg_1_group.update()
  bg_2_group.update()
  bg_3_group.update()
  player_group.update()
  enemy_group.update()

  # desenhando todas as entidades na tela
  bg_1_group.draw(screen)
  bg_2_group.draw(screen)
  bg_3_group.draw(screen)
  player_group.draw(screen)
  enemy_group.draw(screen)
  
  # atualização do score
  scoretext = font.render(f"Score {score}", 1, GREEN)
  screen.blit(scoretext, (5, 10))
  score += 1

  # atualizando a tela
  pygame.display.update()
  clock.tick(FPS)

  # aqui é verificada se houve colisão entre dois grupos de sprites
  if pygame.sprite.groupcollide(player_group, enemy_group, False, False, pygame.sprite.collide_mask):
    # se colidirem o score volta a zero
    enemy_group.remove(enemy_group.sprites()[0])
    score = 0