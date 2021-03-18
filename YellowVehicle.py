from Enemy import Enemy

class YellowVehicle(Enemy):
  """
    Essa classe extende a classe Enemy e simplesmente invoca
    o construtor passando seus atributos padrões, é mais para 
    facilitar na hora de instanciar um novo objeto.
  """
  def __init__(self):
    super().__init__(
      path = "./vehicles/v-yellow.png",
      speed = 8,
      xpos = 20,
      ypos = 80,
      width = 80,
      height = 80
    )