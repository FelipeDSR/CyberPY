from Enemy import Enemy

class Drone(Enemy):
  def __init__(self):
    super().__init__(
      path = "./drone/drone.png",
      speed = 10,
      xpos = 20,
      ypos = 10,
      width = 80,
      height = 80
    )