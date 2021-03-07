from Enemy import Enemy

class RedVehicle(Enemy):
  def __init__(self):
    super().__init__(
      path = "./vehicles/v-red.png",
      speed = 7,
      xpos = 20,
      ypos = 80,
      width = 150,
      height = 120
    )