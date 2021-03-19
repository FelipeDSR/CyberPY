"""! @cyberPY Jogo cyberpunk 2D"""

##
# @file Animation.py
#
# @brief Arquivo da classe de animações do jogo CyberPY

class Animation:
  def __init__(self, images, deltaTime=8):
    # imagens para a animação
    self.images = images
    # tempo que uma animação leva para ser completada
    self.timer = 0
    self.index = 0
    # imagem atual da animação
    self.image = self.images[self.index]
    self.deltaTime = deltaTime
    
  def update(self):
    # metodo de atualização onde a imagem atual é passado para a próxima
    self.timer += 1
    if self.timer % self.deltaTime == 0:
      if self.index < len(self.images) - 1:
        self.index += 1
      else:
        self.index = 0
    self.image = self.images[self.index]
