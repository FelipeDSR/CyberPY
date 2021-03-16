import pygame

from random import randrange
from Player import Player
from Drone import Drone
from RedVehicle import RedVehicle
from YellowVehicle import YellowVehicle
from Ground import Ground
from Configs import *

pygame.init()
font = pygame.font.SysFont("monospace", 16)
GREEN = (0,255,0)

pygame.mixer.music.load("./sounds/cyberpunk-street.ogg")
pygame.mixer.music.play(-1)
screen = pygame.display.set_mode(SCREEN_SIZE)

bg_1_group = pygame.sprite.Group()
bg_2_group = pygame.sprite.Group()
bg_3_group = pygame.sprite.Group()

for i in range(2):
  bg_1 = Ground("./layers/bg-1.png", BG_1_SPEED, i * SCREEN_WIDTH)
  bg_1_group.add(bg_1)
  
  bg_2 = Ground("./layers/bg-2.png", BG_2_SPEED, i * SCREEN_WIDTH)
  bg_2_group.add(bg_2)
  
  bg_3 = Ground("./layers/bg-3.png", BG_3_SPEED, i * SCREEN_WIDTH)
  bg_3_group.add(bg_3)

player = Player()
player_group = pygame.sprite.Group(player)

redVehicle = RedVehicle()
enemy_group = pygame.sprite.Group(redVehicle)

clock = pygame.time.Clock()

def shouldKillSprite(sprite):
  return sprite.rect[0] < -(sprite.rect[2])

score = 0

while True:
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

  if len(enemy_group.sprites()) == 0 or shouldKillSprite(enemy_group.sprites()[0]):
    if len(enemy_group.sprites()) > 0:
      enemy_group.remove(enemy_group.sprites()[0])
    
    x = randrange(31)
    if x <= 10 :
      newEnemy = RedVehicle()
    elif x <= 20:
      newEnemy = YellowVehicle()
    else:
      newEnemy = Drone()  
    enemy_group.add(newEnemy)
  
  bg_1_group.update()
  bg_2_group.update()
  bg_3_group.update()
  player_group.update()
  enemy_group.update()

  bg_1_group.draw(screen)
  bg_2_group.draw(screen)
  bg_3_group.draw(screen)
  player_group.draw(screen)
  enemy_group.draw(screen)
  
  scoretext = font.render(f"Score {score}", 1, GREEN)
  screen.blit(scoretext, (5, 10))
  score += 1

  pygame.display.update()
  clock.tick(FPS)

  if pygame.sprite.groupcollide(player_group, enemy_group, False, False, pygame.sprite.collide_mask):
    enemy_group.remove(enemy_group.sprites()[0])
    score = 0