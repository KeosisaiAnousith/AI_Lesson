import pygame
import math
import random
from queue import PriorityQueue

# Initialize Pygame
pygame.init()

GRID_WIDTH = 600     # Chiều rộng của lưới game (đơn vị: pixel)
GRID_HEIGHT = 600    # Chiều cao của lưới game (đơn vị: pixel)
BUTTON_HEIGHT = 50   # Chiều cao của nút bấm (đơn vị: pixel)
ROWS = 20            # Số hàng trong lưới
COLS = 20            # Số cột trong lưới

# Tính toán kích thước của mỗi ô trong lưới
CELL_WIDTH = GRID_WIDTH // COLS    # Độ rộng của mỗi ô = Tổng chiều rộng / Số cột
CELL_HEIGHT = GRID_HEIGHT // ROWS  # Chiều cao của mỗi ô = Tổng chiều cao / Số hàng

# Window size
WIDTH = GRID_WIDTH
HEIGHT = GRID_HEIGHT + BUTTON_HEIGHT

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
GREY = (128, 128, 128)
BUTTON_COLOR = (220, 220, 220)
BUTTON_HOVER_COLOR = (200, 200, 200)

class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.f = float('inf')
        self.g = float('inf')
        self.h = 0
        self.blocked = False
        self.neighbors = []
        self.previous = None
        self.visited = False
        self.in_openset = False
    
    def show(self, screen, color=None):
        if color:
            fill_color = color
        else:
            fill_color = BLACK if self.blocked else WHITE
            
        rect = pygame.Rect(self.i * CELL_WIDTH, self.j * CELL_HEIGHT, 
                          CELL_WIDTH, CELL_HEIGHT)
        pygame.draw.rect(screen, fill_color, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)
    
    def add_neighbors(self, grid):
        self.neighbors = []
        if self.i < COLS - 1:
            self.neighbors.append(grid[self.i + 1][self.j])
        if self.i > 0:
            self.neighbors.append(grid[self.i - 1][self.j])
        if self.j < ROWS - 1:
            self.neighbors.append(grid[self.i][self.j + 1])
        if self.j > 0:
            self.neighbors.append(grid[self.i][self.j - 1])

def h_score(a, b):
    return abs(a.i - b.i) + abs(a.j - b.j)

class PathFinder:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("A* Path Finding")
        
        self.initialize_grid()
        
        # Font for button
        self.font = pygame.font.Font(None, 32)
        button_width = 300
        button_height = 40
        button_x = (WIDTH - button_width) // 2
        button_y = GRID_HEIGHT + (BUTTON_HEIGHT - button_height) // 2
        self.button_rect = pygame.Rect(button_x, button_y, button_width, 
                                        button_height)
        
        # Path finding state
        self.is_searching = False
        self.has_path = False
        self.needs_update = False
        
    def initialize_grid(self):
        # Initialize grid
        self.grid = [[Cell(i, j) for j in range(ROWS)] for i in range(COLS)]
        
        # Add random walls
        for i in range(COLS):
            for j in range(ROWS):
                if random.random() < 0.2:
                    self.grid[i][j].blocked = True
        
        # Setup neighbors
        for i in range(COLS):
            for j in range(ROWS):
                self.grid[i][j].add_neighbors(self.grid)
        
        # Start and end points
        self.start = self.grid[0][0]
        self.end = self.grid[COLS-1][ROWS-1]
        self.start.blocked = False
        self.end.blocked = False
        
        # Initialize path finding variables
        self.open_set = []
        self.closed_set = []
        self.path = []
        
    def draw_button(self):
        pygame.draw.rect(self.screen, WHITE, (0, GRID_HEIGHT, WIDTH, 
                                                BUTTON_HEIGHT))
        pygame.draw.rect(self.screen, BUTTON_COLOR, self.button_rect)
        pygame.draw.rect(self.screen, BLACK, self.button_rect, 2)
        text = self.font.render("Click To Find Shortest Path", True, BLACK)
        text_rect = text.get_rect(center=self.button_rect.center)
        self.screen.blit(text, text_rect)
        
    def get_clicked_cell(self, pos):
        x, y = pos
        if y < GRID_HEIGHT:
            i = x // CELL_WIDTH
            j = y // CELL_HEIGHT
            if 0 <= i < COLS and 0 <= j < ROWS:
                return self.grid[i][j]
        return None
        
    def draw(self):
        self.screen.fill(WHITE)
        
        # Draw all cells
        for i in range(COLS):
            for j in range(ROWS):
                self.grid[i][j].show(self.screen)
        
        # Draw closed set (red)
        for cell in self.closed_set:
            cell.show(self.screen, RED)
        
        # Draw current examining cells (green)
        for cell in self.open_set:
            cell.show(self.screen, GREEN)
        
        # Draw path (blue)
        for cell in self.path:
            cell.show(self.screen, BLUE)
            
        # Draw start and end
        self.start.show(self.screen, PURPLE)
        self.end.show(self.screen, GREY)
        
        # Draw button
        self.draw_button()
        
        pygame.display.flip()
    
    def reset_path(self):
        self.open_set = []
        self.closed_set = []
        self.path = []
        self.has_path = False
        for row in self.grid:
            for cell in row:
                cell.f = float('inf')
                cell.g = float('inf')
                cell.h = 0
                cell.previous = None
    
    def find_path(self):
        self.reset_path()
        self.is_searching = True
        
        self.start.g = 0
        self.start.f = h_score(self.start, self.end)
        self.open_set = [self.start]
        
        while self.open_set and self.is_searching:
            current = min(self.open_set, key=lambda x: x.f)
            
            if current == self.end:
                self.path = []
                temp = current
                while temp.previous:
                    self.path.append(temp)
                    temp = temp.previous
                self.has_path = True
                self.is_searching = False
                return True
            
            self.open_set.remove(current)
            self.closed_set.append(current)
            
            for neighbor in current.neighbors:
                if neighbor in self.closed_set or neighbor.blocked:
                    continue
                
                temp_g = current.g + 1
                
                if neighbor not in self.open_set:
                    self.open_set.append(neighbor)
                elif temp_g >= neighbor.g:
                    continue
                
                neighbor.previous = current
                neighbor.g = temp_g
                neighbor.h = h_score(neighbor, self.end)
                neighbor.f = neighbor.g + neighbor.h
            
            self.draw()
            pygame.time.wait(50)
        
        return False
    
    def run(self):
        running = True
        mouse_pressed = False
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if y < GRID_HEIGHT:  # Click trong grid
                        mouse_pressed = True
                        cell = self.get_clicked_cell((x, y))
                        if cell and cell != self.start and cell != self.end:
                            cell.blocked = not cell.blocked
                            self.needs_update = True # Đánh dấu cầntìmlạiđườngđi
                            self.reset_path()  # Reset đường đi cũ khi cóthayđổi
                    elif self.button_rect.collidepoint(x, y):  # Click vào nút
                        self.find_path()
                
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_pressed = False
                
                elif event.type == pygame.MOUSEMOTION and mouse_pressed:
                    x, y = pygame.mouse.get_pos()
                    cell = self.get_clicked_cell((x, y))
                    if cell and cell != self.start and cell != self.end:
                        cell.blocked = True
                        self.needs_update = True  # Đánh dấu cần tìm lại đườngđi
                        self.reset_path()  # Reset đường đi cũ khi có thay đổi
            
            self.draw()
            
        pygame.quit()

if __name__ == "__main__":
    finder = PathFinder()
    finder.run()