class Fruit:
  """
  水果可以被鸟吃
  """
  def __init__(self, center):
    self.center = center

  def eaten(self, bird):
    ...

class Portal:
  """
  传送门可以将鸟传送至另一个门
  """
  def __init__(self, center1):
    self.center1 = center1
    self.center2 = (0, 0)
  def set_pos2(self, center2):
    self.center2 = center2
  def teleport(self, bird):
    ...

class EndPoint:
  """
  终点可以被激活
  """
  def __init__(self, center, status=False):
    self.center = center
    self.status = status
  def activate(self):
    self.status = not self.status

class BoxRod:
  """
  箱杆拥有数个方格，可以被移动，移动钱检查冲突
  """
  def add_block(self, type, pos, center):
    ...