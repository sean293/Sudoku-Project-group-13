import pygame
from constants import *
from cell import Cell
from sudoku_generator import *
import sys
import copy

"""
Note:
Many of the functions in this class are either incomplete, unused, or implemented incorrectly. This class needs more work
"""


class Board:
    """
    Constructor for the Board class.
    screen is a window from PyGame.
    difficulty is a variable to indicate if the user chose easy, medium, or hard.
    """

    def __init__(self, width, height, screen, difficulty):
        self.reset_rectangle = None  # need to put rectangle variables in initializer to use them in the main method
        self.restart_rectangle = None
        self.exit_rectangle = None
        self.width = width
        self.height = height
        self.screen = screen

        global og_board
        global a

        if difficulty == "easy":
            self.board = generate_sudoku(9, 30)
            og_board = generate_sudoku(9, 30)
            a = copy.deepcopy(og_board)

        elif difficulty == "medium":
            self.board = generate_sudoku(9, 40)
            og_board = generate_sudoku(9, 40)
            a = copy.deepcopy(og_board)

        else:
            self.board = generate_sudoku(9, 50)
            og_board = generate_sudoku(9, 50)
            a = copy.deepcopy(og_board)

        # self.cells uses a nested for loop to create a 2D array of cells which contain the respective values in board
        self.cells = [[Cell(self.board[i][j], i, j, self.screen) for j in range(9)] for i in range(9)]

        for x in range(0, len(self.board) - 1):
            for y in range(0, len(self.board[0]) - 1):
                if self.board[x][y] > 0:
                    self.cells[x][y].sketched = False

    # will not need this function for the final project
    def print_board(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                print(self.board[i][j], end=" ")
            print()

    """
    Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.  
    Draws every cell on this board.  
    """

    def draw(self):
        self.screen.fill(BG_COLOR)
        # draw lines
        for i in range(0, 10):
            pygame.draw.line(self.screen, LINE_COLOR, (56, SQUARE_SIZE * i),
                             (550, SQUARE_SIZE * i), LINE_WIDTH - 10)
        # draw vertical lines
        for i in range(0, 10):
            pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i + 56, 0),
                             (SQUARE_SIZE * i + 56, 500), LINE_WIDTH - 10)

        # draw bolded lines
        # horizontal
        for i in range(0, 10):
            if i % 3 == 0:
                pygame.draw.line(self.screen, LINE_COLOR, (56, SQUARE_SIZE * i),
                                 (550, SQUARE_SIZE * i), LINE_WIDTH)
                pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i + 56, 0),
                                 (SQUARE_SIZE * i + 56, 500), LINE_WIDTH)

        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw(self.screen)

        # Initialize buttons
        # Initialize text first
        button_font = pygame.font.Font(None, 70)
        reset_text = button_font.render("reset", 0, (255, 255, 255))
        restart_text = button_font.render("restart", 0, (255, 255, 255))
        exit_text = button_font.render("exit", 0, (255, 255, 255))

        # Initialize button background color and text
        reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
        reset_surface.fill(LINE_COLOR)
        reset_surface.blit(reset_text, (10, 10))

        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        restart_surface.fill(LINE_COLOR)
        restart_surface.blit(restart_text, (10, 10))

        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surface.fill(LINE_COLOR)
        exit_surface.blit(exit_text, (10, 10))

        # Initialize button rectangle
        self.reset_rectangle = reset_surface.get_rect(center=(WIDTH - 475, 560))
        self.restart_rectangle = restart_surface.get_rect(center=(WIDTH - 300, 560))
        self.exit_rectangle = exit_surface.get_rect(center=(WIDTH - 125, 560))

        # draw buttons
        self.screen.blit(reset_surface, self.reset_rectangle)
        self.screen.blit(restart_surface, self.restart_rectangle)
        self.screen.blit(exit_surface, self.exit_rectangle)

    """
    Sets the value of the current selected cell equal to user entered value.  
    Called when the user presses the Enter key.  
    """

    def place_number(self, row, col, chip_type):
        self.cells[row][col].sketched = True
        self.board[row][col] = chip_type
        self.update_cells()
        self.cells[row][col].selected = True

    """
    Sets the sketched value of the current selected cell equal to user entered value.  
    It will be displayed at the top left corner of the cell using the draw() function. 
    """

    def sketch(self, value, row, col):
        self.cells[row][col].sketched = True
        self.board[row][col] = value
        self.update_cells()
        self.cells[row][col].sketched = True

    """
    Marks the cell at (row, col) in the board as the current selected cell.  
    Once a cell has been selected, the user can edit its value or sketched value.   
    """

    def select(self, row, col):
        self.update_cells()
        self.cells[row][col].selected = True

    """
    If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col) 
    of the cell which was clicked. Otherwise, this function returns None. 
    """

    def click(self, x, y):
        if 0 <= x <= 8:
            if 0 <= y <= 8:
                return [x, y]
        else:
            return None

    """
    Clears  the  value  cell.  Note  that  the  user  can  only  remove  the  cell  values  and  sketched  value  that  are 
    filled by themselves.  
    """

    def clear(self):
        self.click()
        self.cells[row][col].value = 0

    def update_cells(self):
        self.cells = [[Cell(self.board[i][j], i, j, self.screen) for j in range(9)] for i in range(9)]

    """
    Check whether the Sudoku board is solved correctly.  
    """

    def check_board(self):
        count = 0
        row = 0
        num = 0
        range_start = 1
        curr = self.board[0][0]
        gate = True
        while gate == True:
            # check for duplicate in rows
            for i in range(range_start, len(self.board[0])):  # 0-8
                if curr == self.board[row][i]:
                    count += 1
                    gate = False
                    break
                else:
                    pass
            num += 1
            range_start += 1
            if range_start > len(self.board[0]):
                range_start = 1
                row += 1
                num = 0
            if row > 8:
                break

            curr = self.board[row][num]

        if count > 0:
            return False
        else:
            return True

    """
    Returns a Boolean value indicating whether the board is full or not.  
    """

    def is_full(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return False
        return True

    """
    Finds an empty cell and returns its row and col as a tuple (x, y). 
    """

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i, j] == 0:
                    return tuple((i, j))

    """
    Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).  
    """

    def reset_to_original(self):
        global og_board
        global a
        self.board = a
        self.update_cells()





