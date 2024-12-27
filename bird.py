import copy
from colors import colors

class Bird:
  """
  鸟头[(坐标),(激活颜色),(颜色)]：
    1. 可以检查4个方向都是什么
    2. 可以向合法的方向移动
    3. 可以被激活、反激活
    4. 可以检查指定方向是什么
    5. 可以吃水果
  鸟身[[(坐标)],[(激活颜色)],[(颜色)]]：
    1. 可以向上一个方块移动一格
    2. 可以被激活、反激活
    3. 可以检查其下方是否有支撑
    4. 可以检查指定方向是什么
    5. 吃水果时身体会增加
  鸟：
    1. 可以被推向指定方向
    2. 可以检查每一格下方是否有支撑
    3. 可以向下落
    4. 会被摔死
    5. 会被刺扎死
  """
  def __init__(self, color):
    self.color = color
    self.head = [(), colors[self.color+'_HEAD_ACTIVE'], colors[self.color+'_HEAD']] # 坐标，激活颜色，未激活颜色
    self.length = 0
    self.active = False
    self.body = [[],[],[]] # 坐标，激活颜色，未激活颜色

  def to_string(self):
    # print("name:", self.name)
    print("length:",self.length)
    print("head:", self.head)
    print("body:", self.body)

  def to_coodinates(self):
    coodinates = [copy.deepcopy(self.body[0], copy.deepcopy(self.body[1 if self.active else 2]))]
    coodinates[0].insert(0, self.head)
    coodinates[1].insert(0, self.head[1 if self.active else 2])
    return coodinates

  def set_head(self, position):
    """
    设置头的位置

    Args:
      position: 头的坐标。

    Returns：
      头身坐标二维列表
    """
    self.head[0] = [position]
  
  def add_body(self, position, number):
    """
    添加身体方块，增加长度

    Args:
      position: 身体方块的坐标。
      number: 身体方块的编号。

    Returns:
      头身坐标二维列表
    """
    print(number)
    print(number - self.length)
    print(number - self.length + 1)
    l = self.length
    for i in range(number - self.length + 1):
      print('a',self.body)
      self.body[0].append((0, 0))
      self.body[1].append((255, 255, 255))
      l += 1
    self.length = l
    print('b',self.body)
    self.body[0][number] = position

  def eat_fruit(self):
    """
    在身体列表最前端增加一个方块即原来头的位置。改变颜色分布。

    Args:
        a: 第一个加数。
        b: 第二个加数。

    Returns:
        两个数的和。
    """
    ...

  def move_body(self):
    """
    从尾部开始往前移。

    Args:
        a: 第一个加数。
        b: 第二个加数。

    Returns:
        两个数的和。
    """
    ...

  def drop(self):
    """
    坠落，所有身体向下移一格，然后重新检查站立位置

    Args:
        a: 第一个加数。
        b: 第二个加数。

    Returns:
        两个数的和。
    """
    ...

  def ending(self):
    """
    到达终点，一块一块进入。自动激活下一只鸟。

    Args:
        a: 第一个加数。
        b: 第二个加数。

    Returns:
        两个数的和。
    """
    ...

  def up(self):
    ...

  def down(self):
    ...

  def left(self):
    ...
  
  def right(self):
    ...

  def conflict(self):
    """
    检查移动是否合法。

    Args:

    Returns:
      移动是否有冲突
    """
    ...

  def active(self):
    """
    切换激活状态，并更改颜色。
    """
    active = not active
    ...

  def set_colors(length, color):
    """
      
    """
    colors = [color]
    if length > 2:
      divisor = length - 1
      last = (colors[0][0]>>1,colors[0][1]>>1,colors[0][2]>>1)
      for i in range(divisor - 1, -1, -1):
        colors.append((last[0] * i // divisor + last[0],
                      last[1] * i // divisor + last[1],
                      last[2] * i // divisor + last[2]))
      colors.append(last)
    return colors