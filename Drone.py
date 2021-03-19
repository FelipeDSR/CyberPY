"""! @cyberPY Jogo cyberpunk 2D"""

##
# @file Drone.py
#
# @brief Arquivo da classe do inimigo Drone

from Enemy import Enemy

class Drone(Enemy):
  """
    Essa classe extende a classe Enemy e simplesmente invoca
    o construtor passando seus atributos padrões, é mais para 
    facilitar na hora de instanciar um novo objeto.
  """
  def __init__(self):
    super().__init__(
      path = "./drone/drone.png",
      speed = 10,
      xpos = 20,
      ypos = 10,
      width = 80,
      height = 80
    )