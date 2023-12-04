# from sudokugenerator import SudokuGenerator as sg
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((700, 500))  #   home screen for the game (width, height)
pygame.display.set_caption("SUDOKU")
mouse = pygame.mouse.get_pos()

# height and width of displayed features (text)
width = 800
height = 800

# game screen color
white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)  # button color
dark_grey = (169, 169, 169) # button hover color

def start_menu():
    global easy_box

    screen.fill((255, 255, 255))

    font = pygame.font.SysFont('Garamond', 50)
    title = font.render('Welcome to Sudoku!', True, (0, 0, 0))
    easy_text = font.render('Easy', True, black)
    medium_text = font.render('Medium', True, black)
    hard_text = font.render('Hard', True, black)


    mouse = pygame.mouse.get_pos()

    # adding the boxes
    easy_box = pygame.draw.rect(screen, dark_grey, [width / 3 - 50, height / 4, 200, 50])
    if width / 3 - 50 <= mouse[0] <= width / 3 - 50 + 200 and height / 4 <= mouse[1] <= height / 4 + 50:
        easy_box = pygame.draw.rect(screen, grey, [width / 3 - 50, height / 4, 200, 50])

    med_box = pygame.draw.rect(screen, dark_grey, [width / 3 - 50, height / 4 + 75, 200, 50])
    if width / 3 - 50 <= mouse[0] <= width / 3 - 50 + 200 and height / 4 + 75 <= mouse[1] <= height / 4 + 125:
        med_box = pygame.draw.rect(screen, grey, [width / 3 - 50, height / 4 + 75, 200, 50])

    hard_box = pygame.draw.rect(screen, dark_grey, [width / 3 - 50, height / 4 + 150, 200, 50])
    if width / 3 - 50 <= mouse[0] <= width / 3 - 50 + 200 and height / 4 + 150 <= mouse[1] <= height / 4 + 200:
        hard_box = pygame.draw.rect(screen, grey, [width / 3 - 50, height / 4 + 150, 200, 50])

    # displaying the features to the screen
    screen.blit(title, (width / 6, height / 8))
    screen.blit(easy_text, (width / 3, height / 4))
    screen.blit(medium_text, (width / 4 + 35, height / 4 + 75))
    screen.blit(hard_text, (width / 3, height / 4 + 150))
    pygame.display.update()

# def run_game():
#     screen.fill((255, 255, 255))
#
#     font = pygame.font.SysFont('Garamond', 50)
#     title = font.render('Welcome to Sudoku!', True, (0, 0, 0))


gamestate = "menu"

game_run = True
while game_run:
    for event in pygame.event.get():
        if event.type == QUIT:  # quits window if x button pressed
            game_run = False

    if gamestate == "menu":
        start_menu()
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if (easy_box.collidepoint(mouse_pos)):
                gamestate = 'easy_mode'
                print("yay")

    elif gamestate == 'easy_mode':
        run_game()






    rect = pygame.Rect(10, 20, 30, 30)

