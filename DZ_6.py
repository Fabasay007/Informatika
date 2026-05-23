import pygame
import random
import math
from queue import PriorityQueue

# Инициализация Pygame
pygame.init()

# Константы
WIDTH = 600
GRID_SIZE = 10
CELL_SIZE = WIDTH // GRID_SIZE
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A*")

# Цвета
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# Типы ячеек
EMPTY = 0
OBSTACLE = 1
START = 2
END = 3
PATH = 4
VISITED = 5


class Cell:

    
    def __init__(self, row, col): # Конструктор клетки
        self.row = row # Номер строки
        self.col = col  # Номер столбца
        self.x = col * CELL_SIZE # Координата X на экране
        self.y = row * CELL_SIZE  # Координата Y на экране
        self.color = WHITE # Начальный цвет клетки
        self.neighbors = [] # Список соседних клеток

    
    def get_pos(self):  # Возвращает позицию клетки в сетке
        return self.row, self.col

    def is_closed(self):  # Проверка, является ли клетка закрытой
        return self.color == RED

    def is_open(self):  # Проверка, является ли клетка открытой
        return self.color == GREEN

    def is_barrier(self):  # Проверка, является ли клетка препятствием
        return self.color == BLACK

    def is_start(self):    # Проверка стартовой клетки
        return self.color == ORANGE

    def is_end(self):    # Проверка конечной клетки
        return self.color == TURQUOISE
    
    def reset(self):    # Сброс клетки в обычное состояние
        self.color = WHITE
  
    def make_start(self):    # Сделать клетку стартовой
        self.color = ORANGE
  
    def make_closed(self): # Сделать клетку закрытой
        self.color = RED

    def make_open(self):    # Сделать клетку открытой
        self.color = GREEN

    def make_barrier(self):    # Сделать клетку препятствием
        self.color = BLACK

    def make_end(self):     # Сделать клетку конечной
        self.color = TURQUOISE

    def make_path(self):     # Сделать клетку частью пути
        self.color = PURPLE
   
    def draw(self, win): # Отрисовка клетки на экране

        pygame.draw.rect(
            win,
            self.color,
            (self.x, self.y, CELL_SIZE, CELL_SIZE)
        )

    def update_neighbors(self, grid):
        self.neighbors = []

        # вниз
        if self.row < GRID_SIZE - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        # вверх
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        # вправо
        if self.col < GRID_SIZE - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        # влево
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])


# Создание двумерной сетки из клеток
def make_grid():

    grid = []
    for i in range(GRID_SIZE):
        grid.append([])  # Добавляем новую строку
        for j in range(GRID_SIZE):
            cell = Cell(i, j) # Создаем клетку
            grid[i].append(cell) # Добавляем клетку в строку
    return grid


def draw_grid(win, grid):
    for row in grid:
        for cell in row:
            cell.draw(win)

    # Рисуем сетку
    for i in range(GRID_SIZE):
        pygame.draw.line(win, GREY, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE))
        pygame.draw.line(win, GREY, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH))

    pygame.display.update()


def generate_random_grid(grid):
    # Очищаем сетку
    for row in grid:
        for cell in row:
            cell.reset()

    # Выбираем случайные начальную и конечную точки
    start_row, start_col = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
    end_row, end_col = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)

    # Убедимся, что начальная и конечная точки разные
    while (start_row, start_col) == (end_row, end_col):
        end_row, end_col = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)

    start = grid[start_row][start_col]
    end = grid[end_row][end_col]

    start.make_start()
    end.make_end()

    # Добавляем случайные препятствия 20%
    obstacle_count = int(GRID_SIZE * GRID_SIZE * 0.2)
    for _ in range(obstacle_count):
        row, col = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        cell = grid[row][col]

        if not cell.is_start() and not cell.is_end():
            cell.make_barrier()

    return start, end


def h(p1, p2):
    # Манхэттенское расстояние
    x1, y1 = p1
    x2, y2 = p2

    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def a_star_algorithm(draw, grid, start, end):
    count = 0

    open_set = PriorityQueue()
    open_set.put((0, count, start)) #Задание точки старта

    came_from = {}

    g_score = {}
    f_score = {}

    for row in grid: # Для кажкой клетки изначально задается значение бесконечность
        for cell in row:
            g_score[cell] = float("inf")
            f_score[cell] = float("inf")

    g_score[start] = 0     # Для стартовой клетки расстояние равно 0 
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start} # проверка, есть ли клетка уже в очереди

    while not open_set.empty():  # код работает пока есть клетки для проверки 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current) #Берётся клетка с наименьшим f_score и удаляется из множества открытых клеток

        if current == end: # Если клетка найдена, то финиш
            reconstruct_path(came_from, end, draw) # Восстанавливаем путь
            start.make_start()
            end.make_end()
            print("Путь найден")
            print("Длина пути:", g_score[end])
            return True

        for neighbor in current.neighbors: # Перебираются все соседние клетки текущей клетки
            temp_g_score = g_score[current] + 1 # Считается новая длина пути до соседа

            if temp_g_score < g_score[neighbor]: # Если находится путь кратче, то заменяем на него
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos()) # Сохраняем, откуда пришли, обновляем стоимость пути и общий приоритет

                if neighbor not in open_set_hash: # Проверяем, нет ли соседа уже в очереди.
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)  # Добавляем соседа в очередь с приоритетом.

                    if neighbor != end:
                        neighbor.make_open() # Окрашиваем соседа как открытую клетку

        draw()

        if current != start:
            current.make_closed() # После обработки клетка становится закрытой

    print("Путь не найден")
    return False



def load_my_matrix(grid):

    matrix = [
        [0,1,0,0,0,1,1,1,0,1],
        [1,1,1,1,1,0,1,1,0,0],
        [1,1,1,1,0,0,0,0,1,1],
        [0,1,1,0,1,0,0,1,1,1],
        [0,0,0,1,1,0,1,1,0,0],
        [1,1,0,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,0,0],
        [1,0,0,1,0,0,0,1,0,0],
        [0,0,0,0,0,1,0,1,0,1],
        [0,0,1,0,0,0,0,1,0,0]
    ]

    # очищаем поле
    for row in grid:
        for cell in row:
            cell.reset()

    # ставим препятствия
    for i in range(10):
        for j in range(10):

            if matrix[i][j] == 1:
                grid[i][j].make_barrier()

    # старт
    start = grid[8][0]
    start.make_start()

    # конец
    end = grid[9][9]
    end.make_end()

    return start, end

def main():

    grid = make_grid()

    # загружаем твою матрицу
    start, end = load_my_matrix(grid)

    run = True

    while run:

        draw_grid(WIN, grid)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            # SPACE запускает A*
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)

                    a_star_algorithm(
                        lambda: draw_grid(WIN, grid),
                        grid,
                        start,
                        end
                    )

                # R генерирует случайное поле
                if event.key == pygame.K_r:

                    start, end = generate_random_grid(grid)

    pygame.quit()


main()