import pygame
from Configs import SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
  def __init__(self, path, speed, xpos, ypos, width, height):
    """
    Essa classe representa a estrutura de qualquer inimigo no jogo.

    É necessário usar todos os parâmetros do seu método construtor.

    Constructor:
      path: Um argumento obrigatório com o caminho para a imagem da entidade.
      speed: A velocidade da entidade em direção ao Player.
      xpos: A posição inicial do veículo em relação ao eixo X.
      ypos: A posição do veículo no eixo Y (a altura de voo do veículo).
      width:  A largura do veículo.
      height: A altura do veículo.

    Atritutes:
      image: é a imagem do veículo, o convert_aplha() do pygame remove toda a parte 
        transparente em volta da imagem, então a máscara dela será fiel ao contorno 
        do veículo e não um block retangular.
      
      mask: é feita uma máscara em cima da imagem PNG do veículo onde todos os pixels 
        do veiculo servirão para detectar colisões. 

      rect: é um atributo da classe Sprite do pygame para ter referência de posição e 
        tamanho do objeto na tela.
    """
    super(Enemy, self).__init__()
    self.image = pygame.image.load(path).convert_alpha()
    self.image = pygame.transform.scale(self.image, (width, height))
    self.mask = pygame.mask.from_surface(self.image)
    self.rect = self.image.get_rect()
    self.rect[0] = SCREEN_WIDTH + width + xpos
    self.rect[1] = SCREEN_HEIGHT - height - ypos
    self.speed = speed

  def update(self):
    """
    Esse método: atualiza a posição horizontal do veículo (o que faz ele se mover em direção ao player).
    """
    self.rect[0] -= self.speed
