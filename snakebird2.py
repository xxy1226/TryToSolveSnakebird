import os
import pygame
import maze
from colors import colors
from bird import Bird

GRID_WIDTH = 40

FILES_PER_ROW = 5

# init
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("")
# pygame.display.set_caption("蛇鸟")
clock = pygame.time.Clock()
FPS = 1

# variables
welcome = True
base_folder = os.path.dirname(__file__)
birds_name = []
birds = {}

# fonts
font_name = os.path.join(base_folder, '方圆体.ttc')
font_title = pygame.font.Font(font_name, 72)
font_file = pygame.font.Font(font_name, 36)

def get_maze_files():
  maze_files = []
  for file in os.listdir("maze"):
    if file.endswith(".txt"):
      maze_files.append(file[:-4])
  return maze_files

def draw_file_list(files, selected_row, selected_col):
  y = 200
  for row in range(len(files)):
    x = 50
    for col in range(len(files[row])):
      text = font_file.render(files[row][col], True, (255, 255, 255))
      if row == selected_row and col == selected_col:
        pygame.draw.rect(screen, (0, 255, 0), (x - 5, y - 5, text.get_width() + 10, text.get_height() + 10), 2)
      screen.blit(text, (x, y))
      x += 150
    y += 100

def show_text(screen, font, text, x, y, color=(255, 255, 255)):
  text_surface = font.render(text, True, color)
  text_rect = text_surface.get_rect()
  text_rect.midtop = (x, y)
  screen.blit(text_surface, text_rect)

def show_welcome(screen, files_2d, selected_row, selected_col):
  show_text(screen, font_title, u'蛇鸟', 400, 80)
  draw_file_list(files_2d, selected_row, selected_col)

def load_maze_from_file(filename):
  with open(filename, 'r') as f:
    lines = f.readlines()
    row_count, col_count = map(int, lines[0].strip().split(','))
    maze_data = []
    for line in lines[1:]:
      maze_data.append(list(line))
    for i in range(len(maze_data)):
      for j in range(len(maze_data[i])):
        if maze_data[i][j] in ['r', 'R', 'b', 'B', 'y', 'Y', 'g', 'G', 'p', 'P']:
          name = maze_data[i][j]
          if name.upper() not in birds_name:
            birds_name.append(name.upper())
            bird = Bird(name.upper())
            birds[name.upper()] = bird
          else:
            bird = birds[name.upper()]
          if name.islower():
            bird.add_body((i, j), int(maze_data[i][j+1]))
          else:
            bird.set_head((i, j))
          maze_data[i][j], maze_data[i][j+1] = ' ', ' '
          ...
    print(birds[birds_name[0]].to_string())
  return row_count, col_count, maze_data

def draw_matrix(screen, rows, cols, matrix):
  for i, row in zip(range(rows), matrix):
    for j, code in zip(range(cols), row):
      if type(code) == str:
        color = colors[code]
      else:
        color = code
      if color is not None:
        # print('position:',i,',',j,'color:',color)
        pygame.draw.rect(screen, color, (j * GRID_WIDTH, i * GRID_WIDTH, GRID_WIDTH, GRID_WIDTH))
        if code  == '@@':
          show_text(screen, font_file, code[0], j * GRID_WIDTH + GRID_WIDTH // 2, i * GRID_WIDTH + 2 )
        elif code == 'oo':
          show_text(screen, font_file, code[0], j * GRID_WIDTH + GRID_WIDTH // 2, i * GRID_WIDTH )
        elif code == '^^':
          show_text(screen, font_file, code[0], j * GRID_WIDTH + GRID_WIDTH // 2, i * GRID_WIDTH + GRID_WIDTH // 2)
        elif code == '**':
          show_text(screen, font_file, code[0], j * GRID_WIDTH + GRID_WIDTH // 2, i * GRID_WIDTH + GRID_WIDTH // 4)
      

running = True
maze_files = get_maze_files()

rows, remainder = divmod(len(maze_files), FILES_PER_ROW)
if remainder:
  rows += 1
files_2d = [maze_files[i:i+FILES_PER_ROW] for i in range(0, len(maze_files), FILES_PER_ROW)]

selected_row, selected_col = 0, 0
count = 0
while running:
  clock.tick(FPS)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if welcome:
        if event.key == pygame.K_RETURN:
          filename = f"maze/{maze_files[5 * selected_row + selected_col]}.txt"
          rows, cols, maze_data = load_maze_from_file(filename)
          screen = pygame.display.set_mode((cols * GRID_WIDTH, rows * GRID_WIDTH + 30 + GRID_WIDTH))
          matrix = [[None] * cols for i in range(rows)]
          for row in range(rows):
            for col in range(cols):
              matrix[row][col] = maze_data[row][2*col]+maze_data[row][2*col+1]
          welcome = False
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
          selected_row = max(0, selected_row - 1)
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
          selected_row = min(rows - 1, selected_row + 1)
          selected_col = min(selected_col, len(files_2d[selected_row]) - 1)
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
          selected_col -= 1
          if selected_col < 0:
            selected_col = len(files_2d[selected_row]) - 1
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
          selected_col += 1
          if selected_col > len(files_2d[selected_row]) -1:
            selected_col = 0
        # continue
      else:
        pass


  screen.fill((0, 0, 0))
  if welcome:
    show_welcome(screen, files_2d, selected_row, selected_col)
  else:
    draw_matrix(screen, rows, cols, matrix)
  pygame.display.update()

        