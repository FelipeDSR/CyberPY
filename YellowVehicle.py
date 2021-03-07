from Enemy import Enemy

class YellowVehicle(Enemy):
  def __init__(self):
    super().__init__(
      path = "./vehicles/v-yellow.png",
      speed = 8,
      xpos = 20,
      ypos = 80,
      width = 80,
      height = 80
    )