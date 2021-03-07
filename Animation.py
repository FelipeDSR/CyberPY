class Animation:
  def __init__(self, images, deltaTime=8):
    self.images = images
    self.timer = 0
    self.index = 0
    self.image = self.images[self.index]
    self.deltaTime = deltaTime
    
  def update(self):
    self.timer += 1
    if self.timer % self.deltaTime == 0:
      if self.index < len(self.images) - 1:
        self.index += 1
      else:
        self.index = 0
    self.image = self.images[self.index]
