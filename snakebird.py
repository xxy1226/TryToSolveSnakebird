import os
import pygame
import maze

FILES_PER_ROW = 5
COLOR_WALL = (139,69,19)
COLOR_AIR = (135,206,235)
COLOR_THORN = (192,192,192)
COLOR_END_ACTIVE = (255,255,255)
COLOR_END = (111,111,111)
COLOR_PORTAL = (200,100,100)
COLOR_FRUIT = (255,165,0)

COLOR_RBIRD_HEAD_ACTIVE = (200, 50, 50)
COLOR_RBIRD_ACTIVE = (170, 40, 40)
COLOR_RBIRD_HEAD = (140, 30, 30)
COLOR_RBIRD = (110,20,20)

COLOR_GBIRD_HEAD_ACTIVE = (50, 200, 50)
COLOR_GBIRD_ACTIVE = (40, 170, 40)
COLOR_GBIRD_HEAD = (30, 140, 30)
COLOR_GBIRD = (20, 110, 20)

COLOR_BBIRD_HEAD_ACTIVE = (50, 50, 200)
COLOR_BBIRD_ACTIVE = (40, 40, 170)
COLOR_BBIRD_HEAD = (30, 30, 140)
COLOR_BBIRD = (20, 20, 110)

COLOR_YBIRD_HEAD_ACTIVE = (200, 200, 50)
COLOR_YBIRD_ACTIVE = (170, 170, 40)
COLOR_YBIRD_HEAD = (140, 140, 30)
COLOR_YBIRD = (110,110,20)

COLOR_PBIRD_HEAD_ACTIVE = (150, 50, 150)
COLOR_PBIRD_ACTIVE = (130, 40, 130)
COLOR_PBIRD_HEAD = (110, 30, 110)
COLOR_PBIRD = (90, 20, 90)


# init
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("蛇鸟")

# fonts
font_title = pygame.font.Font(None, 72)
font_file = pygame.font.Font(None, 36)

def get_maze_files():
  maze_files = []
  for file in os.listdir("maze"):
    if file.endswith(".txt"):
      maze_files.append(file[:-4])
  return maze_files

def draw_file_list(files, selected_row, selected_col):
  y = 150
  for row in range(len(files)):
    x = 50
    for col in range(len(files[row])):
      text = font_file.render(files[row][col], True, (255, 255, 255))
      if row == selected_row and col == selected_col:
        pygame.draw.rect(screen, (0, 255, 0), (x-5, y - 5, text.get_width() + 10, text.get_height() + 10), 2)
      screen.blit(text, (x, y))
      x += 150
    y += 100

def load_maze_from_file(filename):
  with open(filename, 'r') as f:
    lines = f.readlines()
    row_count, col_count = map(int, lines[0].strip().split(','))
    maze_data = []
    for line in lines[1:]:
      maze_data.append(list(line))
  return row_count, col_count, maze_data

def draw_playmaze(screen, playmaze):
  for row in range(playmaze.rows):
    for col in range(playmaze.cols):
      print("Row:", row, "Col", col)
      print(playmaze.data)
      if playmaze.data[row][col] == ' ':
        color = COLOR_AIR
      elif playmaze.data[row][col] == 'x':
        color = COLOR_WALL
      cell_size = 20
      pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

# main loop
running = True
maze_files = get_maze_files()

rows, remainder = divmod(len(maze_files), FILES_PER_ROW)
if remainder:
    rows += 1
files_2d = [maze_files[i:i+FILES_PER_ROW] for i in range(0, len(maze_files), FILES_PER_ROW)]

selected_row = 0
selected_col = 0

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP or event.key == pygame.K_w:
        selected_row = max(0, selected_row - 1)
      elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        selected_row = min(rows - 1, selected_row + 1)
      elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        selected_col = max(0, selected_col - 1)
      elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        selected_col = min(len(files_2d[selected_row]) - 1, selected_col + 1)
      elif event.key == pygame.K_RETURN:
        filename = f"maze/{maze_files[5 * selected_row + selected_col]}.txt"
        rows, cols, maze_data = load_maze_from_file(filename)
        playmaze = maze.Maze(rows, cols, maze_data)
        draw_playmaze(screen, playmaze)
        pygame.display.flip()

  screen.fill((0, 0, 0)) 

  # title
  text_surface = font_title.render("Snakebird", True, (255, 255, 255))
  text_rect = text_surface.get_rect(center=(400, 80))
  screen.blit(text_surface, text_rect)
  
  # file list
  draw_file_list(files_2d, selected_row, selected_col)  
  
  pygame.display.flip()

pygame.quit()