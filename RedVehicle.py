from Enemy import Enemy

class RedVehicle(Enemy):
  """
    Essa classe extende a classe Enemy e simplesmente invoca
    o construtor passando seus atributos padrões, é mais para 
    facilitar na hora de instanciar um novo objeto.
  """
  def __init__(self):
    super().__init__(
      path = "./vehicles/v-red.png",
      speed = 7,
      xpos = 20,
      ypos = 80,
      width = 150,
      height = 120
    )