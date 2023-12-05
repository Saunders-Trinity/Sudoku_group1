import pygame
from sudoku_generator import SudokuGenerator
from board import Board
from cell import Cell
from scenes import Scene

# constants
width = 600
height = 600
# colors
gator_blue = (0, 33, 165)
gator_orange = (250, 70, 22)
white = (255, 255, 255)
black = (0, 0, 0)

# main menu
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("COP3502c Sudoku Project!")
screen.fill(gator_blue)

# text presets
title_font_size = pygame.font.SysFont(None, 72)
subtitle_font_size = pygame.font.SysFont(None, 45)
regular_font_size = pygame.font.SysFont(None, 30)

title = title_font_size.render("Welcome to Sudoku!", True, (250, 70, 22))
subtitle = subtitle_font_size.render("Select Game Mode:", True, (250, 70, 22))
easy_text = regular_font_size.render("Easy", True, (250, 70, 22))
medium_text = regular_font_size.render("Medium", True, (250, 70, 22))
hard_text = regular_font_size.render("Hard", True, (250, 70, 22))

reset = regular_font_size.render("RESET", True, (0, 128, 0))
restart = regular_font_size.render("RESTART", True, (0, 128, 0))
exit = regular_font_size.render("EXIT", True, (0, 128, 0))
restart_square = pygame.Rect((225, 550), (reset.get_width(), reset.get_height()))
reset_square = pygame.Rect((55,550), (restart.get_width(), restart.get_height()))
exit_square = pygame.Rect((425,550), (restart.get_width(), restart.get_height()))

# drawing the squares (clickable buttons)
easy_square = pygame.draw.rect(screen, white, pygame.Rect(60, 445, 80, 30))
med_square = pygame.draw.rect(screen, white, pygame.Rect(250, 445, 80, 30))
hard_square = pygame.draw.rect(screen, white, pygame.Rect(445, 445, 80, 30))

# printing the text
screen.blit(title, (80, 100))
screen.blit(subtitle, (150, 350))
screen.blit(easy_text, (80, 450))
screen.blit(medium_text, (250, 450))
screen.blit(hard_text, (450, 450))

pygame.display.flip()

def lower_buttons():  # prints the lower buttons
    reset = regular_font_size.render("RESET", True, (0, 0, 0))
    restart = regular_font_size.render("RESTART", True, (0, 0, 0))
    exit = regular_font_size.render("EXIT", True, (0, 0, 0))
    screen.blit(reset, (55, 550))
    screen.blit(restart, (225, 550))
    screen.blit(exit, (425, 550))


# running the main game loop
run_sudoku = True
while run_sudoku:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # selecting the easy option
            if easy_square.collidepoint(event.pos):
                sudoku_screen = pygame.display.set_mode((540, 600))
                pygame.display.set_caption("Difficulty: Easy")
                sudoku_screen.fill(white)
                lower_buttons()
                pygame.display.flip()

            # selecting the medium option
            elif med_square.collidepoint(event.pos):
                sudoku_screen = pygame.display.set_mode((540, 600))
                pygame.display.set_caption("Difficulty: Medium")
                sudoku_screen.fill(white)
                lower_buttons()
                pygame.display.flip()

            # selecting the hard option
            elif hard_square.collidepoint(event.pos):
                sudoku_screen = pygame.display.set_mode((540, 600))
                pygame.display.set_caption("Difficulty: Hard")
                sudoku_screen.fill(white)
                lower_buttons()
                screen.fill((255, 255, 255))

                # grid i found online, havent played around with the sizing/location of the lines yet tho
                for i in range(10):
                    w = 3 if i == 3 or i == 6 else 1
                    pygame.draw.line(screen, (0, 0, 0), (50, 50 + i * 30), (320, 50 + i * 30), w)
                    pygame.draw.line(screen, (0, 0, 0), (50 + i * 30, 50), (50 + i * 30, 320), w)
                pygame.display.flip()


            if reset_square.collidepoint(event.pos):  # restarting the whole game
                pass

            if restart_square.collidepoint(event.pos):  # resetting the current game with randomized numbers
                pass

            if exit_square.collidepoint(event.pos):  # exiting the game
                run_sudoku = False

            # need to create winner and loser/game over screens