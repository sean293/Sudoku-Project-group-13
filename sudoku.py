from linecache import checkcache
import pygame, sys
from constants import *
from board import Board
from board import *
import numpy as np

def draw_game_start(screen):
    # initialize the title and instruction fonts, the number controls for the size of the font
    start_title_font = pygame.font.Font(None, 100)
    instruction_font = pygame.font.Font(None, 60)
    button_font = pygame.font.Font(None, 70)  # button font to be used for the difficulty buttons

    # Fills the entire screen with one color, can be used to erase everything on the screen currently
    screen.fill(BG_COLOR)

    """
    Pay attention to this, this is used a lot throughout the project to set up objects that you see on the screen
    Process of creating objects (buttons, text, lines, etc.):
    First create a "surface" - use previously created font along with render method. first parameter is the text, second
    parameter is always 0, and third parameter is the color of the object
    next, create a rectangle using the surface we just created. The only parameter for get rect is a tuple for the x y 
    cords
    Finally blit the surface and rectangle to the screen
    """
    title_surface = start_title_font.render("Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    instruction_surface = instruction_font.render("Select Game Mode:", 0, LINE_COLOR)
    instruction_rectangle = instruction_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 75))
    screen.blit(instruction_surface, instruction_rectangle)

    # Initialize buttons
    # Initialize text first
    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))

    # Initialize button background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10, 10))

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(center=(WIDTH - 500, HEIGHT // 2))
    medium_rectangle = medium_surface.get_rect(center=(WIDTH - 300, HEIGHT // 2))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH - 100, HEIGHT // 2))

    # draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    # whlie loop for the user to choose the difficulty
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  # exits the progrma/game
            if event.type == pygame.MOUSEBUTTONDOWN:
                # clicking the difficulty button will return the respective difficulty for the game
                if easy_rectangle.collidepoint(event.pos):
                    return "easy"
                elif medium_rectangle.collidepoint(event.pos):
                    return "medium"
                elif hard_rectangle.collidepoint(event.pos):
                    return "hard"
        pygame.display.update()


def draw_game_over(screen):
    # initialize fonts
    button_font = pygame.font.Font(None, 70)
    game_over_font = pygame.font.Font(None, 40)

    screen.fill(BG_COLOR)  # clears the screen

    """
    checks if the user has won the game, if the user has, then print the game won screen and display the exit button,
    which the user can use to exit the program. If the user lost, then display the game over screen and display the
    restart button which the user can press to restart the game.
    """
    if board.check_board() == True:  
        # set up end-of-game screen
        game_over_surf = game_over_font.render("Game Won!", 0, LINE_COLOR)
        game_over_rect = game_over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        screen.blit(game_over_surf, game_over_rect)

        # initialize exit button
        exit_text = button_font.render("Exit", 0, (255, 255, 255))

        # Initialize and draw button
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surface.fill(LINE_COLOR)
        exit_surface.blit(exit_text, (10, 10))

        # Creates a rectangle object to be drawn on to the screen
        exit_rectangle = exit_surface.get_rect(center=(WIDTH - 300, HEIGHT // 2))

        # draw
        screen.blit(exit_surface, exit_rectangle)

        # checks to see if the user clicks on the screen
        if event.type == pygame.MOUSEBUTTONDOWN:
            #  If the user clicks on the exit button, quit the program
            if exit_rectangle.collidepoint(event.pos):
                sys.exit()
    else:
        # set up end-of-game screen
        game_over_surf = game_over_font.render("Game Over :(", 0, LINE_COLOR)
        game_over_rect = game_over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        screen.blit(game_over_surf, game_over_rect)

        # initialize restart button
        # initialize exit button
        restart_text = button_font.render("Restart", 0, (255, 255, 255))

        # Initialize and draw button
        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        restart_surface.fill(LINE_COLOR)
        restart_surface.blit(restart_text, (10, 10))

        # rectangle
        restart_rectangle = restart_surface.get_rect(center=(WIDTH - 300, HEIGHT // 2))

        # draw
        screen.blit(restart_surface, restart_rectangle)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if restart_rectangle.collidepoint(event.pos):
                draw_game_start(screen)  # puts the user back to the start screen
                board.reset_to_original()  
                screen.fill(BG_COLOR)  # clears the screen after the user chooses a difficulty
                board.draw()  # draws the board with all of the values on the screen



if __name__ == '__main__':
    game_over = False  # not sure if this is needed
    winner = 0  # not sure if this is needed either

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # sets up the main screen
    pygame.display.set_caption("Sudoku")  # sets the title of the new window

    difficulty = draw_game_start(screen)  # Calls function to draw start screen
    screen.fill(BG_COLOR)  # clears the screen to draw the board
    board = Board(9, 9, screen, difficulty)  # set up a new board
    board.draw()  # draw the board

    

    # main loop where game is played
    while game_over == False:
        # pygame events are actions like clicking or pushing a key
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  # exits the game
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                clicked_row = int(event.pos[1] / SQUARE_SIZE)  # gets the y value for the sudoku board
                clicked_col = int(event.pos[0] / SQUARE_SIZE) - 1  # gets the x value for the sudoku board

                # if statements to check if the buttons at the bottom of the screen are selected
                if board.reset_rectangle.collidepoint(event.pos):
                    pygame.display.update()
                    board.reset_to_original()

                elif board.restart_rectangle.collidepoint(event.pos):
                    board.reset_to_original()
                    draw_game_start(screen)

                    
                elif board.exit_rectangle.collidepoint(event.pos):
                    sys.exit()

                # makes sure that the user can't click outside the board, without this, if the user clicks outside
                # the board, the game will quit because of an error (Index out of range error)
                if clicked_col > 8 or clicked_col < 0 or clicked_row > 8:
                    continue

                board.select(clicked_row, clicked_col)  # selects the cell at the given x, y coordinates

                print(clicked_row, clicked_col)  # prints out the x, y coordinates to make debugging easier

                board.draw()  # updates the board

                board.print_board()  # prints the board and the values stored in it to help with debugging

            """
            checks for when the user presses a key, in this case, the only keys that can be pressed are the backspace
            key and the keys 1-9
            """
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    board.place_number(clicked_row, clicked_col, 0) # FIXME mark_square needs to be replaced with clear here
                    screen.fill(BG_COLOR)  # clears the screen
                    board.draw()  # draws the board
                    pygame.display.update()
                """
                For every number key pressed, changes the value in the cell to the respective number key pressed. Still 
                missing some functionality like making sure the values that exist at the beginning of the game can't 
                be changed
                """
                if event.key == pygame.K_1:
                    board.place_number(clicked_row, clicked_col, 1)
                    screen.fill(BG_COLOR)
                    board.draw()
                    pygame.display.update()
                if event.key == pygame.K_2:
                    board.place_number(clicked_row, clicked_col, 2)
                    screen.fill(BG_COLOR)
                    board.draw()
                    pygame.display.update()
                if event.key == pygame.K_3:
                    board.place_number(clicked_row, clicked_col, 3)
                    screen.fill(BG_COLOR)
                    board.draw()
                    pygame.display.update()
                if event.key == pygame.K_4:
                    board.place_number(clicked_row, clicked_col, 4)
                    screen.fill(BG_COLOR)
                    board.draw()
                    pygame.display.update()
                if event.key == pygame.K_5:
                    board.place_number(clicked_row, clicked_col, 5)
                    screen.fill(BG_COLOR)
                    board.draw()
                    pygame.display.update()
                if event.key == pygame.K_6:
                    board.place_number(clicked_row, clicked_col, 6)
                    screen.fill(BG_COLOR)
                    board.draw()
                    pygame.display.update()
                if event.key == pygame.K_7:
                    board.place_number(clicked_row, clicked_col, 7)
                    screen.fill(BG_COLOR)
                    board.draw()
                    pygame.display.update()
                if event.key == pygame.K_8:
                    board.place_number(clicked_row, clicked_col, 8)
                    screen.fill(BG_COLOR)
                    board.draw()
                    pygame.display.update()
                if event.key == pygame.K_9:
                    board.place_number(clicked_row, clicked_col, 9)
                    screen.fill(BG_COLOR)
                    board.draw()
                    pygame.display.update()

            # game is over
            if board.is_full() == True:

                pygame.time.delay(100)
                draw_game_over(screen)
            else:
                pass
        pygame.display.update()






