class Maze:
  def __init__(self, rows, cols, data):
    self.rows = rows
    self.cols = cols
    self.data = data
  
  def print_maze(self):
    for row in self.data:
      print(''.join(row))